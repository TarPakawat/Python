a1 = int(input("Enter a number: "))
a = (a1*2)-1
count = 0
loops = 0

if a1 <= 0 or a1 > 26:
    print("Invalid input, program terminates.")
else:
    while count < a:
        if count <= int(a/2):
            loops = a-(count+1)
        elif count > int(a/2):
            loops = count
        loop = 0
        C = ''
        while loops < a:
            Chr = (chr((65+loop)))
            loop += 1
            loops += 1
            C += Chr
        print(C)
        count += 1
