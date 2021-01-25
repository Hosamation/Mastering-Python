# ---------------------------------------------------------
# ------------  Assignment For Lessons 33 - 37  -----------
# ---------------------------------------------------------

#  https://elzero.org/python-assignments-lesson-from-33-to-37/

# [01]
print('\nTrue Values \n')

print(bool('Hosam'))      # True
print(bool(100))          # True
print(bool(1.50))         # True
print(bool(True))         # True

print('\nFalse Values \n')

print(bool(''))           # False
print(bool(0))            # False
print(bool(False))        # False
print(bool(None))         # False
# All Empty Values = False

print("\n##### End Of Assignment 1 #####\n")

# [02]
html = 80
css = 60
javaScript = 70

print(html > 50 and css > 50 and javaScript > 50) # True

print("\n##### End Of Assignment 2 #####\n")

# [03]
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)   # True

print(num > num_one and num > num_two)  # False

print("\n##### End Of Assignment 3 #####\n")

# [04]
num_one = 10
num_two = 20
result = num_one + num_two

print(result) # 30

print(result ** 3) # 27000
print((result ** 3) % 26000) # 1000
print(((result ** 3) % 26000) / 5) #200.0
print(type(str(((result ** 3) % 26000) / 5)))  # c<class 'str'>