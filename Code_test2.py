def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1
n = int(input(""請輸入人數：""))
k = 3

last_person = josephus(n, k)
print(""最後留下的同事是第"", last_person, ""順位。"")"
