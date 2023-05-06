n = int(input())
x_nums = []
y_nums = []

for _ in range(n):
    x,y = map(int,input().split())
    x_nums.append(x)
    y_nums.append(y)

width = max(x_nums) - min(x_nums)
height = max(y_nums) - min(y_nums)

print(width * height)