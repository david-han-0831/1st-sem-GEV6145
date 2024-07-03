# a. [30] 1~100 까지 integer random number가 들어 있는 3x10x10 배열을 만들고 결과를 화면에 출력하십시오. 
import numpy as np
arr = np.random.randint(1, 101, size=(3, 10, 10))
print(arr)

# b. [35] 50보다 크거나 같은 값은 1, 50보단 작은 값은 2로 변환한 결과를 화면에 출력하십시오.
new_arr = np.where(arr >= 50, 1, 2)
print(new_arr)

# c. [35] 1번째 배열에서 아래 그림에서와 같이 붉은색 상자 안의 원소들을 추출하여 화면에 출력하십시오. 
# 여기서, 배열 index는 0부터 시작하여, 0, 1, 2입니다.

new_arr2 = arr[1, -5:, -5:] # 처음 만든(a에서) 배열에서 가져오기
print(new_arr2)

new_arr3 = new_arr[1, -5:, -5:] # 1,2로 변환시킨 배열에서 가져오기
print(new_arr3)