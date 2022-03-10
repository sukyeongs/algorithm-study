## 1. 92335 k진수에서 소수 개수 구하기

#### 1) 10진수를 k진수로 바꾸기

```python
    while n:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    
    rev_base = rev_base[::-1]
```

**divmod**(n, k): n을 k로 나눈 몫과 나머지를 제공하는 함수

나머지를 순서대로 저장한 뒤, 순서를 바꾸면 k진수 변환



#### 2) 소수 판별

```python
for j in range(2, int(i**0.5)+1):
            if i%j==0:
                prime = False
                break
```

판별하고자 하는 수의 제곱근에 1을 더한 수로 나누어 떨어지면 합성수, 나누어 떨어지지 않으면 소수

→ 이는 파이썬 **math.sqrt**를 사용해도 좋을 것 같음

 



## 2. 양궁대회

#### 1) 파이썬으로 중복조합 사용

```python
from itertools import combinations_with_replacement

...

def solution(n, info):
	for i in combinations_with_replacement(range(11), n):
        ...
```

**itertools**: 리스트, 튜플, 문자열 등의 요소에서 순열과 조합을 구할 수 있도록 도와주는 라이브러리

**combinations_with_replacement**: 중복조합
