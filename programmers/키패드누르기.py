def cal_distince(now, target):
    result = 0
    if now > target:
        bigger = now
        smaller = target
    else:
        bigger = target
        smaller = now
        
    while bigger - 3 >= smaller:
        result += 1
        bigger -= 3
        
        if bigger == smaller:
            return result
    
    while bigger != smaller:
        result += 1
        bigger -= 1
        
    return result 

def solution(numbers, hand):
    dict = {1: 'L', 3: 'R', 4: 'L', 6:'R', 7: 'L', 9 : 'R'}
    answer = ''
    result = ''
    l_pos = 10
    r_pos = 12
    
    for n in numbers:
        n = 11 if n == 0 else n
        if n in dict:
            result = dict[n]
        else:
            l_distince = cal_distince(l_pos, n)
            r_distince = cal_distince(r_pos, n)
            if l_distince == r_distince:
                result = 'R' if hand == 'right' else 'L'
            elif l_distince > r_distince:
                result = 'R'
            else:
                result = 'L'
        
        answer += result
        if result == 'L':
            l_pos = n
        else:
            r_pos = n
    return answer