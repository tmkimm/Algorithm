def solution(d, budget):
    d.sort()
    sum = 0
    answer = []
    for i in d:
        if sum == budget:
            break
        if sum + i <= budget:
            sum += i
            answer.append(i)
    return len(answer)