list = [1,2,3,4,5]
print(list)
print(list[3])
another_list = ["Gaurav Kapoor","OpenSense Labs",23,'M']
print(another_list)
print(list+another_list)
print("Gaurav Kapoor" in another_list)
list.append(6)
print(list)
another_list.insert(1,"Software Developer")
print(another_list)
numbered_list = range(10)
print(numbered_list)
numbered_list = range(1,11)
print(numbered_list)
numbered_list = range(0,11,2)
print(numbered_list)
for x in another_list:
  print(x)
i = 5
j = 0
while i < 25:
  j = j + i
  i = i + 1
print(j)
