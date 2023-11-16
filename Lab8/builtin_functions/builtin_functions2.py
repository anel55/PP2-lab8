def case_test(text):
    upper = 0
    lower = 0
    for x in text:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
        else:
            pass
    length = len(text)
    print(f"General length of string: {length} \nUpper-case: {upper} \nLower-case: {lower}")

string = input()
case_test(string)
