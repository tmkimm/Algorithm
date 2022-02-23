def solution(n, arr1, arr2):
    arr1_0b = []
    arr2_0b = []
    for i in arr1:
        arr1_0b.append(bin(i)[2:].zfill(n))
    for i in arr2:
        arr2_0b.append(bin(i)[2:].zfill(n))
    
    answer = []
    for i1, i2 in zip(arr1_0b, arr2_0b):
        string = ""
        for x, y in zip(i1, i2):
            if x == '1' or y == '1':
                string += "#"
            else:
                string += " "
        answer.append(string)    
        
    return answer