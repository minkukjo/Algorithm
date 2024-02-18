# 예상 대진표

# a와 b를 적절히 나눠서 둘이 0이 될 때 까지 반복. 근데 이게 왜 트리 문제지?

def solution(n,a,b):
    answer = 0

    while a != b:
        
        a = (a+1) // 2
        b = (b+1) // 2
        
        answer += 1
    return answer
    
# 다단계 칫솔 판매

class Seller:
    def __init__(self, money, parent, name) -> None:
        self.money = money
        self.parent = parent
        self.childs = []
        self.name = name
        
    # enroll의 최대값이 10000
    # log2(10000+1) => 대략 13 
    # 휴리스틱하게 접근할 경우, 어쨌든 탐색 중간에 값을 찾으니까 엄청 오래 걸리지는 않는 알고리즘
    def find_node(self, target_name):
        if self.name == target_name:
            return self
        for child in self.childs:
            found = child.find_node(target_name)
            if found:
                return found
        return None

def solution(enroll, referral, seller, amount):
    answer = []
    
    who_is_parent = {enroll[i]: referral[i] for i in range(len(referral))}
    result = {}
    
    root = Seller(0, None, "-")
    
    for e in enroll:
        parent_name = who_is_parent[e]
        
        if root.name != parent_name:
            parent_node = root.find_node(parent_name)
        else:
            parent_node = root
        parent_node.childs.append(Seller(0, parent_node, e))
    
    for i in range(len(seller)):
        total = amount[i] * 100
        seller_name = seller[i]
        seller_node = root.find_node(seller_name)
        share(seller_node, total)
        
    setResult(root, result)
    
    for e in enroll:
        answer.append(result[e])
    
    return answer
    
def share(node, money):
    if node.name == "-":
        return
    left = int(money * 0.1)
    node.money += money - left
    share(node.parent, left)
    
def setResult(node, result):
    result[node.name] = node.money
    for child in node.childs:
        setResult(child, result)         

# 시간 초과
# 그냥 딕셔너리로 쉽게 풀자....
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    who_is_parent = dict(zip(enroll,referral))
    temp = defaultdict(int)
    answer = []
    
    def setResult(seller, profit):
        if seller == "-" or profit == 0:
            return
        left = int(profit * 0.1)
        temp[seller] += profit - left
        setResult(who_is_parent[seller], left)

    for i in range(len(seller)):
        profit = amount[i] * 100
        
        setResult(seller[i], profit)
        
    for e in enroll:
        answer.append(temp[e])
        
    return answer
    
    
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])