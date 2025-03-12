my_list = []
count_dict = {}
def ask():
    num_input = input("Enter a number: ")
    if num_input.isdigit():
        num_input = int(num_input)
        my_list.append(num_input)
        