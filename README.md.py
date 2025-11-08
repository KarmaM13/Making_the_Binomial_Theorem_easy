# Making_the_Binomial_Theorem_easy
#This is a Python code used to make the difficult formulas easy.

a = float (input("Enter what 'a' means: "))
b = float (input("Enter what 'b' means: "))


result_1 = a**2 + 2*a*b + b**2
result_2 = a**2 - 2*a*b + b**2
result_3 = a**3 + 3*a**2*b + 3*a*b**2 + b**3
result_4 = a**3 - 3*a**2*b + 3*a*b**2 - b**3


print(f"(a+b)^2 = {result_1:.2f}")
print(f"(a-b)^2 = {result_2:.2f}")
print(f"(a+b)^3 = {result_3:.2f}")
print(f"(a-b)^3 = {result_4:.2f}")

