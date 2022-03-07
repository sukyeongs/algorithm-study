## k진수에서 소수 개수 구하기


### 소수 구하기 함수
- 소수는 앞과 뒤가 *짝을 이루는 성질*이 있음


예 ) 36의 소수 : 2 - 18, 3 - 12, 6 - 6


-> 따라서 소수를 구하고 싶다면, N의 제곱근까지만 나누어 떨어지는지 확인하면 됨! 


```
def is_prime_num(n):
    # 제곱근 구하는 함수 : math.sqrt
    sqrt_n = math.sqrt(n)
    sqrt_n = int(sqrt_n) 
    for i in range(2,sqrt_n +1):
        if n % i == 0:
            return False
    return True
```


### N진법으로 바꾸는 함수
- 몫과 나머지를 구할 수 있는 함수 : divmod


```
몫, 나머지 = divmod(나눠지는 수, 나누는 수)
```
-> 따라서 divmod 함수를 반복하여 N진법을 구할 수 있음


```
def dec_to_n(k,n):
    rev_base = ''
    while k > 0:
        k, mod = divmod(k, n)
        rev_base += str(mod)
    return rev_base[::-1]
```