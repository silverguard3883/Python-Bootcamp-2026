import requests
from datetime import datetime

WORKOUT_TRACKER_API_KEY = ""
WORKOUT_TRACKER_API_SECRET = ""
WORKOUT_TRACKER_APP_ID = ""
WORKOUT_TRACKER_URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

USERNAME = ""
PROJECTNAME = "workoutTracker"
SHEET_NAME = "sheet1"

SHEETY_URL = f"https://api.sheety.co/{USERNAME}/{PROJECTNAME}/{SHEET_NAME}"

HEADERS = {
    "x-app-id": WORKOUT_TRACKER_APP_ID,
    "x-app-key": WORKOUT_TRACKER_API_KEY,
    "Content-Type": "application/json",
}

query = input("What exercise did you perform? ")

exercise_data = {
    "query": query,
    "weight_kg": 70,            #Optional: Weight in kg(1 - 500)
    "height_cm": 175,           #Optional: Height in cm(1 - 300)
    "age": 30,                  #Optional: Age(1 - 150)
    "gender": "male"            #Optional: "male" or "female"
}

add_workout = requests.post(url=SHEETY_URL, json=exercise_data, headers=HEADERS)
workout_data = add_workout.json()

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for workout in workout_data["exercises"]:
    sheet_input_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": workout["workout"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }

    sheety_response = requests.post(url=SHEETY_URL, json=sheet_input_data)
    print(sheety_response.text)



