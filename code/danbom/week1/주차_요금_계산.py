
# 문자열로 나타낸 시각을 정수형 분으로 변환하는 함수 (리턴값: 정수형 분으로 나타낸 시각값)
def hhmm_to_int(s):
    return int(s[:2])*60+int(s[3:])

  
  
# 주차요금 계산 함수 (리턴값: 주차요금)
def cal(time, fees):
  
    # time : 주차한 총 시간(분)
    # fees : [기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)]
    
    # 주차한 총 시간이 기본 시간보다 적거나 같은 경우,
    # 기본 요금 리턴
    
    if time <= fees[0]: 
        return fees[1]
      
    # 기본 시간을 초과했을 때,
    # 단위시간마다 단위요금 추가
    # 단, 초과 시간이 단위 시간에 나누어 떨어지지 않는 경우 올림 계산
    # over : 기본 시간 초과 시간 (분)
      
    over = time - fees[0]
    if not over % fees[2] == 0:
      over += fees[2]
    return fees[1] + over // fees[2] * fees[3]

  
  
def solution(fees, records):
  
    # fees : [기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)]
    # records : ["시각(시:분), 차량번호, 내역", ...]
    
    # time : time[i]는 차량번호 i가 주차한 총 시간(분)
    # = 차 번호는 네자리 양의 정수이므로 [0]*10000으로 초기화
    # entered : entered[i]는 차량번호 i가 입차한 시간(분)
    # = 입차하지 않은 경우를 -1로 나타내기 위해 [-1]*10000로 초기화
    # result : 차량 번호가 작은 자동차부터 청구할 주차 요금 배열
    
    time = [0]*10000
    entered = [-1]*10000
    result = []
    
    for r in records:
        hhmm, car, state = r.split()
        
        # 입차 및 출차 시각을 정수형 분으로 변환
        int_hhmm = hhmm_to_int(hhmm)
        
        # 차량 번호를 정수로 변환
        car = int(car)
        
        # 입차 : entered[차량번호]에 입차 시간 저장
        if state == "IN":
            entered[car] = int_hhmm
            
        # 출차 : 주차한 총 시간 저장(추가) 및 출차 상태로 변경
        else:
            time[car] += int_hhmm - entered[car]
            entered[car] = -1
            
    
    for i in range(10000):
      
        # 출차된 내역이 없는 경우,
        # 23:59에 출차된 것으로 간주
        if entered[i] != -1:
            time[i] += hhmm_to_int('23:59') - entered[i]
            
    for x in time:
        if x != 0:
            result.append(cal(x, fees))

    return result
  
