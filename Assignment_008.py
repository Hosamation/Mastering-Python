# ---------------------------------------------------------
# ------------  Assignment For Lessons 33 - 37  -----------
# ---------------------------------------------------------

# https: // elzero.org/python-assignments-lesson-from-38-to-40/

# [01]
name = input('What\'s Is Your First Name? ').strip().capitalize()
print(f'Hello {name}, Happy To See You Here.')

print("\n##### End Of Assignment 1 #####\n")

# [02]
age = int(input('What\'s Is Your Age? '))
print(type(age))  # <class 'int'>

if age <= 16:
  print('Hello Your Age Is Under 16, Some Articles Is Not Suitable For You')
else:
  print(f'Hello Your Age Is {age}, All Articles Is Suitable For You')

print("\n##### End Of Assignment 2 #####\n")

# [03]
first_name = input('What\'s Is Your First Name? ').strip().capitalize()
second_name = input('What\'s Is Your Second Name? ').strip().capitalize()
print(f'Hello {first_name} {second_name:.1s}.')

print("\n##### End Of Assignment 3 #####\n")

# [04]
email = input('What\'s Is Your Email? ').strip().lower()
user_name = email[:email.index('@')].capitalize()
domain = email[email.index('@') + 1: email.index('.')]
level_domain = email[email.index('.') + 1:]

print(f'Your Name Is {user_name} \nEmail Service Provider Is {domain} \nTop Level Domain Is {level_domain}')

print("\n##### End Of Assignment 4 #####\n")
