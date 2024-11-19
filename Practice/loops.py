myName = "Dhamari"


for char in myName:
    print(char)

myFriends = ["Kari", "Malayki","Emile","Jason"]

for friends in myFriends:
    print(friends)

grades = [55,24,24,34,90]
print("Grades before cruve:", grades)

## Each grade in grades is increased by 25
for count, grade in enumerate(grades):
    grades[count] = grade + 25

print("Grades after curve:", grades)