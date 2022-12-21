from csv import writer
import sys

nm = sys.argv[1]
dob = sys.argv[2]
passd = sys.argv[3]

List = [nm, dob, passd]
 
with open('users.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close()

print("Account created successfully")