# A very simple diffie-hellman encryption/decryption method

# Variables assignment
x = int(input("Value for Alice is: "))
y = int(input("Value for Bob is: "))
g = int(input("Value for g is: "))
n = int(input("Enter a prime number: "))

# Begin

print("Value of g is: ", g )
print("Prime number is: ", n )
print("Alice secret is: ", x )
print("Bob's secret is: ", y)

# Alice - g**x % n

a = g**x % n

# Bob - g**y % n

b = g**y % n

# Time to send em and flip em

# Alice - b**x % n

d = b**x % n

# Bob - a**y % n

e = a**y % n

# print it. prove it. cheer. be happy.

print("The secret is... ", d )
print("Just to prove its right... ", e )

