with open(r"C:\\Users\\Махарон\\Downloads\\lab.txt") as f:
    with open(r"C:\\Users\\Махарон\\Downloads\\lab1.txt", "w") as f1:
        for line in f:
            f1.write(line)