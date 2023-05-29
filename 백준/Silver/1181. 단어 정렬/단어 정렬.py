# 입력 받기
N = int(input())  # 단어의 개수

words = []
for _ in range(N):
    word = input().strip()  # 입력된 단어에서 공백 제거
    words.append(word)

# 단어 정렬하기
words = list(set(words))  # 중복 제거
sorted_words = sorted(words, key=lambda x: (len(x), x))  # 길이에 따라 오름차순, 길이가 같으면 사전 순으로 정렬

# 정렬된 결과 출력
for word in sorted_words:
    print(word)
