# ---------------------------------------------------------
# ------------  Assignment For Lessons 24 - 25  -----------
# ---------------------------------------------------------

# https: // elzero.org/python-assignments-lesson-from-24-to-25

# [01]
a = 'Osama',  
print(a)                      # ('Osama',)
print(type(a))                # <class 'tuple'>
print("\n##### End Of Assignment 1 #####\n")

# [02]
friends = ('Osama', 'Ahmed', 'Sayed')
# friends[0] = 'Elzero'       # 'tuple' object does not support item assignment
friends = list(friends)       # Change to list 
friends[0] = 'Elzero'
friends = tuple(friends)
print(friends)                # 'Osama', 'Ahmed', 'Sayed'
print(type(friends))          # <class 'tuple'>
print(len(friends))           # 3
print("\n##### End Of Assignment 2 #####\n")

# [03]
nums = (1, 2, 3)
letters = ('A', 'B', 'C')
nums_letters = nums + letters  
print(nums_letters)           # (1, 2, 3, 'A', 'B', 'C')
print(len(nums_letters))      # 6
print("\n##### End Of Assignment 3 #####\n")

# [04]
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)                      # 1
print(b)                      # 2
print(c)                      # 4


