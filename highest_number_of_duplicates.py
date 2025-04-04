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
        most_duplicated_num = [num for num, count in count_dict.items() if count == max_duplicates]
        print(f"The number(s) with the most duplicates: {most_duplicated_num} with {max_duplicates} duplicates")
        ask()
    else:
        exit()

ask()