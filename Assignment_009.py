# ---------------------------------------------------------
# ------------  Assignment For Lessons 41 - 46  -----------
# ---------------------------------------------------------

# https: // elzero.org/python-assignments-lesson-from-41-to-46/

# [01]
num1 = int(input('Enter The First Number: ').strip())
num2 = int(input('Enter The Second Number: ').strip())
operation = input("Choose The Operator '+' or '-' or '*' or '/' or '%': ").strip()

if operation == '+':
  print(num1 + num2)

elif operation == '-':
  print(num1 - num2)

elif operation == '*':
  print(num1 * num2)

elif operation == '/':
  print(num1 / num2)

elif operation == '%':
  print(num1 % num2)

else:
  print('Please Choose Right Opreation')

print("\n##### End Of Assignment 1 #####\n")

# [02]
age = 17
print('App Is Suitable For You') if age > 16 else print('App Is Not Suitable For You')

print("\n##### End Of Assignment 2 #####\n")

# [03]
your_age = int(input('Pleasel Write Your Age: ').strip())
months = your_age * 12
weeks = months * 4
days = your_age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if your_age <= 100 and your_age >= 10:
  print(f'Your Age In Months Is {months} Months')
  print(f'Your Age In Weeks Is {weeks} Weeks')
  # print(f'You have {your_age} years old and You live \n{months} Months \n{weeks} Weeks \n{days} Days \n{hours} Hours \n{minutes} Minutes \n{seconds:3,} Seconds')
else:
  print('You are Out of Range')

print("\n##### End Of Assignment 3 #####\n")

# [04]
country = input('Input Your Country: ').strip().capitalize()
countries = ['Egypt', 'Palestine', 'Syria', 'Yemen', 'KSA', 'USA', 'Bahrain', 'England']
price = 100
discount = 30

if country in countries:
  print(f'Your Country Eligible For Discount And The Price After Discount Is ${price - discount}')
else:
  print(f'Your Country Not Eligible For Discount And The Price Is ${price}')

print("\n##### End Of Assignment 4 #####\n")
