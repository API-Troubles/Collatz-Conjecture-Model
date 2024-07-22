import sympy

starting_num = input("Enter starting number: ")

# Checks
try:
    starting_num = int(starting_num)
except ValueError:
    raise TypeError("You must input a valid number!") from None

if starting_num <= 2:
    raise ValueError("The number cannot be smaller or equal to 2.")

if starting_num % 2 != 0:
    raise ValueError("The number must be odd.")



def goldbach_conjecture(number):
    for addend in range(2, number // 2 + 1):  # other half is redundant and uneeded
        if sympy.isprime(addend) and sympy.isprime(number - addend): # Check if they off
            return {"result": True, "addends": [addend, number - addend]}
    return {"result": False, "addends": None}


check_conjecture = goldbach_conjecture(starting_num)

if check_conjecture["result"]:
    print(f"""
    {starting_num} obeys the goldbach conjecture! 
    {' + '.join(str(i) for i in check_conjecture['addends'])} = {starting_num}
    """)
else:
    print(f"""
    Wait... {starting_num} doesn't obey the conjecture?!11??!?!
    either I coded this wrong or you just answered a conjecture! 
    Wow such famous! Autograph pls?!?
    """)
# No seriously if you did somehow prove it false thad'd be funny
# You'll split the prize money w/ me right? Trust!
