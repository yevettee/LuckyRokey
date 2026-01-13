# PCCE 기출문제 3번/ 수나누기
# 문제 설명
# 2자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

# 제한사항
# 10 ≤ number ≤ 2,000,000,000
# number의 자릿수는 2의 배수입니다

print('1--------------------')
number = int(input())

answer = 0

for i in range(5):
    answer += number % 100
    number //= 100

print(answer)
# 제한 사항에 2,000,000,000의 범위 제한이 걸려있기 때문에 범위를 5로 한정 

print('2--------------------')
number = int(input())

answer = 0

while number >= 10 :
    answer += number % 100
    number //= 100

print(answer)

# while 문을 사용하여 number의 자리수가 2자리 수 밑으로
# 내려갈 때 멈추는 반복문 실행

print('3--------------------')
number = int(input())

answer = 0

for i in range((len(str(number)))//2):
    answer += number % 100
    number //= 100
print(answer)

# 문자열로 변환하여 자리수를 구하기 위해 문자열 변환 함수 사용
# 2자리씩 묶어야 했기 때문에 2로 나눈 몫을 범위로 잡음