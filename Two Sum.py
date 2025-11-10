nums = []
winning_nums = []
lost = False
one = 0
two = 1
while True:
    try:
        num = int(input("Enter a number to add it to the list and enter a letter to quit: "))
        nums.append(num)
    except ValueError:
        break

while True:
    try:
        target = int(input("Enter target number: "))
        break
    except ValueError:
        print("Please enter a valid number")

print(f"nums = {nums}, target = {target}")

nums_length = len(nums) - 1

while True:
    try:
        target_check = nums[one] + nums[two]
    except IndexError:
        lost = True
        break
    if target_check == target:
        if one == two:
            lost = True
            break
        else:
            winning_nums.append(one)
            winning_nums.append(two)
            break
    elif target_check != target and two != nums_length:
        two += 1
    elif target_check != target and two == nums_length:
        two = 1
        one += 1

if lost == True:
    print("There were no numbers adding up to the target number.")
else:
    print(winning_nums)