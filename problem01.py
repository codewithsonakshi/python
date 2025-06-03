a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
d = int(input("enter fourth number : "))


if a>b and a>c and a>d:
    greatest = a
elif b>c and b>d:
    greatest = b
elif c>d:
    greatest = c
else:
    greatest = d

print ("THe greatest number is:",greatest)


