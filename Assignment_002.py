# ---------------------------------------------------------
# ------------  Assignment For Lessons 11 - 18  -----------
# ---------------------------------------------------------


# [01] Create 3 Variables Name, Age, Country
name, age, country = 'Osama', 38, 'Egypt'
print(f'\"Hello \'{name}\', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}')

print("\n##### End Of Assignment 1 #####\n")

# [02] Print The Same Previous Text But in 3 Lines Not Single Line
print(f'Hello \'{name}\' \nHow You Doing \nYour Age Is {age} + \n And Your Country Is: {country}')  # Hello Mohammad

print("\n##### End Of Assignment 2 #####\n")

# [03] Get The Letter "l" From Elzero
e = 'Elzero'
print(e[1])  # l

# Get The Letter "z" From Elzero
print(e[2])  # z

# Get The Letter "o" From Elzero
print(e[-1])  # o

print("\n##### End Of Assignment 3 #####\n")


# [04] Get The Letters "lze" From Elzero
print(e[1:4])  # lze

# Get The Letters "Ezr" From Elzero
print(e[::2])  # Ezr

# Get The Letters "rzE" From Elzero
print(e[-2::-2])  # rzE

print("\n##### End Of Assignment 4 #####\n")

# [05] Remove Special Character From The String "#@#@Elzero#@#@" And Return Elzero
a = "#@#@Elzero#@#@"
print(a.strip("#@"))    # Elzero
print(a.rstrip("#@"))   # #@#@Elzero
print(a.lstrip("#@"))   # Elzero#@#@

print("\n##### End Of Assignment 5 #####\n")

# [06] Make A Function Add Zeros Before Given Number And Return Number Not Exceed 4 Width Example "0010", "1800"
num = "9"
print(num.zfill(4))

num = "15"
print(num.zfill(4))

num = "130"
print(num.zfill(4))

num = "950"
print(num.zfill(4))

num = "1500"
print(num.zfill(4))

print("\n##### End Of Assignment 6 #####\n")

# [07]
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "#"))
print(name_two.rjust(20, "#"))

print("\n##### End Of Assignment 7 #####\n")

# [08] Convert This String "OSamA" To "osAMa"
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())  # osAMa
print(name_two.swapcase())  # OSAma

print("\n##### End Of Assignment 8 #####\n")

# [09] Count How Much Word Love in This String "I Love Python And Although Love Elzero Web School"
f = "I Love Python And Although Love Elzero Web School"
print(f.count("Love"))  # 2

print("\n##### End Of Assignment 9 #####\n")

# [10] Find The Index Of The Letter "z" in String "Elzero"
print(e.index('z'))  # 2

print("\n##### End Of Assignment 10 #####\n")

# [11] Replace The Word <3 With Love Letter One Time in This String => "I <3 Python And Although <3 Elzero Web School"
p = "I <3 Python And Although <3 Elzero Web School"
# I Love Python And Although <3 Elzero Web School
print(p.replace("<3", "Love", 1))

print("\n##### End Of Assignment 11 #####\n")


# [12] Replace All The Words <3 With Love Letter in This String => "I <3 Python And Although <3 Elzero Web School"
# I Love Python And Although Love Elzero Web School
print(p.replace("<3", "Love", 2))

print("\n##### End Of Assignment 12 #####\n")

# [17] Format The Variables Created in Step One With The New Way f""
# Hello Mohammad How You Doing Your Age Is 33
print(f'My Name Is {name}, And My Age Is {age}, And My Country Is {country}')

print("\n##### End Of Assignment 13 #####\n")
