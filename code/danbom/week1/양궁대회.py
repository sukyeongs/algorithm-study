
# 깊이 탐색을 통해 나온 (현재 순서, 현재 라이언의 점수 별 화살 개수 배열)들을 저장하고 다시 반복하기 위해 deque 도입 
from collections import deque

# 깊이 탐색 (리턴값 : "라이언이 가장 큰 점수 차이로 우승하기 위한 10점부터 0점까지 맞춘 화살 개수 배열"들의 배열)
def bfs(n, apeachInfo):
  
    # n : 주어진 화살의 개수
    # apeachInfo : 어피치의 점수 별 화살 개수 배열
    
    # maxGap : 최대 점수 차 
    # = 0으로 초기화
    # deq : (현재 순서, 현재 라이언의 점수 별 화살 개수 배열)들을 담을 deque 
    # = deque([(0, [0 for i in range(len(apeachInfo))])])으로 초기화
    # res : 리턴값(배열)으로 아예 없거나, 여러개일 가능성이 있다
    # = []로 초기화
    
    maxGap = 0
    deq = deque([(0, [0 for i in range(len(apeachInfo))])])
    res = []
    
    while deq:
      
        # cnt : 현재 순서로, 현재 과녁 점수는 10-cnt
        # ryanInfo : 현재 라이언의 점수 별 화살 개수 배열
        
        cnt, ryanInfo = deq.popleft()
        
        # 1. 라이언이 화살을 모두 쏜 경우
        
        if sum(ryanInfo) == n:
          
            # apeachSum : 어피치의 전체 점수
            # ryanSum : 라이언의 전체 점수
            
            apeachSum, ryanSum = 0, 0
            
            # 점수 별 화살의 개수가 더 많은 사람이 점수를 가져간다
            for i in range(len(apeachInfo)):
                if not (apeachInfo[i] == 0 and ryanInfo[i] == 0):
                    if apeachInfo[i] >= ryanInfo[i]:
                        apeachSum += 10 - i
                    else:
                        ryanSum += 10 - i
                        
            # 1-1. 라이언이 이긴 경우,
            if apeachSum < ryanSum:
              
                # gap : 라이언과 어피치의 점수 차
                # gap이 maxGap 보다 클 때, res를 초기화하고 res에 현재 라이언의 점수 별 화살 개수 배열을 저장한다.
                # gap이 maxGap 과 같을 때, res에 현재 라이언의 점수 별 화살 개수 배열을 추가한다.
                
                gap = ryanSum - apeachSum
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(ryanInfo)
        
        
        
        # 2. 라이언이 쏜 화살 개수가 n보다 클 경우 거르기
        
        elif sum(ryanInfo) > n:
            continue
        
        
        
        # 3. 라이언이 화살을 모두 사용하지 않았는데, 현재 순서가 10인 경우
        # 남은 화살을 모두 써버리고 deq에 추가한다.
        
        elif cnt == 10:
            tmp = ryanInfo.copy()
            tmp[cnt] = n - sum(tmp)
            deq.append((cnt+1, tmp))
        
        
        
        # 위의 3가지 경우가 모두 아닌 경우
        # 라이언이 현재 점수에서 
        # 이기기 위해 어피치보다 1발 많이 쏘거나
        # 지기 위해 아예 화살을 쏘지 않는 두 경우를 deq에 추가한다.
        
        else:
            more = ryanInfo.copy()
            more[cnt] = apeachInfo[cnt]+1 
            deq.append((cnt+1, more))
            zero = ryanInfo.copy()
            zero[cnt] = 0
            deq.append((cnt+1, zero))
    
    return res

  
  
def solution(n, info):
    result = bfs(n, info)
    
    # result 배열의 원소가
    # 없는 경우 : 라이언이 어피치를 이길 수 있는 방법이 없으므로 [-1] 리턴
    # 1개인 경우 : 원소 하나를 리턴
    # 여러개인 경우 : 가장 낮은 점수를 더 많이 맞힌 경우를 리턴해야한다.
    # 과녁 점수가 높은 순으로 탐색해 배열에 추가해왔으므로, 가장 마지막 원소를 리턴
    
    if not result:
        return [-1]
    elif len(result) == 1:
        return result[0]
    else:
        return result[-1]
