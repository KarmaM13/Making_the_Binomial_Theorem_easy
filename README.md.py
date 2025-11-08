# Making_the_Binomial_Theorem_easy
#This is a Python code used to make the difficult formulas easy.


a = input("Enter what 'a' means: ")
b = input("Enter what 'b' means: ")


try:
    a = float(a)
except ValueError:
    print("Invalid input for 'a'. Please enter a numeric value.")
    exit()

try:
    b = float(b)
except ValueError:
    print("Invalid input for 'b'. Please enter a numeric value.")
    exit()

# Calculation
result_1 = a**2 + 2*a*b + b**2      # (a+b)^2
result_2 = a**2 - 2*a*b + b**2      # (a-b)^2
result_3 = a**3 + 3*a**2*b + 3*a*b**2 + b**3  # (a+b)^3
result_4 = a**3 - 3*a**2*b + 3*a*b**2 - b**3  # (a-b)^3

# Answers
print(f"(a + b)^2 = {result_1:.2f}")
print(f"(a - b)^2 = {result_2:.2f}")
print(f"(a + b)^3 = {result_3:.2f}")
print(f"(a - b)^3 = {result_4:.2f}")


