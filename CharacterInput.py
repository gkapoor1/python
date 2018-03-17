import datetime
name = raw_input("Enter your name : ")
age = input("Enter your age : ")
now = datetime.datetime.now()
print(name + ", you will turn 100 in year " + str(now.year - age + 100))
