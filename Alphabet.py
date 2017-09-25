a = int(input("Enter a number: "))
count = 0
loops = 0

if a <= 0 or a > 26:
    print("Invalid input, program terminates.")
else:
    while count < a:
        loops = a-(count+1)
        loop = 0
        C = ''
        while loops < a:
            Chr = (chr((65+loop)))
            loop += 1
            loops += 1
            C += Chr
        print(C)
        count += 1
