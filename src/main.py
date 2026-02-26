def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to AI Automation Bootcamp."


def main():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)


if __name__ == "__main__":
    main()