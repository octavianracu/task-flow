birth_year = int(input("Year of birth: "))
current_year = 2023
age = current_year - birth_year

if age > 0 and age <= 3:
    print ("Baby")
elif age >= 4 and age <= 9:
    print("Kid")
elif age >= 10 and age <= 15:
    print("Teen")
elif age >= 16 and age <= 18:
    print("Young")
elif age >= 19 and age <= 50:
    print("Adult")
else:
    print ("Old")