import math
#Get input from user
# n = input("Enter n:")
# x = input("Enter x:")

#Define the original f(x) = e^x 
def original_func(x):
    return pow(math.e, x)

#Define the P_n(x) = Sum of (x^k)/(k!) at a = 0 
sum = 0
def P(n,x):
    sum = 0
    if n ==0:
        sum = 1
        return sum 
    else:

        for i in range(0,n+1):
            sum += (x**i)/math.factorial(i)
        return sum 

#Define the difference between actual value and approximate value
def difference (n, x):
    return original_func(x) - P(n,x)

def format_float(n,x) :
     result = "{:.15f}".format(difference(n, x))
     return result

print("When n = 0, x = 0.1 the difference : " + str(format_float(0, 0.1)))
print("When n = 1, x = 0.1 the difference : " + str(format_float(1, 0.1)))
print("When n = 2, x = 0.1 the difference : " + str(format_float(2, 0.1)))
print("When n = 3, x = 0.1 the difference : " + str(format_float(3, 0.1)))

print("When n = 0, x = -0.25 the difference : " + str(format_float(0, -0.25)))
print("When n = 1, x = -0.25 the difference : " + str(format_float(1, -0.25)))
print("When n = 2, x = -0.25 the difference : " + str(format_float(2, -0.25)))
print("When n = 3, x = -0.25 the difference : " + str(format_float(3, -0.25)))



