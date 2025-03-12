my_list = []
count_dict = {}
def ask():
    num_input = input("Enter a number: ")
    if num_input.isdigit():
        num_input = int(num_input)
        my_list.append(num_input)
        if num_input in count_dict:
            count_dict[num_input] += 1
        else:
            count_dict[num_input] = 1
        max_duplicates = max(count_dict.values())