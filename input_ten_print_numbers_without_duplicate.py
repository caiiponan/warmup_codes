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
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)