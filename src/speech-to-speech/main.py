from can_to_eng import *
from eng_to_can import *

def main():
    """
    Main function to run the translation loop.
    """
    # Initialize the speech engine once at the start
    initialize_speech_engine()
    
    while True:
        print("\nChoose an option:")
        print("1. Speak in Cantonese and translate to English speech")
        print("2. Speak in English and translate to Cantonese speech")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            translate_cantonese_to_english_speech()
        elif choice == '2':
            translate_english_to_cantonese_speech()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()