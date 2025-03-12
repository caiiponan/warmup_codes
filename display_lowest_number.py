my_list = []

def ask():
    num_input = input("Enter a number: ")
    if num_input.isdigit() == True:
        if num_input not in my_list:
            my_list.append(num_input)
            print(f"The smalles number so far is: {min(my_list)}")
            ask()
    else:
        exit
ask()