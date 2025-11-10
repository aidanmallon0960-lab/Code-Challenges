while True:
    num = input("Please enter a number or press q to quit: ").strip().lower()
    if num == "q":
        break
    else:
        try:
            num = int(num)
            num = str(num)
            char_one = num[0]
            char_two = num[-1]
            if char_one == char_two:
                print(f"{num} is a palindrome number")
            else:
                print(f"{num} is not a palindrom number")
        except ValueError:
            print("Please enter a valid number")
    