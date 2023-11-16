from time import sleep
def square_root(sleeptime, number):
    sleeptime = sleeptime/1000
    sleep(sleeptime)
    number = pow(number, 1/2)
    return number

time = int(input("Enter a time in ms:"))
number = int(input("Enter a number:"))
print(f"Square root of {number} after {time} miliseconds is {square_root(time, number)}")