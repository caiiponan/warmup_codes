my_list = []

def ask():
    num_input = int(input("Enter a number: "))
    if type(num_input) == int:
        my_list.append(num_input)
        print(f"The smallest number so far is: {min(my_list)}")
        ask()
    else:
        exit
ask()