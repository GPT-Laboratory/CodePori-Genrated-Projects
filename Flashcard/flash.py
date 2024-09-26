import json
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardApp:
    def __init__(self, file_name="flashcards.json"):
        self.file_name = file_name
        self.flashcards = []
        self.load_flashcards()

    def load_flashcards(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                for entry in data:
                    self.flashcards.append(Flashcard(entry['question'], entry['answer']))
        except FileNotFoundError:
            print("No flashcards found. You can start adding new flashcards.")

    def save_flashcards(self):
        with open(self.file_name, 'w') as file:
            json.dump([{"question": fc.question, "answer": fc.answer} for fc in self.flashcards], file, indent=4)

    def add_flashcard(self, question, answer):
        self.flashcards.append(Flashcard(question, answer))
        self.save_flashcards()
        print(f"Flashcard '{question}' added.")

    def view_flashcards(self):
        if not self.flashcards:
            print("No flashcards available.")
        else:
            print("\n--- All Flashcards ---")
            for idx, fc in enumerate(self.flashcards, 1):
                print(f"{idx}. Q: {fc.question} | A: {fc.answer}")
            print("\n")

    def quiz_user(self):
        if not self.flashcards:
            print("No flashcards available for quiz.")
            return

        random.shuffle(self.flashcards)  # Randomize the order
        correct = 0

        print("\n--- Quiz Time ---")
        for flashcard in self.flashcards:
            print(f"Question: {flashcard.question}")
            user_answer = input("Your Answer: ").strip()

            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!\n")
                correct += 1
            else:
                print(f"Incorrect! The correct answer is: {flashcard.answer}\n")

        print(f"Quiz Over! You got {correct} out of {len(self.flashcards)} correct.")

    def main_menu(self):
        while True:
            print("\n--- Flashcard App Menu ---")
            print("1. Add Flashcard")
            print("2. View Flashcards")
            print("3. Quiz Yourself")
            print("4. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                question = input("Enter the question: ").strip()
                answer = input("Enter the answer: ").strip()
                self.add_flashcard(question, answer)
            elif choice == "2":
                self.view_flashcards()
            elif choice == "3":
                self.quiz_user()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = FlashcardApp()
    app.main_menu()
