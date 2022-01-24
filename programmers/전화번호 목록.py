# 해시
# 배열중 접두어가 있는지 찾는 문제
# 굳이 해시를 왜만드나 했는데 리스트에서 in으로 검사하는 것 보다 hash로 확인하는게 더 빠르기 때문
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
      
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

"""
다른 사람 풀이
sort를 사용하면 속도가 느려짐
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
"""