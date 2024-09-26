import datetime
import json
import random

class FitnessTracker:
    def __init__(self, user_file="user_data.json"):
        self.activities = []
        self.user_file = user_file
        self.load_user_data()

    def load_user_data(self):
        try:
            with open(self.user_file, 'r') as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = {
                "name": None,
                "age": None,
                "weight": None,
                "height": None,
                "activity_log": []
            }

    def save_user_data(self):
        with open(self.user_file, 'w') as file:
            json.dump(self.user_data, file, indent=4)

    def add_activity(self, activity, duration, calories_burned):
        entry = {
            "activity": activity,
            "duration": duration,
            "calories_burned": calories_burned,
            "date": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.user_data["activity_log"].append(entry)
        self.save_user_data()

    def display_activities(self):
        if not self.user_data["activity_log"]:
            print("No activities recorded yet.")
        else:
            for entry in self.user_data["activity_log"]:
                print(f"Date: {entry['date']}, Activity: {entry['activity']}, Duration: {entry['duration']} mins, "
                      f"Calories burned: {entry['calories_burned']} kcal")

    def track_progress(self):
        total_activities = len(self.user_data["activity_log"])
        total_calories = sum([entry["calories_burned"] for entry in self.user_data["activity_log"]])
        print(f"Total activities: {total_activities}")
        print(f"Total calories burned: {total_calories} kcal")

    def personalized_recommendations(self):
        weight = self.user_data.get("weight", 70)  # Assuming average weight if not set
        recommended_activity = random.choice(["Jogging", "Cycling", "Swimming", "Yoga", "Strength training"])
        recommended_duration = random.randint(20, 40)
        recommended_calories = (recommended_duration * weight * 0.1)  # Simple estimation

        print("Personalized Recommendations:")
        print(f"Try {recommended_activity} for {recommended_duration} minutes.")
        print(f"You'll burn approximately {recommended_calories:.2f} kcal.")

    def update_profile(self):
        self.user_data["name"] = input("Enter your name: ")
        self.user_data["age"] = int(input("Enter your age: "))
        self.user_data["weight"] = float(input("Enter your weight (kg): "))
        self.user_data["height"] = float(input("Enter your height (cm): "))
        self.save_user_data()

    def view_profile(self):
        if not self.user_data["name"]:
            print("No profile found.")
        else:
            print(f"Name: {self.user_data['name']}")
            print(f"Age: {self.user_data['age']}")
            print(f"Weight: {self.user_data['weight']} kg")
            print(f"Height: {self.user_data['height']} cm")

def main():
    tracker = FitnessTracker()

    while True:
        print("\n--- Fitness Tracker Menu ---")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Add Activity")
        print("4. View Activities")
        print("5. Track Progress")
        print("6. Get Personalized Recommendations")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.view_profile()
        elif choice == "2":
            tracker.update_profile()
        elif choice == "3":
            activity = input("Enter activity (e.g., running, cycling): ")
            duration = int(input("Enter duration in minutes: "))
            calories_burned = float(input("Enter calories burned: "))
            tracker.add_activity(activity, duration, calories_burned)
            print(f"Activity '{activity}' recorded.")
        elif choice == "4":
            tracker.display_activities()
        elif choice == "5":
            tracker.track_progress()
        elif choice == "6":
            tracker.personalized_recommendations()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
