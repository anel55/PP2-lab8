def multiply(numbers):  
    total = 1
    for x in numbers:
        total = total * x  
    return total  

print(float(multiply([1, 2.2, 3.6, 4.5, 5])))