## flow1
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Geetha"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "90"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"Maths"}
  - action_process_favourite_subject
  - slot{"teachers_score": 0.444}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 0.8052}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 1.2071}
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.8126}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 1.6568, "family_score": 0.8442 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 1.7322 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 2.1341 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye




## flow2
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Nazira"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"cgpa": "9"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"Mathematics"}
  - action_process_favourite_subject
  - slot{"teachers_score": 0.888}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 0.6125}
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": -0.3724 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": -0.6479 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.1963, "family_score": 0.8442 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 1.9642 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 2.3661 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye


## flow3
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Fazil"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "90"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": -0.296 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.1506 }
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"Mathematics"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.175}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 0.8138}
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.958}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 1.0183, "family_score": 0.0603 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.9483 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 1.3502 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye

## flow4
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Janardhan"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* dont_start
  - utter_no_issues
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "4"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.6597}
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"Maths","subject2": "Physics", "subject3": "Chemistry", "subject4": "Geography", "subject5": "Computer Science"}
  - action_process_favourite_subject
  - slot{"teachers_score": 2.1037}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 2.1037}
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": 0.25 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": -0.1224 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": -0.0621, "family_score": 0.0603 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.5043 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.9062 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye

## flow5
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Narpinder"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"cgpa": "9"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": -0.296 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.7003 }
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"Biology","subject2": "History", "subject3": "Civics"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.148}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 1.148}
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": 0.8653 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": 0.6243 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.8506, "family_score": 0.2263 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.6703 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.6703 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye  


## flow6
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Baljeet Kaur"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* dont_start
  - utter_no_issues
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"cgpa": "9"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.6597}
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"Geography","subject2": "Computer Science", "subject3": "PE"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 0.0}
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.8074}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.2263, "family_score": 0.2263 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye


## flow7
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "John"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"cgpa": "9"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"English 1"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": -0.2755}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.0}
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": 0.7269 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": 0.4939 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": -0.296, "family_score": -0.296 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye

## flow8
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - slot{"user_name": "dear"}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"cgpa": "9.98"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"PE"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": 0.0 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.128 }
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": -0.069 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": 0.0 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": -0.296, "family_score": -0.296 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye

## flow9
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Rahul Sharma"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "40"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subjectall": "all subjects"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": -0.296 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.2144 }
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": -0.0346 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": 0.0 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.3182, "family_score": 0.3182 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye

## flow10
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Karan B U"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"cgpa": "5"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subjectall": "every subject"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.4019}
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": -0.0346 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": 0.0 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.3182, "family_score": 0.3182 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye

## flow11
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Sheela"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "10"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subjectall": "every subjects"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": 0.0 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.4019 }
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.8074}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.25, "family_score": 0.25 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye


## flow12
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Vindya"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "5"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subjectall": "all the subjects"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.4019}
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.8074}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.25, "family_score": 0.25 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye


## flow13
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Susan"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "4"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subject1": "Kannada", "subject2": "CS"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": -0.5719}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": 0.0 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.2144 }
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.4767}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": -0.296, "family_score": -0.296 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye


## flow14
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Ria Thomas"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_favourite_subject
* tell_favourite_subject{"subjectall": "all the subjects"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
  - utter_ask_percentage
* tell_score{"percentage": "100"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.4019}
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.4767}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": -0.296, "family_score": -0.296 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": 0.0 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye




## flow15
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Sumanth"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_favourite_subject
* tell_favourite_subject{"subjectall": "all the subjects"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
  - utter_ask_percentage
* tell_score{"cgpa": "10"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": -0.296 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.0 }
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": -0.069 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": 0.0 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.0, "family_score": 0.0 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": -0.296 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye


## flow16
* greet
  - utter_greet
  - utter_ask_name
* tell_name
  - slot{"user_name": "Sowmya"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"percentage": "50"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_favourite_subject
* tell_favourite_subject{"subject1":"Physics"}
  - action_process_favourite_subject
  - slot{"teachers_score": 1.444}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_negetive
  - action_record_reason
  - slot{"teachers_score": 0.0 }
  - utter_ask_teacher_help
* tell_ask_teacher_help
  - action_record_reason
  - slot{"friends_score": 0.0 }
  - utter_ask_best_friends
* tell_best_friends_negetive
  - action_record_reason
  - slot{"friends_score": 0.2263 }
  - utter_why_no_friends
* tell_no_friends_reason
  - action_record_reason
  - slot{"friends_score": 0.0 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.0, "family_score": 0.0 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": -0.296 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye
  
## interactive_story_1
* greet
  - utter_greet
  - utter_ask_name
* tell_name{"user_name": "Bhargav Vishnu"}
  - slot{"user_name": "Bhargav Vishnu"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* ok_start
  - utter_pacifier
  - utter_academics_intro
  - utter_favourite_subject
* tell_favourite_subject{"subject1": "Maths"}
  - action_process_favourite_subject
  - slot{"teachers_score": 0.434}
* tell_reason_for_no_fav
  - action_record_reason
  - slot{"teachers_score": -0.5719}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.0}
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.8126 }
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.0, "family_score": 0.0 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 0.444 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": -0.296 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye

## interactive_story_1
* greet
  - utter_greet
  - utter_ask_name
* tell_name{"user_name": "Sumanth Reddy"}
  - slot{"user_name": "Sumanth Reddy"}
  - action_introduce_and_respond_to_name
  - slot{"family_score": 0.0, "teachers_score": 0.0, "friends_score": 0.0}
  - utter_start
* dont_start
  - utter_no_issues
  - utter_academics_intro
  - utter_ask_percentage
* tell_score{"cgpa": "1.1"}
  - action_process_score
  - slot{"teachers_score": 0.0}
  - utter_teacher_help
* tell_help_reason_positive
  - action_record_reason
  - slot{"teachers_score": 0.4019}
  - utter_ask_best_friends
* tell_best_friends_positive
  - action_record_reason
  - slot{"friends_score": 0.8126}
  - utter_parents_allow
* tell_parents_allow
  - action_record_reason
  - slot{"friends_score": 0.2263, "family_score": 0.2263 }
  - utter_decision
* tell_decision_support
  - action_record_reason
  - slot{"family_score": 1.151 }
  - utter_more_preference
* tell_more_preference
  - action_record_reason
  - slot{"family_score": -0.296 }
  - action_process_bye
  - utter_bye
* stop_bot_eva
  - action_process_bye
  - utter_bye


## fallback story
* out_of_scope
  - action_final_fallback