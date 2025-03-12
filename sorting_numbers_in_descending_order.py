my_list = []

def ask():
    num_input = (input("Enter a number: "))
    if num_input.isdigit() == True:
        num_input = int(num_input)
        if num_input not in my_list:
            my_list.append(num_input)
            my_list.sort(reverse=True)
            print(my_list)
            ask()
        else:
            ask()
    