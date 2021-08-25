def get_positive_numeral(x):
    try:
        x = float(x)
    except ValueError:
        return(x, 'は数値に変換できません')
    except:
        print('予期していないエラーです')
        exit()
    if(x <= 0):
        return(x, 'は正の数値ではありません')

v = input('正の数値を入力してください ')
r = get_positive_numeral(v)
print('結果は ', r)

