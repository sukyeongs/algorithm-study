# WIL : Week 1
1주차에 대한 WIL
# kakao_92335
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92335
## Unsolved Code
```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def decimal_to_k_notation_converter(n,k):
    tmp = ''
    while n > 0:
        tmp += str(n%k)
        n //= k
    return tmp[::-1]

def solution(n, k):
    answer = 0
    converted_n = decimal_to_k_notation_converter(n,k)
    numbers = converted_n.split('0')
    
    for number in numbers:
        if number == '':
            continue
        if is_prime(int(number)):
            answer += 1
    return answer
```
### 결과
테스트 16개 중 1개 시간초과로 실패
### 접근
1. string으로 n을 10진법 -> k진법으로 변환한다.
2. 변환된 수(string)을 '0'으로 구분(split)한다. 이렇게 하면 문제에서 나온 '0P0', 'P0', '0P', 'P' 네가지 경우의 수를 추출할 수 있다.
3. 순회하며 소수인지 아닌지 판별한다. 이 때 구분된 리스트(numbers)에 ''이 있으면 continue로 예외처리.
### 회고
소수 판별 과정이 너무 naive해서 시간초과가 뜨는 것 같다. 방법론을 조금 더 알아보고 시도해야겠다.

## Solved Code
```python
import math

def is_prime(n):
    if n < 2:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def decimal_to_k_notation_converter(n,k):
    tmp = ''
    while n > 0:
        tmp += str(n%k)
        n //= k
    return tmp[::-1]

def solution(n, k):
    answer = 0
    converted_n = decimal_to_k_notation_converter(n,k)
    numbers = converted_n.split('0')
    
    for number in numbers:
        if number == '':
            continue
        if is_prime(int(number)):
            answer += 1
    return answer
```
### 결과
성공
### 접근
위와 동일하나 소수 판별에 차이가 있다. n을 2부터 n까지 나눠보며 소수를 판별하는 것이 아닌, 2부터 루트n 까지 나눠보며 판별한다.

위의 방법이 유효한 이유를 16을 예시로 설명하겠다. 16은 1, 2, 4, 8, 16 이 약수다. 이 때 16 = 1 * 16 = 2 * 8 = 4 * 4 라는 대칭 구조를 띈다. 따라서 1 ~ 16까지 나눠보며 소수인지 아닌지 판별 할 필요 없이 16의 제곱근인 4 까지만 나눠봐도 이를 판별할 수 있다 :)

## 1번 문제 회고
학교에서 c언어만 하다가 다시 파이썬 코테로 넘어오니 엄청 버벅거렸다,,,ㅠㅠ. 문제를 처음 봤을 때 몇가지 스텝으로 문제를 쪼갤 수 있었다. 하지만 거기까지고 구현하려고 하니 막혔다. 진법 변환부터 막혀서 다시 구글링 해보고 유튜브로 파이썬 문법 강의도 다시 듣고 문제로 돌아왔다. 

그렇게 첫 번째 코드를 완성했지만 시간초과가 떴다. 조건에 1 ≤ n ≤ 1,000,000에 정확성 테스트 10초(?)라 나와있어서 시간초과가 안 뜰줄 알았는데 실행시간 계산을 어떻게 하는거지..? 어쨋든 나동빈좌의 소수 판별 알고리즘 기법을 통해 O(n) -> O(루트n) 으로 개선하여 문제를 풀 수 있었다.

그리고 강의를 보며 <strong>에라토스테네스의 체</strong> 라는 알고리즘도 처음 알게 되었는데, 이는 어떤 범위 안의 수들이 소수인지 판별할 때 쓰인다고 한다. 이번 문제에서는 범위가 주어졌다고 생각하지 않아 이 알고리즘을 적용하지 않았다.

## Ref
[나동빈의 이코테 강의 : 소수 판별 알고리즘](
https://www.youtube.com/watch?v=CyINCmJPjfM&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=37)