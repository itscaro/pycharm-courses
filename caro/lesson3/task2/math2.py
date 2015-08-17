def lookandsay(n):
    Given the current number, say the next number


until = int(input("How many numbers in the look-and-see sequence to print out: "))

currentNb = None
for i in range(1, until): # Here we have only (until - 1) loop starting from 1
    if currentNb == None:
        currentNb = 1
        print(currentNb)

    currentNb = lookandsay(currentNb)
    print(currentNb)