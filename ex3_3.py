x = float(input(''))
rnew = x

while True:
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if(diff < 0):
        diff = -diff
    if diff <= 1.0E-6:
        break
