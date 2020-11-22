# ---------------------------------------------------------
# ------------  Assignment For Lessons 19 - 20  -----------
# ---------------------------------------------------------

# [01] Write Down All Types Of Integer
print(type(1))
print(type(-1))

# [02] Get The Imaginary Part For The Complex Number "1+2j"
complexNumber = 1+2j
print(type(complexNumber))
print(f'Imaginary Part is {complexNumber.imag}')

# [03] Get The Real Part For The Complex Number "1+2j"
print(f'Real Part is {complexNumber.real}')

# [04] Convert Number 10 To Floating Point Number With 10 Number After Decimal
print(float(10))

# [05] Convert Floating Number 159.650 To Integer
print(int(159.650))

# [06] Function
# --- Create Function Accepts Three Parameters ( num1, num2, operation )
# --- Check if Given Arguments Is Integers
# --- Return The Results of Addition if Third Parameter is ( add )
# --- Return The Results of Multiplication if Third Parameter is ( multiply )


def myFunction(num1, num2, operation):
    if (isinstance(num1, int)) == True and (isinstance(num2, int)) == True and (operation == 'add' or operation == 'multiply'):
        if operation == 'add':
            print(num1 + num2)
        elif operation == 'multiply':
            print(num1 * num2)
        else:
            print('Choose add or multiply')
    else:
        print('Your input not Integer')


myFunction(2, 4, 'add')
myFunction(2, 4, 'multiply')
# [07] Get The Same Result Without Use The Exponents 3 ** 8
print(3**8)                             # 6561
print(3 * 3 * 3 * 3 * 3 * 3 * 3 * 3)    # 6561

# [08] Whats The Different Between 21 / 2 And 21 // 2 "Write Soultion With Comment"
print(21 / 2)       # Float 10.5
print(21 // 2)      # Int   10
