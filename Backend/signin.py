import csv
import sys

try:
    name = str(sys.argv[1])
    passd = str(sys.argv[2])

    f = open("users.csv", "r")
    data = csv.reader(f)
    for i in data:
        if (len(i) == 0):
            continue

        if (str(i[0]) == name):
            if (str(i[2]) == passd):
                print(0)
                break
            else:
                print(1)
                break
    else:
        print(2)
except Exception as e:
    print(e)

# with open('users.csv', 'r') as file:
#     csvFile = csv.reader(file)
#     for i in csvFile:
#         print(i[0])
#         # if (str(i[0]) == name):
#         #     if (str(i[2]) == passd):
#         #         print(0)
#         #     else:
#         #         print(1)
#     # print(2)