# ---------------------------------------------------------
# ------------  Assignment For Lessons 21 - 23  -----------
# ---------------------------------------------------------

# https://elzero.org/python-assignments-lesson-from-21-to-23/

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# [01]
print(friends[0])       # Osama
print(friends[-5])      # Osama
print(friends[-1])      # Mahmoud
print(friends[4])       # Mahmoud

# [02]
print(friends[::2])     # Osama, Sayed, Mahamoud
print(friends[1::2])    # Ahmed, Ali

# [03]
print(friends[1:4])     # Ahmed, Sayed, Ali
print(friends[-2::])    # Ali, Mahmoud

# [04]
friends[-2::] = ['Elzero', 'Elzero']    # Osama, Ahmed, Sayed, Elzero, Elzero
# friends[-1] = 'Elzero'
# friends[-2] = 'Elzero'
print(friends)

# [05]
friends.insert(0, 'Nasser')   # Nasser, Osama, Ahmed, Sayed, Elzero, Elzero
# Nasser, Osama, Ahmed, Sayed, Elzero, Elzero, Salem
friends.append('Salem')
print(friends)

# [06]
friends.remove('Nasser')      # Osama, Ahmed, Sayed, Elzero, Elzero, Salem
friends.remove('Osama')       # Ahmed, Sayed, Elzero, Elzero, Salem
friends.remove('Salem')       # Ahmed, Sayed, Elzero, Elzero
print(friends)

# [07]
employees = ['Samah', 'Eman']
school = ['Ramy', 'Shady']
friends.extend(employees)     # Ahmed, Sayed, Elzero, Elzero, Samah, Eman
# Ahmed, Sayed, Elzero, Elzero, Samah, Eman, Ramy, Shady
friends.extend(school)
# Ahmed, Sayed, Elzero, Elzero, Samah, Eman, Ramy, Shady
print(friends)

# [08]
friends.sort()
# Ahmed, Elzero, Elzero, Eman, Ramy, Samah, Sayed, Shady
print(friends)
friends.sort(reverse=True)
# Shady, Sayed, Samah, Ramy, Eman, Elzero, Elzero, Ahmed
print(friends)

# [09]
print(len(friends))           # 8
length = friends.__len__()
print(length)                 # 8

[10]
programming_languages = ['Python', ['Django', 'Flask'], 'Web', [
    'HTML', 'CSS', 'Javascribt', ], 'PHP', 'C#', 'C++']
print(programming_languages[1][0])      # Django
print(programming_languages[2])         # Web
