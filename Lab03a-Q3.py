print('task_1 :')
def get_middle_four_chars(str1):
    print("Original String is", str1)
    mi = int(len(str1) / 2)
    res = str1[mi - 2:mi + 2]
    print("Middle four chars are:", res)

get_middle_four_chars("Billdesctran")
get_middle_four_chars("HoSongHu")

print("\n")

print('task_2 :')
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)
    mi = int(len(s1) / 2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)
append_middle("Ault", "Kelly")
