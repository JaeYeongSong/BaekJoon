A, B, C = map(int, input().split())

# 노트북 가격보다 1개당 생산하는 비용이 크다면
if B >= C:
    print(-1)
else:
    # 1. 1개당 생산하는 비용 구하기 (C - B)
    # 2. 1개당 생산하는 비용에서 고정지출로 나눠서 본전 구하기
    # 3. +1로 손익분기점 찾기
    print(int(A / (C - B) + 1))