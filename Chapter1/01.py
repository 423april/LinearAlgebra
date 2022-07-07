'''
먼저 정수의 개수를 입력받은 다음, 해당하는 개수만큼의 정수를 입력받아 합을 계산하는 함수 calc()를 작성하라
'''


def calc(n):
    sum = 0
    for i in range(n):
        sum += int(input())
    return sum


print("Input the number of values to be added => ")
count = int(input())
while count <= 0:
    count = int(input())
print("Sum = ", calc(count))
