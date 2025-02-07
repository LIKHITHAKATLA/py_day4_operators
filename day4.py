# ARTHEMATIC OPERATORS
print("ARTHEMATIC OPERATORS")
a = 2
b = 3
print(a +  b)       # 5
print(a - b)        # -1
print(a * b)        # 6
print(a / b)        # 0.66666
print(a % b)        # 2
print(a // b)       # 0
print(a ** b)       # 8


# ASSIGNMENT OPERATOR
print("ASSIGNMENT OPERATOR")
a,b = 2,7
a+=b
print(a)  #9

a,b = 2,7
a-=b
print(a)   #-5

a,b = 2,7
a*=b
print(a)   #14

a,b = 2,7
a/=b
print(a)   #0.2857142857142857

a,b = 2,7
a%=b
print(a)  #2

a,b = 2,7
a//=b
print(a)   #0

a,b = 2,7
a**=b
print(a)   #128

print("LOGICAL OPERATOR")
#LOGICAL OPERATOR
print("AND")
print(2 and 3)           #3
print(3 and 2)           #2
print(3 > 2 and 2 < 1)   # False
print(3 > 2 and 6 > 5 and 2 < 8)    # True


print("or")
print(2 or 3)            #2
print(3 or 1)            #3
print(2 < 3 or 5 < 6)   #True

print("not")
a = False
print(not a)             #True


print("RELATIONAL OPERATORS")
a = 10
b = 13
c = 13
print(a >  b)       # False
print(a < b)        # True
print(a >= c)        # False
print(a <= c)        # True

print("BITWISE OPERATOR")
a = 2
b = 5
print(a &  b)       # 0
print(a | b)        # 7
print(a ^ b)        # 7
print( ~a )         # -3
print(a << 2)       # 8
print(b >> 2)       # 1

