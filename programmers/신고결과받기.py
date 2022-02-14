def solution(id_list, report, k):
    notice = {}         # 알림 받은 수
    report_list = {}    # id별 신고 내역
    report_cnt = {}     # id별 신고 받은 횟수
    suspended = []      # 정지된 사용자 수
    
    # 초기화
    for id in id_list:
        notice[id] = 0
        report_list[id] = []
    report_cnt = notice.copy()
    
    # set을 이용하여 중복 제거
    report = set(report)          
    
    # id별 신고 내역 dict로 정리
    for item in report:
        a, b = item.split()
        report_cnt[b] += 1
        report_list[a].append(b)
        if report_cnt[b] == k:      
            suspended.append(b)
     
    for suspend_id in suspended:
        for key in report_list.keys():
            if suspend_id in report_list[key]:
                notice[key] += 1
    
    return list(notice.values())