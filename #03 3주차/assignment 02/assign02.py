# Assignment 02 (총 100점)

# 1. [10] 수강생의 학번(ID), 성명(name), 성적(점수:score), 전공(major), 과목(couse)을 포함한 
#    필요한 속성들을 저장할 수 있는 class를(Student) 정의하고,

# 2. [10] 평균성적을 출력하는 method 및 추가로 필요한 method 혹은 function을 정의합니다.
#    모든 학생은 GEV6145를 수강하고 있는 것으로 가정합니다.

# 3. [10] Excel 화일로 제공되는 수강생 명단을 읽어드려, 수강생 instance를 생성합니다.

# 4. [10] 수강생 별 점수는 80점이상 100점이하 사이의 
#    random number로(소수점이하 1자리) 생성하되 정규분포하도록 할당합니다.

# 5. [10] 생성된 총 수강생 수를 화면에 출력하십시오.

# 6. [10] 수강생들의 점수 평균을 화면에 출력하십시오. 80-100점 사이에서 정규분포하므로
#         평균은 90점에 가까울 것입니다.

# 7. [10] "Enter ID: "란 prompt에 ID의 마지막 4자리 digit을 입력하면, full-ID, 성명, 전공, 점수를
#     출력하도록 하십시오.
#     Enter ID: 0230
#      2023400230, 홍길동, 인공지능, 84.2.
      
# 8. [10] get_Name(stu01)을 실행하면 stu01 성명을 화면에 출력하도록 합니다.

# 9. [20] instance_name["name"] 를 입력하면 stu01 ID과 점수를 화면에 출력합니다.


# % 주의점 %
# a. assign02_홍길동.ipynb 화일을 제출하십시오. 첫자 'a'는 소문자입니다. 과제명과 성명 사이는 _(single underscore)입니다.

# b. 채점자가 제출자의 logic을 따라 채점할 수 있도록 code를 논리 block 별로 구분하고, 간결하나 충분한 comment 하십시오.
#    comment가 없을 시 정도에 따라 총 점수의 최대 20%까지 감점합니다.
#    논리적으로 구분된 code block을 하나의 cell에서(Jupyter Notebook) 실행하여 채점자가 이해하기 쉽도록 합니다.

# c. method 앞에는 반드시 decorator @instancemethod 등을 명시합니다.

# d. 생성되는 instance 명은 stu01부터 stu36으로 합니다. 제공되는 excel 화일의 '번호' column의 값-2가 stuXX의 XX에 해당합니다.
#    예: 번호 값이 38이면 stu36이 됩니다.

# e. class, instance, method, function 등을 명명할 때 Python에서 지향하는 naming convention을 따르십시오.
#    예: class 명은 대문자로 시작해 class임을 알립니다. instance attribute는 명사로, method는 동사를 주로 선택 등.

# 여러분의 판단에 따라, class variable, instance method, class method, static method,
# general function 등을 자유롭게 사용할 수 있습니다. 