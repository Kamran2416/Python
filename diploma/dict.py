#dictionary are always in key and value
#key should be followed by one data type
#values can be anything
#if the key is not avalible then it will add th elemnt if it is there than it will change 
 

student ={1: "Kamran",2: "Hassan",3:"Irqan",4:"Hamza",5:"Aiman"}

print(student)
print(student[1])

student[4]="Nikhil"
print(student)

student[6]="Hamza"
print(student)

#for s in student:
#   print(s,student[s])

for k,v in student.items():
    print(k,v)