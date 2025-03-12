my_list: []

def ask():
    num_input = input("Enter a number: ")
    if num_input.isdigit == True:
        if num_input not in my_list:
            my_list.append(num_input)
            print(min(my_list))
    else:
        exit
ask()