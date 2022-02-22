def solution(N, stages):
    cnt = {}
    for i in stages:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
            
    user_cnt = len(stages)
    failover = {}
    for i in range(1, N + 1):
        if i not in cnt:
            cnt[i] = 0
        if cnt[i] != 0:    
            failover[i] = (cnt[i] / user_cnt)
            user_cnt -= cnt[i]
        else:
            failover[i] = 0
            
    answer = []
    for x, y in sorted(failover.items(), key=lambda x: x[1], reverse=True):
        answer.append(x)
    return answer