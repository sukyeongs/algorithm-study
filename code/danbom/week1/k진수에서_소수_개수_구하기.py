
# 양의 정수 n을 k진수로 바꾸는 함수 (리턴값 : 양의 정수 n을 k진수로 바꾼 문자열)
def decimal_to_k(n, k):
  
    # to_k :n을 k진수로 바꾼 문자열
    # n을 k로 나누었을 때 나머지값들이 순서대로 저장된다. 
    # 더 이상 나누어지지 않을 때, 문자열을 뒤집어 리턴한다.
    
    # div : n을 k로 나누었을 때 몫
    # 이 값이 0보다 클 때 까지 나머지를 구해 나머지값을 to_k에 이어 저장한다.
    
    to_k = ""
    div = n
    
    while (div > 0):
        to_k += str(div % k)
        div = div // k
        
    return to_k[::-1]


  
# 소수 판별 함수 (리턴값 : 정수 n이 소수이면 True, 소수가 아니면 False)
def is_prime(n):
  
    # 처음에 2부터 n까지 반복하며 나머지가 0일 경우 False를 리턴했는데,
    # n이 매우 큰 경우인 테케 1에서 시간 초과가 났다. (제한사항 : 1 ≤ n ≤ 1,000,000)
    # n의 약수는 n의 제곱근을 중심으로 대칭적으로 나타나기 때문에
    # 2부터 n의 제곱근까지로 반복 길이 조정
    
    if (n == 1): return False
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0): return False
    return True

  
  
# 소수 개수 구하는 함수 (리턴값 : 문자열 n을 0으로 분할했을 때, 나타나는 소수의 개수)
def count_prime(n):
  
    # count : 문자열 n을 검사했을 때, 소수가 나타나는 횟수
    # 문자열 n을 0으로 분할하고 분할된 문자열이 소수인 경우 count 증가
    
    count = 0
    for i in n.split('0'):
        if i != "":
            if is_prime(int(i)):
                count += 1
    return count
    
    
    
def solution(n, k):
    to_k = decimal_to_k(n,k)
    return count_prime(to_k)
  
