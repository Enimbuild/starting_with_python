'''Creating Variables

- Python has no command for declaring a variable
- In order to create a variable, we have to *assign* a value to it

for example:

c = "oranges" ,means we have assigned the value of oranges to the letter c.'''

c = "oranges"
d = 5
a = 'Hotel'
b = 'breakfast'

print(a,b)
print(f"You can have a {b} in a {a} in the morning")

print(c)
print(f"the type of c is :",type(c))            # we can also print the type of variable (Casting)
print(d)
print(f"the type of d is :",type(d))
print(f"I need {d} {c}!")

# Casting

c = str("oranges")
d = int(5)

print(d,c)

# Strings

y = "Hello Python World, are you learning about data types?"

print(y)
print("is y an int? :",isinstance(y, str))
