def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to AI Automation Bootcamp."


def calculate_name_length(name: str) -> int:
    return len(name)


def main():
    user_name = input("Enter your name: ")

    greeting_message = greet(user_name)
    name_length = calculate_name_length(user_name)

    print(greeting_message)
    print(f"Your name has {name_length} characters.")


if __name__ == "__main__":
    main()