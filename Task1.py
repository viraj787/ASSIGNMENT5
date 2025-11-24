marks = {"viraj" : "93","Alice" : "85","jay" : "63" , "nandan" : "100"}

name = input("Enter the student's name:")

if name in marks:
    print(f"{name}'s mark: {marks.get(name)}")
else:
    print("Student not found.")