# Module: app.py

import recipe_finder

def main_menu():
    while True:
        print("\nRecipe Finder Menu:")
        print("1. Search by Ingredient")
        print("2. Search by Cuisine")
        print("3. Search by Dietary Preference")
        print("4. View Recipe Instructions")
        print("5. Add a Review")
        print("6. Save Recipe to Favorites")
        print("7. View Favorite Recipes")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            ingredient = input("Enter an ingredient to search for: ")
            recipe_finder.search_by_ingredients(ingredient)
        elif choice == "2":
            cuisine = input("Enter a cuisine to search for: ")
            recipe_finder.search_by_cuisine(cuisine)
        elif choice == "3":
            diet = input("Enter a dietary preference to search for: ")
            recipe_finder.search_by_diet(diet)
        elif choice == "4":
            recipe_id = int(input("Enter the recipe ID to view instructions: "))
            recipe_finder.view_instructions(recipe_id)
        elif choice == "5":
            recipe_id = int(input("Enter the recipe ID to add a review: "))
            review = input("Enter your review: ")
            recipe_finder.add_review(recipe_id, review)
        elif choice == "6":
            recipe_id = int(input("Enter the recipe ID to save to favorites: "))
            recipe_finder.save_to_favorites(recipe_id)
        elif choice == "7":
            recipe_finder.view_favorites()
        elif choice == "8":
            print("Exiting Recipe Finder. Goodbye!")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 8.")

if __name__ == "__main__":
    main_menu()
