def get_positive_numeral(x):
      try:
          x = float(x)
          return x
      except ValueError:
          return(x, 'は数値に変換できません')
      except:
          print('予期していないエラーです')
          exit()
      if(x <= 0):
          return(x, 'は正の数値ではありません')

def square_root(x):
    '引数 x の平方根を求める'
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
        if(diff < 0):
            diff = -diff
    return rnew

v = input('正の数値を入力してください ')
r = get_positive_numeral(v)
k = square_root(r)
print('結果は ', k)