def triangle(num):
    if num < 1:
        print(""請輸入大於等於1的數字"")
        return

    for i in range(1, num + 1):
        if i == 1 or i == num:
            print('* ' * i)
        else:
            print('*' + ' ' * (i - 2) + '*')
