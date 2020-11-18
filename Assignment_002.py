# ---------------------------------------------------------
# ------------  Assignment For Lessons 11 - 18  -----------
# ---------------------------------------------------------


# [01] Create 3 Variables Name, Age, Country
name, age, country = 'Mohammad', 33, 'Egypt'

# [02] Print This Text To The Console => "Hello 'Variable Name', How You Doing \ """ Your Age Is "Variable Age""
print(f'Hello {name} How You Doing Your Age Is {age}')  # Hello Mohammad How You Doing Your Age Is 33

# [03] Print The Same Previous Text But in 3 Lines Not Single Line
print(f'Hello {name} \nHow You Doing \nYour Age Is {age}')  # Hello Mohammad
# How You Doing
# Your Age Is 33


# [04] Get The Letter "l" From Elzero
e = 'Elzero'
print(e[1])  # l

# [05] Get The Letter "o" From Elzero
print(e[-1])  # o

# [06] Get The Letters "lze" From Elzero
print(e[1:4])  # lze

# [07] Get The Letters "Ezr" From Elzero
print(e[::2])  # Ezr

# [08] Get The Letters "rzE" From Elzero
print(e[-2::-2])  # rzE

# [09] Remove Special Character From The String "#@#@Elzero#@#@" And Return Elzero
a = "#@#@Elzero#@#@"
print(a.strip("#@"))    # Elzero
print(a.rstrip("#@"))   # #@#@Elzero
print(a.lstrip("#@"))   # Elzero#@#@

# [10] Make A Function Add Zeros Before Given Number And Return Number Not Exceed 4 Width Example "0010", "1800"
c = '10'
print(c.zfill(4))  # 0010

# [12] Convert This String "OSamA" To "osAMa"
g = 'OSamA'
print(g.swapcase())  # osAMa

# [13] Count How Much Word Love in This String "I Love Python And Although Love Elzero Web School"
f = "I Love Python And Although Love Elzero Web School"
print(f.count("Love"))  # 2

# [14] Find The Index Of The Letter "z" in String "Elzero"
print(e.index('z'))  # 2

# [15] Replace The Word <3 With Love Letter One Time in This String => "I <3 Python And Although <3 Elzero Web School"
p = "I <3 Python And Although <3 Elzero Web School"
# I Love Python And Although <3 Elzero Web School
print(p.replace("<3", "Love", 1))

# [16] Replace All The Words <3 With Love Letter in This String => "I <3 Python And Although <3 Elzero Web School"
# I Love Python And Although Love Elzero Web School
print(p.replace("<3", "Love", 2))

# [17] Format The Variables Created in Step One With The New Way f""
# Hello Mohammad How You Doing Your Age Is 33
print(f'Hello {name} How You Doing Your Age Is {age}')
