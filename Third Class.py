# Date: March 9,2022

# Personal Presentation, last class review
# Variable Initialization
place = "Costa Rica"
name = "Camila"
color = "pink"
hobby = "programming in Python"
age = 16
print("My name is " + name.capitalize() + ", I am " + str(age) +
      " years old," + " I live in " + place.title() + ", my favorite color is " + color.lower() +
      "and what I love the most is " + hobby.upper() + ".")

# Methods for string analysis with boolean return
a = "Hi"
b = "hello"
c = "PINK"
d = "text"
e = "1234"

# True Values
print(a.istitle())
print(b.islower())
print(c.isupper())
print(d.isalpha())
print(e.isnumeric())
# Different Values
print(e.istitle())
print(d.islower())
print(a.isupper())
print(b.isalpha())
print(d.isnumeric())

# .istitle() turns True if first letter is capitalized and the rest is in lowercase else, turns False
# .islower() turns True if everything is in lowercase else, turns False
# .isupper() turns True if everything is in uppercase else, turns False
# .isalpha() turns True if there are only letters in the string, else, turns False
# .isnumeric() turns True if there are only numbers in the string, else, turns False
