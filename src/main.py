def add_numbers(a:int,b:int)->int:
    print("Function started")
    result = a + b
    print("Function ended")
    return result

def main():

    print("Main function started")
    num1 = 10
    num2 = 20
    Total = add_numbers(num1, num2)
    print("Total:", Total)
    print("Main function ended")
if __name__ == "__main__":
    main()