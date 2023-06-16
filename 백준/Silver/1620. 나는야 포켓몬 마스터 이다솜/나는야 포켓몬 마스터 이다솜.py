import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokedex = {}
pokedex_number = {}

for i in range(1, n+1):
    pokemon = input().strip()
    pokedex[i] = pokemon
    pokedex_number[pokemon] = i

for _ in range(m):
    question = input().strip()
    if question.isdigit():
        print(pokedex[int(question)])
    else:
        print(pokedex_number[question])
