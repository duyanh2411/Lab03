print('task_1 :')
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)
print("\n")        

print('task_2 :')
num = 145
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)
print("\n")

print('task_3 :')
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)
