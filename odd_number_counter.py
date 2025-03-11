first_num = int(input("First number: "))
second_num = int(input("Second number: "))
third_num = int(input("Third number: "))
fourth_num = int(input("Fourth number: "))
fifth_num = int(input("Fifth number: "))
sixth_num = int(input("Sixth number: "))
seventh_num = int(input("Seventh number: "))
eighth_num = int(input("Eight number: "))
ninth_num = int(input("Ninth number: "))
tenth_num = int(input("Tenth number: "))
count = 0
list = [first_num, second_num, third_num, fourth_num, fifth_num, sixth_num, seventh_num, eighth_num, ninth_num, tenth_num]
for i in list:
    while i % 2 != 0:
        count += 1
        break
print(f"The number of odd numbers in the given are: {count}.")