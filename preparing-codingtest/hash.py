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