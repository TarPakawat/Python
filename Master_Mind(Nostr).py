target = int(input("Enter a target (4-digit integer): ")) 
guess = int(input("Enter your guess (4-digit integer): ")) 
  
pos = 0 
digit = 0 
pCount = 1 
while pCount <= 1000: 
    targetDigit = target // pCount % 10 
    dCount = 1 
    while dCount <= 1000: 
        if targetDigit == guess // dCount % 10: 
            digit += 1 
        dCount *= 10 
  
    if targetDigit == guess // pCount % 10: 
        pos += 1 
    pCount *= 10 
  
digit -= pos 
  
if digit == 0: 
    digitStr = "no digits correct" 
elif digit == 1: 
    digitStr = "one digit correct" 
elif digit == 2: 
    digitStr = "two digits correct" 
elif digit == 3: 
    digitStr = "three digits correct" 
else: 
    digitStr = "four digits correct" 
  
if pos == 0: 
    print("No positions correct,", digitStr) 
elif pos == 1: 
    print("One position correct,", digitStr) 
elif pos == 2: 
    print("Two positions correct,", digitStr) 
elif pos == 3: 
    print("Three positions correct,", digitStr) 
else: 
    print("Congratulations, you just mastered my mind!!")
