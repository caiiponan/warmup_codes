my_list = []

def ask():
    num_input =(input("Enter a number: "))
    if num_input.isdigit() == True:
        if num_input not in my_list:
            print(f"{num_input} - UNIQUE")
            my_list.append(num_input)
            ask()