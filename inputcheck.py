while True:
    x = input('正の数値を入力してください ')
    try:
        x = float(x)
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
