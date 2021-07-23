"""
User inputs a number and the computer shows
the hailstone sequence of that number.
"""

def main():
    steps = 0
    user_number = int(input("Enter a number: "))
    while user_number != 1:
        if user_number % 2 == 0:
            print(str(user_number), "is even, so I take half:", str(user_number // 2))
            user_number = user_number // 2
        else:
            print(str(user_number), "is odd, so I make 3n + 1:", str(user_number * 3 + 1))
            user_number = user_number * 3 + 1
        steps += 1
    print("The process took", str(steps), "steps to reach 1")

if __name__ == "__main__":
    main()