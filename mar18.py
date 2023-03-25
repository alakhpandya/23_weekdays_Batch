# f-string: formatted string
"""
print("Enter five integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = (a + b + c + d + e)/5

print(f"The Average of {a}, {b}, {c}, {d} and {e} is: {avg}")
"""

# string: Ordered & Immutable collection of characters

a = 	   "Today is Saturday and I am very excited for tomorrow!"
# index no: 0123456789...........................................
print(a)
print(type(a))
'''
1st - latest iPhone 		- Divyanshi	Kavyan
2nd - Dubai Trip 		- Jesal		Ritu
3rd - Local Trip 		- Ritu		Jesal
4th - Cash prize of Rs.10,000 	- Kavyan	Divyanshi
'''
c = int(input("Enter c: "))
b = int(input("Enter b: "))
print("c + b =", c+b)
print(a[6])
# name = "Yash"
print(len(a))
# Accessing through index numbers
print(a[52])
print(a[2])
# print(a[354])

# slicing
print(a[2 : 4])		# first one is included, last one is excluded