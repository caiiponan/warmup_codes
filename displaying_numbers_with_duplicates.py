first = int(input("First number: "))
sec = int(input("Second number: "))
third = int(input("Third number: "))
fourth = int(input("Fourth number: "))
fifth = int(input("Fifth number: "))
sixth = int(input("Sixth number: "))
seventh = int(input("Seventh number: "))
eighth = int(input("Eighth number: "))
ninth = int(input("Ninth number: "))
tenth = int(input("Tenth number: "))

my_list = [first, sec, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]

count_dict = {}
for i in my_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
new_list = [i for i in my_list if count_dict[i] > 1]
print(new_list)