# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"



from typing import Any, Text, Dict, List
import random
import requests, json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from databaseutil import updateName, get_student_details, updateScores, insertQuestionAnswers

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionRespondToName(Action):
  
  def name(self) -> Text:
    return "action_introduce_and_respond_to_name"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    
    user_name = tracker.get_slot("user_name")
    user_id = tracker.sender_id
    introduction_sentence = ("My name is Eva assistant counsellor. " 
                        "For the next few minutes we shall have a conversation where most of the times "
                        "I ask question and you would answer. "
                        "I want you to be comfortable and Feel free to interact with me. ")
    if user_name:
      updateName(user_id, user_name)
      details = get_student_details(user_id)
      family_score = details.get("family_score",0)
      teachers_score = details.get("teachers_score",0)
      friends_score = details.get("friends_score",0)
      dispatcher.utter_message(f"Nice to meet you {user_name}!")
      dispatcher.utter_message(introduction_sentence)
      return [SlotSet("family_score",family_score), 
              SlotSet("teachers_score",teachers_score),
              SlotSet("friends_score",friends_score)]
    else:
      dispatcher.utter_message(f"Oh Dear! I did not get your name, Thats Fine Lets continue!")
      dispatcher.utter_message(introduction_sentence)
      user_name = "Dear"
      return [SlotSet("user_name",user_name)]



class ActionProcessScore(Action):
  
  def __init__(self):
    self.more_positive_response = ["Congrats! Hard work pays off always.",
                                   "Wow! I am talking to a genius. Congratulations!", 
                                   "Congrats! I am glad to hear that.", 
                                   "Well Done! I am glad to hear that. Congratulations!",
                                   "You Seem to be a bright student! Keep this going. Congrats"]
    self.positive_response = ["Thats a good scoring. You can try for more next time.", 
                              "Ohh! That is good. I know you have even more potential to score more", 
                              "Wonderful! Keep that spirit"]
    self.negetive_response = ["Ohh! Dont worry. Its a long way ahead. You can try next time",
                              "I am sure that If you try a little bit more. You can do well in upcoming exams",
                              "Dont worry. You can do well in upcoming exams"]
    self.utter_message = "Hmm Ok"
    self.contexts = {"CGPA": "CGPA", "PERCENT":"PERCENT"}
  
  def name(self) -> Text:
    return "action_process_score"

  def set_utter_message(self, score, context):
    if context =="CGPA":
      if score >= 8 and score <= 10:
        self.utter_message = self.more_positive_response[random.randint(0,len(self.more_positive_response)-1)]
      if score < 8 and score > 4:
        self.utter_message = self.positive_response[random.randint(0,len(self.positive_response)-1)] 
      if score <=4 and score >= 0:
        self.utter_message = self.negetive_response[random.randint(0,len(self.negetive_response)-1)]
    if context == "PERCENT":
      if score >= 80 and score <= 100:
        self.utter_message = self.more_positive_response[random.randint(0,len(self.more_positive_response)-1)]
      if score < 80 and score > 45:
        self.utter_message = self.positive_response[random.randint(0,len(self.positive_response)-1)] 
      if score <=45 and score >= 0:
        self.utter_message = self.negetive_response[random.randint(0,len(self.negetive_response)-1)]
    
  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    percentage = next(tracker.get_latest_entity_values("percentage"), None)
    cgpa = next(tracker.get_latest_entity_values("cgpa"), None)
    question_message = tracker.latest_message["intent"].get("name")
    answer_message = tracker.latest_message['text']
    for event in tracker.events:
      if (event.get("event") == "bot") and (event.get("event") is not None):
          question_message = event.get("text")
    
    sentimentAnalyze = SentimentIntensityAnalyzer()
    sentimentScore = sentimentAnalyze.polarity_scores(answer_message)
    teachers_score = tracker.get_slot('teachers_score') + sentimentScore['compound']
    
    
    if cgpa and str(cgpa).isdigit():
      cgpa = float(cgpa)
      self.set_utter_message(cgpa, self.contexts["CGPA"])
      
    if percentage and str(percentage).isdigit():
      percentage = float(percentage)
      self.set_utter_message(percentage, self.contexts["PERCENT"])
    
    dispatcher.utter_message(self.utter_message)
    return [SlotSet("teachers_score", teachers_score)]







class ActionProcessfavouriteSubject(Action):
  
  def name(self) -> Text:
    return "action_process_favourite_subject"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    subject1 = next(tracker.get_latest_entity_values("subject1"), None)
    subject2 = next(tracker.get_latest_entity_values("subject2"), None)
    subject3 = next(tracker.get_latest_entity_values("subject3"), None)
    subject4 = next(tracker.get_latest_entity_values("subject4"), None)
    subject5 = next(tracker.get_latest_entity_values("subject5"), None)
    subject6 = next(tracker.get_latest_entity_values("subject6"), None)
    subjectall = next(tracker.get_latest_entity_values("subjectall"), None)
    is_plural = False
    utter_message="Dont you have any favourite subject"
    
    if subjectall:
      utter_message = "Really? Hard to believe!"
      
    else:
      plural_set = set([subject1, subject2, subject3, subject4, subject5, subject6])
      if "Computer Science" in plural_set:
        dispatcher.utter_message("I love Computer Science!")
      elif "Maths" in plural_set:
        dispatcher.utter_message("Most of them do not like Maths. But I love that subject")
      elif "Physical Education" in plural_set:
        dispatcher.utter_message("Most of them like this!")
      elif "Language" in plural_set:
        dispatcher.utter_message("Thats really tuff for me to understand! Anyhow i will learn that.")
      utter_message="But, Why dont you like the other subjects?"
      
    question_message = tracker.latest_message["intent"].get("name")
    answer_message = tracker.latest_message['text']
    for event in tracker.events:
      if (event.get("event") == "bot") and (event.get("event") is not None):
          question_message = event.get("text")
    
    sentimentAnalyze = SentimentIntensityAnalyzer()
    sentimentScore = sentimentAnalyze.polarity_scores(answer_message)
    teachers_score = tracker.get_slot('teachers_score') + sentimentScore['compound']
    
    dispatcher.utter_message(utter_message)
    return [SlotSet("teachers_score",teachers_score)]




