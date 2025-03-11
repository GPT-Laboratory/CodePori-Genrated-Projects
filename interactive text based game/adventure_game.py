import json

def load_story(file_path="story.json"):
    """Loads the story data from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)

def display_scene(scene):
    """Displays the current scene text and choices."""
    print("\n" + scene["text"])
    if scene["choices"]:
        print("\nChoices:")
        for choice in scene["choices"]:
            print(f"- {choice}")

def get_player_choice(choices):
    """Gets the player's choice and ensures it is valid."""
    while True:
        choice = input("\nWhat do you do? ").lower().strip()
        if choice in choices:
            return choice
        print("Invalid choice. Please try again.")

def play_game():
    """Main function to run the game."""
    story = load_story()
    current_scene = "start"

    while True:
        scene = story[current_scene]
        display_scene(scene)

        if not scene["choices"]:
            print("\nGame Over!")
            break

        choice = get_player_choice(scene["choices"])
        current_scene = scene["choices"][choice]

if __name__ == "__main__":
    play_game()
