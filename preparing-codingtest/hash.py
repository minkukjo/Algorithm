from collections import defaultdict

# 오픈채팅방

def solution(record):
    answer = []
    
    names = {}
    for r in record:
        s = r.split()
        
        if len(s) == 3:
            names[s[1]] = s[2]
            
    for r in record:
        s = r.split()
        
        if s[0] == "Enter":
            answer.append(names[s[1]] +"님이 들어왔습니다.")
        elif s[0] == "Leave":
            answer.append(names[s[1]] +"님이 나갔습니다.")
            
    return answer

# 베스트 앨범
from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    genere_dic = defaultdict(list)
    play_dic = defaultdict(int)
    
    for i in range(len(genres)):
        genere_dic[genres[i]].append((i, plays[i]))
        play_dic[genres[i]] += plays[i]
    
    sorted_gen = sorted(play_dic.items(), key = lambda x:x[1], reverse=True)
    
    for genre in sorted_gen:
        # 튜플 정렬은 .sort()를 못쓰고 sorted(array, key, reverse)를 써야하는구나!
        two_songs = sorted(genere_dic[genre[0]], key=lambda x:x[1], reverse=True)[:2]
        
        for song in two_songs:
            answer.append(song[0])
            
    return answer

# 신고 결과 받기
from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    
    report_user = defaultdict(list)
    reported_count = defaultdict(int)
    
    for r in report:
        splited = r.split()
        
        if splited[1] in report_user[splited[0]]:
            continue
        report_user[splited[0]].append(splited[1])
        reported_count[splited[1]] += 1
    
    for id in id_list:
        reported_users = report_user[id]
        
        mail = 0
        for user in reported_users:
            if reported_count[user] >= k:
                mail += 1
        answer.append(mail)
    
    return answer

# 메뉴 리뉴얼

