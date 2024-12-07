n = int(input())
a = n//1000
b = (n//100)%10
c = (n//10)%10
d = n % 10
mas = [a+b, b+c, c+d]
ans = max(mas)*100
mas.remove(max(mas))
ans += max(mas)
print(ans)