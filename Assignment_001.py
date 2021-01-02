# ---------------------------------------------------------
# ------------  Assignment For Lessons 1 - 10  ------------
# ---------------------------------------------------------

# ---------------------------------------------------------
# ---- Write A Multiple Line Comment Describe The Page ----
# ---------------------------------------------------------

# [01] Write A Multiple Line Comment Describe The Page
# For What you are using the comments?!
# -------------------------------
# Informations About File
# License
# Who Created The File
# When The File Created
# Why The File Created
# Write Beside The Programming Line
# Write Before The Programming Line
# Prevent Code From Run
# -------------------------------
# Keyboard Shortcut => ctrl + /

print("\n##### End Of Assignment 1 #####\n")

# [02] Create 3 Variables ( Name => String, Age => Number, Country => String )

####################################################
###### There are 3 ways to type the variables ######
# --------------------------------------------------
# ------- Every single variable in one line --------
name = 'Mohammad'       # String
age = '38'              # String
country = 'Egypt'     # String
# --------------------------------------------------
####################################################
# --------------------------------------------------
# --------- In one line using semicolon ; ----------
# Name = 'Mohammad' ; Age = 33 ; Country = 'Egypt'
# --------------------------------------------------
####################################################
# --------------------------------------------------
# ----------- Multi Assign using comma , -----------
name, age,  country = 'Mohammad', '38', 'Egypt'
# Name = 'Mohammad' , Age = 33 , Country = 'Egypt
# --------------------------------------------------
print("\n##### End Of Assignment 2 #####\n")
# [03] Print To The Console 3 Lines Contains Created Variables Type
print("Name: " + name)
print("Age: " + age)
print("Country: " + country)

print("\n##### End Of Assignment 3 #####\n")


# [04] Concatenate & Print "Hello {Name Var} Your Age Is {Age Var} & Country Is {Country Var}"
# Hello Mohammad Your Age is 33 & Country Is Egypt
print(f'Hello {name} Your Age is {age} & Country Is {country}')

print("\n##### End Of Assignment 4 #####\n")


# [05] Write Single Line Comment Before Every Variable Describe The Data Type

print(type(name))         # <class 'str'> String
print(type(age))          # <class 'int'> Integer
print(type(country))      # <class 'str'> String

print("\n##### End Of Assignment 5 #####\n")
