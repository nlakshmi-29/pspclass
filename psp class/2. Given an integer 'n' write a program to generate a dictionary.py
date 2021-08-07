n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

'''1. User must enter a number and store it in a variable.
2. A dictionary is declared and initialized to values using dictionary comprehension.
3. The numbers between 1 to n are kept as keys while the squares of the numbers are made their values.
4. The final dictionary is printed.'''
