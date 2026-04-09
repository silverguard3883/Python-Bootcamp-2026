import requests

"""Parameters for API URL"""
PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

quiz_questions = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
quiz_questions.raise_for_status()
question_data = quiz_questions.json()["results"]