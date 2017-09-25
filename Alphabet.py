x = int(input("Enter a number: "))
i = 0

if not 0 < x <= 26:
    print("Invalid input, program terminates.")
else :
    while i <= 26:
        while i < x:
           print(chr(ord('A')+i))    
           i += 1 