class ActionProcessBye(Action):
  
  def name(self) -> Text:
    return "action_process_bye"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    scores = {
      "teachers_score":  tracker.get_slot('teachers_score'),
      "family_score" : tracker.get_slot('family_score'),
      "friends_score" : tracker.get_slot('friends_score')
    }
    user_id = tracker.sender_id
    updateScores(user_id,scores)
    dispatcher.utter_message(template="utter_pacifier")




class ActionRecordReason(Action):
  
  def __init__(self):
    self.mapper = {
      "tell_reason_for_no_fav": ["teachers_score"],
      "tell_help_reason_positive": ["teachers_score"],
      "tell_best_friends_positive": ["friends_score"],
      "tell_parents_allow": ["family_score", "friends_score"],
      "tell_decision_support": ["family_score"],
      "tell_more_preference": ["family_score"],
      "tell_best_friends_negetive": ["friends_score"],
      "tell_no_friends_reason": ["friends_score"],
      "tell_ask_teacher_help": ["teachers_score"],
      "tell_help_reason_negetive": ["teachers_score"],
      "dont_start": ["friends_score"],
      
    }
    self.sentimentAnalyze = SentimentIntensityAnalyzer()
    
    
  def name(self) -> Text:
    return "action_record_reason"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    last_intent_name = tracker.latest_message["intent"].get("name")
    question_message = last_intent_name
    answer_message = tracker.latest_message['text']
    user_id = tracker.sender_id
    for event in tracker.events:
      if (event.get("event") == "bot") and (event.get("event") is not None):
          question_message = event.get("text")
    
    insertQuestionAnswers(question_message, answer_message, user_id)
    sentimentScore = self.sentimentAnalyze.polarity_scores(answer_message)
    intents = self.mapper[last_intent_name]
    scores = {
      "teachers_score":  tracker.get_slot('teachers_score'),
      "family_score" : tracker.get_slot('family_score'),
      "friends_score" : tracker.get_slot('friends_score')
    }
    
    dispatcher.utter_message(template="utter_pacifier")
    for intent in intents:
       scores[intent] = scores[intent] + sentimentScore['compound']
    
    
    # positive replies
    if sentimentScore["compound"] >= 0:
      if last_intent_name == "tell_decision_support":
        dispatcher.utter_message(template="utter_positive_decision")
      if last_intent_name == "tell_best_friends_positive":
        dispatcher.utter_message(template="utter_cool")
      if last_intent_name == "tell_help_reason_positive":
        dispatcher.utter_message(template="utter_knew_help")
    
    # negetive replies
    if sentimentScore["compound"] < 0:
      if last_intent_name == "tell_decision_support":
        dispatcher.utter_message(template="utter_negetive_decision")
      if last_intent_name == "tell_help_reason_negetive":
        dispatcher.utter_message(template="utter_ask_doubt")
      if last_intent_name == "tell_no_friends_reason":
        dispatcher.utter_message(template="utter_try_having_friends")
      
    
    return [SlotSet(key, value) for key,value in scores.items()]




class ActionDefaultFallback(Action):
  def __init__(self):
    self.intent_fallback_map = {
      "did_not_tell_name": "Your name was not clear to me. Can you please tell that again?",
      "tell_score": "Can you tell the scoring can be your percentage or CGPA in your last exams or test at school?",
      "tell_favourite_subject": "I asked which subjects do you like in school?",
      "tell_reason_for_no_fav": "I did not get the reason why you dont like the other subjects",
      "tell_help_reason_positive": "I understand that you have asked for help, could tell that more clearly?",
      "tell_help_reason_negetive": "So you have not asked for help anytime?",
      "tell_best_friends_positive": "I could not understand that! Could be more specefic.",
      "tell_best_friends_negetive": "Could you be more specefic?",
      "tell_decision_support": "Could you be more specific if your decisions are supported?",
      "default": "I did not understand could you rephrase it?"
    }
  
  def name(self) -> Text:
    return "action_default_fallback"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    last_intent_name = tracker.latest_message["intent"].get("name")
    utter_message = self.intent_fallback_map["default"]
    if last_intent_name:
      utter_message = self.intent_fallback_map.get(last_intent_name, utter_message)
    dispatcher.utter_message(utter_message)
    
class ActionFinalFallback(Action):
  
  def name(self) -> Text:
    return "action_final_fallback"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    dispatcher.utter_message(f"Sorry I did not get that Ok. Thats fine lets continue!")