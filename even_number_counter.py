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
list = [first, sec, third, fourth, fifth , sixth, seventh, eighth, ninth, tenth]
count = 0
for i in list:
    while i % 2 == 0:
        count += 1
        break
print("The number of even numbers are:", count)