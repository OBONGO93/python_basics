# Dictionary {}
# List []
# Turple ()
student = {"name":"jane sarah","id": 1234,"age":21, "gender": "F"}
print(student["name"]) #key
print(student)
student["weight"] = 61
print(student)

#set - a set does not allow one value to repeat.will make sure only one existance per item

people = {"jane", "Bill", "Kevo", "said", "jane"}
print(people)
people.add("willy") #add
print(len(people)) #count
people.discard("kevo") #remove
print(people)

