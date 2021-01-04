# ---------------------------------------------------------
# ------------  Assignment For Lessons 21 - 23  -----------
# ---------------------------------------------------------

# https://elzero.org/python-assignments-lesson-from-21-to-23/

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# [01]
print(friends[0])       # Osama
print(friends[-5])      # Osama
print(friends.pop(0))  # "Osama"

print(friends[-1])      # Mahmoud
print(friends[3])       # Mahmoud
print(friends.pop(-1))  # "Mahmoud"

print("\n##### End Of Assignment 1 #####\n")


# [02]
print(friends[::2])     # Osama, Sayed, Mahamoud
print(friends[1::2])    # Ahmed, Ali

print("\n##### End Of Assignment 2 #####\n")

# [03]
print(friends[1:4])     # Ahmed, Sayed, Ali
print(friends[-2::])    # Ali, Mahmoud

print("\n##### End Of Assignment 3 #####\n")

# [04]
friends[-2::] = ['Elzero', 'Elzero']   
# friends[-1] = 'Elzero'
# friends[-2] = 'Elzero'
print(friends)   # Osama, Ahmed, Sayed, Elzero, Elzero

# [05]
friends.insert(0, 'Nasser')   # Nasser, Osama, Ahmed, Sayed, Elzero, Elzero
# Nasser, Osama, Ahmed, Sayed, Elzero, Elzero, Salem
friends.append('Salem')
print(friends)

# [06]
friends.remove('Nasser')      # Osama, Ahmed, Sayed, Elzero, Elzero, Salem
# friends.remove('Osama')       # Ahmed, Sayed, Elzero, Elzero, Salem
friends.remove('Salem')       # Ahmed, Sayed, Elzero, Elzero
print(friends)

print("\n##### End Of Assignment 6 #####\n")

# [07]
friends = ["Ahmed", "Sayed"]
employees = ['Samah', 'Eman']
school = ['Ramy', 'Shady']
friends.extend(employees)     # Ahmed, Sayed, Elzero, Elzero, Samah, Eman
# Ahmed, Sayed, Elzero, Elzero, Samah, Eman, Ramy, Shady
friends.extend(school)
# Ahmed, Sayed, Samah, Eman, Ramy, Shady

print("\n##### End Of Assignment 7 #####\n")


print(friends)

# [08]
friends.sort()
# Ahmed, Elzero, Elzero, Eman, Ramy, Samah, Sayed, Shady
print(friends)
friends.sort(reverse=True)
# Shady, Sayed, Samah, Ramy, Eman, Elzero, Elzero, Ahmed
print(friends)

print("\n##### End Of Assignment 8 #####\n")


# [09]
print(len(friends))           # 6
length = friends.__len__()
print(length)                 # 6

print("\n##### End Of Assignment 9 #####\n")


[10]
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])

print("\n##### End Of Assignment 10 #####\n")
