def isKanji(x):
    return x % 3 == 0 or "3" in str(x)
    
for number in range(1,101):
    print(isKanji(number))