my_list = []
def ask():
    num_input = input("Enter a number: ")
    if num_input.isdigit() == True:
        num_input = int(num_input)
        my_list.append(num_input)
        average = sum(my_list)/len(my_list)
        print(average)
        ask()