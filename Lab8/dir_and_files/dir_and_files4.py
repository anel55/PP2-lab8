def file_lengthy(file):
    with open(file) as f:
        lines = len(f.readlines())
        return lines

file = r'C:\\Users\\Махарон\\Downloads\\lab.txt'
print("Number of lines in the file: ",file_lengthy(file))
