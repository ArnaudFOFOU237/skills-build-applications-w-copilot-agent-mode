"""Main application entry point for OctoFit Tracker App."""

from src.joke_generator import JokeGenerator
from src.fitness_tracker import FitnessTracker


def print_menu():
    """Print the main menu."""
    print("\n" + "="*50)
    print("🐙 OCTOFIT TRACKER APP")
    print("="*50)
    print("1. Get a random joke")
    print("2. Get a programming joke")
    print("3. Add a fitness activity")
    print("4. View fitness statistics")
    print("5. View all activities")
    print("6. Exit")
    print("="*50)


def main():
    """Main application loop."""
    joke_generator = JokeGenerator()
    fitness_tracker = FitnessTracker()
    
    print("\n🐙 Welcome to OctoFit Tracker App!")
    print("Track your fitness and stay motivated with jokes.\n")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\nFetching a random joke...")
            joke = joke_generator.get_random_joke()
            joke_generator.print_joke(joke)
        
        elif choice == "2":
            print("\nFetching a programming joke...")
            joke = joke_generator.get_motivational_joke()
            joke_generator.print_joke(joke)
        
        elif choice == "3":
            print("\n--- Add Fitness Activity ---")
            activity_type = input("Activity type (e.g., running, yoga, weightlifting): ").strip()
            
            try:
                duration = int(input("Duration (minutes): "))
                activity = fitness_tracker.add_activity(activity_type, duration)
                print(f"✅ Activity added: {activity}")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number for duration.")
        
        elif choice == "4":
            fitness_tracker.print_statistics()
        
        elif choice == "5":
            fitness_tracker.print_activities()
        
        elif choice == "6":
            print("\n👋 Thanks for using OctoFit Tracker App!")
            joke_generator.close()
            break
        
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
