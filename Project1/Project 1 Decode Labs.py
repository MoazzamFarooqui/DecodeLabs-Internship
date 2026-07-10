import sys

def sanitize_input(raw_text: str) -> str:
    """
    Sanitizes and normalizes the raw user input.
    """
    return raw_text.strip().lower()


def generate_response(user_input: str) -> str:
    """
    Processes the user's input using if-else logic
    and returns the appropriate chatbot response.
    """

    # Exit commands
    if user_input in ["exit", "quit", "terminate", "bye"]:
        return "TERMINATE_SIGNAL"

    # Greeting intents
    elif user_input in ["hello", "hi", "hey", "greetings", "initialize"]:
        return "DecodeBot initialized. Welcome to the team! How may I assist you?"

    # Project-specific intents
    elif user_input == "what is project 1?":
        return ("Project 1 focuses on building a foundation in Control Flow "
                "and Logic through a Rule-Based AI Chatbot.")

    elif user_input == "what are the core skills required?":
        return ("The core skills required are control flow, decision-making "
                "logic, and basic AI concepts.")

    elif user_input == "explain the ipo model":
        return ("The IPO (Input-Process-Output) model explains how a system "
                "takes input, processes it, and produces the desired output.")

    # Unknown input
    else:
        return (
            "Sorry, I didn't understand that.\n"
            "You can try one of these commands:\n"
            "- hello\n"
            "- what is project 1?\n"
            "- what are the core skills required?\n"
            "- explain the ipo model\n"
            "- exit"
        )


def execute_chatbot() -> None:
    """
    Runs the chatbot in a continuous loop until the user exits.
    """

    print("=" * 55)
    print("      DecodeLabs Rule-Based AI Chatbot")
    print("=" * 55)
    print("Available Commands:")
    print("- hello")
    print("- what is project 1?")
    print("- what are the core skills required?")
    print("- explain the ipo model")
    print("- exit")
    print("=" * 55)

    while True:
        try:
            # Input
            raw_input = input("\nUSER INPUT > ")

            # Process
            clean_input = sanitize_input(raw_input)
            response = generate_response(clean_input)

            # Output
            if response == "TERMINATE_SIGNAL":
                print("\nSYSTEM OUTPUT > Thank you for using DecodeBot. Goodbye!")
                sys.exit(0)

            print(f"\nSYSTEM OUTPUT > {response}")

        except KeyboardInterrupt:
            print("\n\nSYSTEM OUTPUT > Process interrupted by user. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    execute_chatbot()