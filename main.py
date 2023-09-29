# main.py

from database import Database
from api_integration import APIIntegration
from ai_ad_generation import AIGeneration
from keyword_suggestions import KeywordSuggestions
from remarketing import Remarketing
from analytics import Analytics
from user_interface import UserInterface
from security import Security
from network_access import NetworkAccess

def main():
    # Initialise the database
    Database.initialise()

    # Initialise the user interface
    ui = UserInterface()

    # User login
    user = ui.login()
    if user is None:
        print("Failed to authenticate user.")
        return

    # Check for multi-factor authentication
    if Security.is_mfa_enabled(user):
        if not Security.authenticate_mfa(user):
            print("Failed to authenticate user via MFA.")
            return

    # Main application loop
    while True:
        # Display the main menu and get the user's choice
        choice = ui.main_menu()

        if choice == '1':
            # Generate ad copy
            prompt = ui.get_ad_prompt()
            ad_copy = AIGeneration.generate_ad(prompt)
            ui.display_ad_copy(ad_copy)

        elif choice == '2':
            # Get keyword suggestions
            platform = ui.get_platform_choice()
            keywords = KeywordSuggestions.get_trending_keywords(platform)
            ui.display_keywords(keywords)

        elif choice == '3':
            # Track user interaction
            interaction = ui.get_user_interaction()
            Remarketing.track_user_interaction(user, interaction)

        elif choice == '4':
            # Track ad performance
            ad_id = ui.get_ad_id()
            performance = Analytics.track_ad_performance(ad_id)
            ui.display_ad_performance(performance)

        elif choice == '5':
            # Exit the application
            break

        else:
            print("Invalid choice. Please try again.")

    # Close all database connections
    Database.close_all_connections()

if __name__ == "__main__":
    main()