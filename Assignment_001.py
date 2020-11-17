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

####################################################

# [02] Create 3 Variables ( Name => String, Age => Number, Country => String )

####################################################
###### There are 3 ways to type the variables ######
# --------------------------------------------------
# ------- Every single variable in one line --------
Name = 'Mohammad'       # String
Age = 33                # Integer
Country = 'Egypt'       # String
# --------------------------------------------------
####################################################
# --------------------------------------------------
# --------- In one line using semicolon ; ----------
# Name = 'Mohammad' ; Age = 33 ; Country = 'Egypt'
# --------------------------------------------------
####################################################
# --------------------------------------------------
# ----------- Multi Assign using comma , -----------
Name, Age,  Country = 'Mohammad', 33, 'Egypt'
# Name = 'Mohammad' , Age = 33 , Country = 'Egypt
# --------------------------------------------------

# [03] Print To The Console 3 Lines Contains Created Variables Type
# [04] Write Single Line Comment Before Every Variable Describe The Data Type

print(type(Name))         # <class 'str'> String
print(type(Age))          # <class 'int'> Integer
print(type(Country))      # <class 'str'> String

# [05] Print A Separator Contains 20 # Character
print('#' * 20)     # Output ####################

# [06] Concatenate & Print "Hello {Name Var} Your Age Is {Age Var} & Country Is {Country Var}"
# Hello Mohammad Your Age is 33 & Country Is Egypt
print(f'Hello {Name} Your Age is {Age} & Country Is {Country}')
