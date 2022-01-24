# 해시
# 옷의 조합의 개수를 찾는 문제
# 직접 조합을 구하는게 아니라 공식으로 풀이
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1