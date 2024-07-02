# 1. [10] 수강생의 학번(ID), 성명(name), 성적(점수:score), 전공(major), 과목(couse)을 포함한
#    필요한 속성들을 저장할 수 있는 class를(Student) 정의하고,

# 2. [10] 평균성적을 출력하는 method 및 추가로 필요한 method 혹은 function을 정의합니다.
#    모든 학생은 GEV6145를 수강하고 있는 것으로 가정합니다.



# Excel 파일을 읽기위한 pandas import
import pandas as pd

# 80점 이상 100점 이하 사이의 random number를 생성하기 위한 random import
import random

# class 생성
class Student:

    # 초기화 함수
    # 학번(ID), 성명(name), 성적(점수:score), 전공(major), 과목(course) 지정
    def __init__(self, ID, name, score, major, course):
        self.ID = ID
        self.name = name
        self.score = score
        self.major = major
        self.course = course

    # ["name"] 으로 접근하기 위한 method
    # 9. 문제에서 사용
    def __getitem__(self, key):
        if key == "name":
            print(f"{self.ID}, {self.score}")

    # 모든 학생은 GEV6145를 수강하고 있는 것으로 가정
    # 과목을 가져오는 method
    @staticmethod
    def get_course():
        return "GEV6145"


    # 평균성적 출력하는method
    @staticmethod
    def get_average_score(stu_list):
        score_sum = 0
        for stu in stu_list:
            score_sum += stu.score
        score_avg = score_sum / len(stu_list)
        return score_avg