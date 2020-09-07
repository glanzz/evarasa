import requests,json
import os
import logging


def updateName(user_id, name):
  
  send_data = [{
      "user_name": name,
      "id": user_id,
  }]
  url = "http://127.0.0.1:3001/students?updateName=True"
  os.environ['no_proxy'] = '127.0.0.1,localhost'
  resp = requests.post(url, json = send_data)
  logging.basicConfig(filename="databaselogs.log")
  logger=logging.getLogger()
  logger.info(f"id {user_id}")
  logger.info(resp.json())
  
def get_student_details(user_id):
  url = f"http://127.0.0.1:3001/students?id={user_id}"
  os.environ['no_proxy'] = '127.0.0.1,localhost'
  resp = requests.get(url)
  if resp.status_code == 200:
    response = resp.json()
    return response
  logging.basicConfig(filename="databaselogs.log")
  logger=logging.getLogger()
  logger.info(resp.json())
  logger.info(user_id)
  return {}
  
  
def updateScores(user_id, send_data):
  send_data["user_id"] = user_id
  url = "http://127.0.0.1:3001/scores"
  os.environ['no_proxy'] = '127.0.0.1,localhost'
  resp = requests.post(url, json = send_data)
  logging.basicConfig(filename="databaselogs.log")
  logger=logging.getLogger()
  logger.info(send_data)
  logger.info(resp.json())

def insertQuestionAnswers(question, answer, user_id):
  send_data = {
      "question": question,
      "answer": answer,
      "user_id": user_id,
  }
  url = "http://127.0.0.1:3001/reasons"
  os.environ['no_proxy'] = '127.0.0.1,localhost'
  resp = requests.post(url, json = send_data)
  logging.basicConfig(filename="databaselogs.log")
  logger=logging.getLogger()
  logger.info(resp.json())