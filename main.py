FirstName = "[First Name]        "
LastName = "[Last Name]         "
Location = "[Location]          "
Job = "[Job]               "
Pet = "[Pet]"
header = FirstName + LastName + Location + Job + Pet

final_list = []
letter_count = 0
result = ""

while True:
    try:
        lines = int(input("How many lines do you want ? > "))
        if lines > 0 and lines <= 50:
            break
        else:
            print("Too much case")

    except ValueError:
        print("Invalid value, please enter an integer")

for line in range(lines):
    while True:
        f_name = input("Enter the first name of the person > ")
        for letter in f_name:
            letter_count += 1
        if letter_count > 0 and letter_count <= 20:
            break
        else:
            print("Name too long or too short")
            letter_count = 0
    letter_count = 0
    while True:
        l_name = input("Enter the last name of the person > ")
        for letter in l_name:
            letter_count += 1
        if letter_count > 0 and letter_count <= 20:
            break
        else:
            print("Name too long or too short")
            letter_count = 0
    letter_count = 0
    while True:
        loc = input("Enter the location of the person > ")
        for letter in loc:
            letter_count += 1
        if letter_count > 0 and letter_count <= 20:
            break
        else:
            print("Name too long or too short")
            letter_count = 0
    letter_count = 0
    while True:
        job = input("Enter the job(s) of the person > ")
        for letter in job:
            letter_count += 1
        if letter_count > 0 and letter_count <= 20:
            break
        else:
            print("Name too long or too short")
            letter_count = 0
    letter_count = 0
    while True:
        pet = input("Enter the pet(s) of the person > ")
        for letter in pet:
            letter_count += 1
        if letter_count > 0 and letter_count <= 20:
            break
        else:
            print("Name too long or too short")
            letter_count = 0
    letter_count = 0
    final_list.append([f_name, l_name, loc, job, pet])

print("")
print(header)
for list in final_list:
    if result != "":
        print(result)
    result = ""

    for item in list:

        for letter in item:

            letter_count += 1

        result += item + " " * (20 - letter_count)
        letter_count = 0
print(result)
