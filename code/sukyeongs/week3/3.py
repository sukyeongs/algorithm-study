def solution(enroll, referral, seller, amount):
    answer = []
    profit_dicts = {}
    tree_dicts = {}
    for i in range(len(enroll)):
        tree_dicts[enroll[i]] = referral[i]
        profit_dicts[enroll[i]] = 0

    for i in range(len(seller)) :
        cost = amount[i]*100
        node = seller[i]
        while node != '-':
            parent = tree_dicts[node]
            if cost*0.1 < 1:
                profit_dicts[node] += cost
                break
            profit_dicts[node] += (cost-(cost//10))
            cost //= 10
            node = parent


    for name in enroll :
        answer.append(int(profit_dicts[name]))
    return answer
