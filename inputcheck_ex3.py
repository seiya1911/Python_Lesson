while True:
    x = input('正の数値を入力してください ')
    try:
        x = float(x)
        rnew = x

        diff = rnew - x/rnew
        if(diff < 0):
            diff = -diff
        while(diff > 1.0E-6):
            r1 = rnew
            r2 = x/r1
            rnew = (r1 + r2)/2
            print(r1, rnew, r2)
            diff = r1 - r2
            diff = abs(diff)
    except ValueError:
        print(x, 'は数値に変換できません')
        continue
    except:
        print('予期していないエラーです')
        exit()
    if(x <= 0):
        print(x, 'は正の数値ではありません')
        continue
    print(x)
