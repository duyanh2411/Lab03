print('task_1 :')
str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)
res = "".join([item for item in str1 if item.isdigit()])
print(res)

print("\n")

print('task_2 :')
import string
str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)
replace_char = '#'
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)
print("The strings after replacement : ", str1)

print("\n")

print('task_3 :')
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_str_list = list(filter(None, str_list))
print("After removing empty strings")
print(new_str_list)

print("\n")

print('task_4 :')
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)
sub_strings = str1.split("-")
print("Displaying each substring")
for sub in sub_strings:
    print(sub)
