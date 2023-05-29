# 입력 받기
N = int(input())  # 회원 수

members = []
for _ in range(N):
    age, name = input().split()  # 나이와 이름 입력
    members.append((int(age), name))  # 나이는 정수형으로 변환하여 저장

# 회원 정렬하기
sorted_members = sorted(members, key=lambda x: x[0])  # 나이를 기준으로 오름차순 정렬

# 정렬된 결과 출력
for member in sorted_members:
    print(member[0], member[1])
