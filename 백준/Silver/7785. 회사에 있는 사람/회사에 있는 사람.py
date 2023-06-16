n = int(input())
log = {}
for _ in range(n):
    name, action = input().split()
    if action == 'enter':
        log[name] = True
    elif action == 'leave':
        del log[name]
        
names = list(log.keys())
names.sort(reverse=True)

for name in names:
    print(name)
