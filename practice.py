print(5)
print("풍선"*9)

# boolean 참 / 거짓
print(5>10)
print(not False)
print(not True)
print(not (5>10))

# 변수에대해서
age = 4
animal = "고양이"
name = "코카"
hobby = "집"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name +"에요")
print(name + "는 " + str(age) +"살이며, "+ hobby +"에만 있어요")
print(name + "는 어른일까요? " + str(is_adult))

age = 4
animal = "고먐미"
name = "모카"
hobby = "방"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name +"에요")
print(name + "는 " + str(age) +"살이며, "+ hobby +"에만 있어요")
print(name + "는 어른일까요? " + str(is_adult))

# 주석하는법
''' 작은 따옴표 3개 '''
# 샵
# ctrl + /

# 퀴즈 #1
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1+1)
print(2**3)
print(10%3)
print(10//3)
print(10 > 3)
print(3 == 3)
print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

# 간단한수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number) 
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
number %= 5 # 1
print(number)

# 숫자처리함수
print(abs(-5)) # 5 |-5|     절댓값 abs
print(pow(4, 2)) # 16 4**2  제곱 pow
print(max(5, 12)) # 12      최대 max
print(min(5, 12)) # 5       최소 min
print(round(3.14)) # 3      반올림 round
print(round(4.99)) # 5      반올림 round

# from math import *
from math import *
print(floor(4.99)) # 4      내림 floor
print(ceil(3.14)) # 4       올림 ceil
print(sqrt(16)) # 4         제곱근 sqrt

# 랜덤함수 random()[소수], randrange(정수, 미만), randint(정수, 이하)
from random import *
print(random()) # 0.0 ~ 1.0 (미만)의 임의의 값 생성 [0.0 ~ 0.*]
print(random() * 10) # 0.0 ~ 10.0 미만읜 임의의 값 생성 [0.0 ~ 9.*]
print(int(random() * 10)) # 0 ~ 10 (미만)의 임의의 값 생성 [0 ~ 9]
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성 [0 ~ 9]
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성 [0 ~ 9]

print(int(random() * 10) + 1) # 1 ~ 10 (이하)의 임의의 값 생성 [1 ~ 10]
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성 [1 ~ 45]

print(randrange(1, 45)) # 1 ~ 45 (미만)의 임의의 값 생성 [1 ~ 44]
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성 [1 ~ 45]

print(randint(1, 45)) # 1 ~ 45 (이하)의 임의의 값 생성 [1 ~ 45]

# 퀴즈 #2
from random import *
day = randint(4, 28) # 4 ~ 28 이하의 임의의 값 생성 [4 ~ 28]
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")
day = randrange(4, 29) # 4 ~ 29 미만의 임의의 값 생성 [4 ~ 28]
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다' # ' '
print(sentence)
sentence1 = "파이썬은 쉬워요" # " "
print(sentence1)
# """ """ 총 4줄
sentence2 = """ 
나는 소년입니다
파이썬은 쉬워요
"""
print(sentence2)

# 슬라이싱
# 성별만 가져오기, 생년도만 가져오기
seonghak = "990509-1234567"

print("성별 : " + seonghak[7])
print("년도 : " + seonghak[0:2]) # 0 ~ 2 미만의 값 출력 [0 ~ 1] 
print("생월 : " + seonghak[2:4]) # 2 ~ 4 미만의 값 출력 [2 ~ 3]
print("생일 : " + seonghak[4:6]) # 4 ~ 6 미만의 값 출력 [4 ~ 5]

print("생년월일 : " + seonghak[:6]) # 0 ~ 6 미만의 값 출략 [0 ~ 5]
print("뒷자리 [7]: " + seonghak[7:]) # 7 이후 마지막까지 값 출력 [7 ~ 13]
# 990509-1234567
# (-14)       (-1)
print("뒷자리 [7]: " + seonghak[-7:]) # -7 이후 마지막까지 값 출력 [-7 ~ -1]

# 문자열처리함수
python = "Python is Amazing"
print(python.lower()) # lower 모두 소문자로
print(python.upper()) # upper 모두 대문자로
print(python[0].isupper()) # isupper 해당 배열의 위치가 대문자인가? 맞으면 True, 틀리면 False (islower도 있음)
print(len(python)) # len 해당 문자열 길이 알려줌
print(python.replace("Python", "Java")) # replace 해당 단어를 다른 단어로 바꿔줌

#index 원하는 문자의 위치를 찾아줌
index = python.index("n")
print(index)
index = python.index("n", index + 1) # index python.index("n",index + 1) n을 찾은 이후 index 위치인 "n" 그 이후인 "n" + 1 다음에 나오는 "n"을 찾음 
print(index)

# find함수 : 해당 단어가 없어도 -1로 출력하며 쭉 진행 가능
# index함수 : 해당 단어가 없으면 오류 (뒤의 문장 출력도 X)
print(python.find("Java"))
#print(python.index("Java"))
print("hi")

print(python.count("i")) # count "i"처럼 문자열에서 해당된 알파벳의 갯수를 나타냄

# 문자열 포맷 
print("a" + "b")
print("a","b")

# 방법 1 
print("나는 %d살입니다." %25)
print("나는 %s을 좋아해요." %"파이썬")
print("Apple은 %c로 시작해요" %'A')
print("나는 %s색과 %s색을 좋아해요."%("보라", "브라운"))
# %d %~~~ %s %"~~~ " %c %'~' 

# 방법 2
print("나는 {}살입니다.".format(25))
print("나는 {}색과 {}색을 좋아해요.".format("보라","브라운"))
print("나는 {0}색과 {1}색을 좋아해요.".format("보라","브라운"))
print("나는 {1}색과 {0}색을 좋아해요.".format("보라","브라운"))
# {} .format(~) {} .format("~","~~") {0} {1} .format("~","~~")

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 25, color = "보라"))
# {age} {color} .format(age = ~, color = "~~")

# 방법 4 (v3.6 이상~)
age = 25
color = "보라"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
# print(f"~~~{age},~~~~{color}~~~~")

# 탈출 문자

# \n : 줄바꿈
print("도망쳐서 도착한 곳에는\n 낙원은 없다.")

# \' \" : 문장 내에서 작은 따옴표, 큰 따옴표
print('저는 "김성학"입니다.')
print("저는 \"김성학\"입니다.")
print("저는 \'김성학\'입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\jip98\\Desktop\\2023\\2023-01\\도망쳐서 도착한 곳에 낙원은 없다")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# 퀴즈 #3
 # 1
print("http://naver.com")
naver = "http://naver.com"
naver = naver[7:]
print(naver.index("."))
naver = naver[:5]

print(naver[:3] + str(len(naver)) + str(naver.count("e")) + '!')
 # 2
naver1 = "http://google.com"
naver1 = naver1.replace("http://","")
print(naver1)
naver1 = naver1[:naver1.index(".")]
#naver1 = naver1.replace(".com","")
print(naver1)

print(naver1[:3] + str(len(naver1)) + str(naver1.count("e")) + '!')

# 리스트 [value1, value2, value3]

# 지하철 칸별로 10명, 20명, 30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10, 20, 30]
print(subway)
subway = ["침착맨", "주호민", "기안84"]
print(subway)
# 주호민이 몇 번째 칸에 타고 있는가?
print(subway.index("주호민"))
# 주우재가 다음 정류장에서 다음 칸에 탐
subway.append("주우재") # ~.append(" ") ->-> 다음칸으로 추가
print(subway)
# 김진효를 침착맨 / 주호민 사이에 태워봄
subway.insert(1, "김진효")  # ~.insert(들어갈 위치, "들어갈 값")
print(subway)
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("침착맨")
print(subway)
print(subway.count("침착맨"))

# 정렬 sort
num_list = [5, 4, 3 ,2, 1]
num_list.sort()
print(num_list)
# 순서 뒤집기 reverse
num_list.reverse()
print(num_list)
# 모두 지우기 clear
num_list.clear()
print(num_list)
# 다양한 자료형 함께 사용
mix_list = ["침착맨", 25, True]
print(mix_list)
# 리스트 확장
num_list = [1, 2, 3, 4, 5]
num_list.extend(mix_list)
print(num_list)

# 사전 { key : value }
cabinet = {3:"룩삼", 100: "얍얍"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) [5] <- 처럼 없는 칸을 가져오면 오류로 실행이 종료됨
print(cabinet.get(5)) # 하지만 cabinet.get(5) <- 처럼 .get 함수를 이용하면 None으로 출력되고 그대로 진행
print(cabinet.get(5,"사용 가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"침착맨","B-100":"주호민"}
print(cabinet["A-3"])
print(cabinet["B-100"])
# 새 손님
print(cabinet)
cabinet["A-3"] = "기안84"
cabinet["C-20"] = "김진효"
print(cabinet)
# 간 손님
del cabinet["A-3"]
print(cabinet)
# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())
# 다 지우기 clear
cabinet.clear()
print(cabinet)

# 튜플 (value1, value2)
menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])
# 튜플은 추가, 변경이 안된다.
#menu.add("생선돈까스")

# name = "김진효"
# age = 30
# hobby = "데바데"
# print(name, age, hobby)

(name, age, hobby) = ("김진효", 30, "데바데")
print(name, age, hobby)

# 집합 (set) 세트 {value1, value2, value2, value3} ==> {value1, value2, value3}
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"룩삼","얍얍","한동숙"}
print(java)
# python = {"룩삼", "공혁준"}
python = set(["룩삼","공혁준"])
print(python)

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python)) # & == java.intersection(python)

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # | == java.union(python)

# 차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python)) # java.difference(python)

# python 할 줄 아는 사람이 늘어남
python.add("얍얍") # python.add("얍얍")
print(python)

# java를 까먹었다
python.remove("얍얍") # python.remove("얍얍")
print(python)

# 자료구조의 변경
menu = {"커피","우유","주스"} # 집합 **순서X, 중복X**
print(menu, type(menu))

menu = list(menu) # ["커피","우유","주스"] 리스트
print(menu, type(menu))

menu = tuple(menu) # ("커피", "우유", "주스") 튜플 **추가X, 변경X**
print(menu, type(menu))

menu = set(menu) # {"커피","우유","주스"} **순서X, 중복X**
print(menu,type(menu))

# 퀴즈 #4
from random import *
# 조건: 1 ~ 20
# 중복X
# random 모듈의 shuffle과 sample를 활용

lists = range(1, 21)
print(type(lists))
lists = list(lists)
print(type(lists))
shuffle(lists)

# 방법 1 shuffle
print("\n-- 당첨자 발표 --")
print("치킨 당첨자 :", lists[0])
print("커피 당첨자 :", lists[1:4])
print("-- 축하합니다 --\n")

winner = sample(lists, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winner[0]))
print("커피 당첨자 : {}".format(winner[1:]))
print("-- 축하합니다 --")

# if문 
# if ~~~: elif ~~~: elif ~~~: else:
'''temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에여")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요")
'''
# for문 
# for ~~ in [~, ~, ~]: or for ~~ in range(~):
''' starbucks = ["아이언맨", "캡틴아메리카", "닥터스트레인지"]
 for customer in starbucks:
     print("{}님 커피 가지고 가세요".format(customer))

 for i in range(1, 101):
     print("대기번호 : {}".format(i))
'''
# while
'''
customer = "토르"
index = 5
while index >= 1:
    print("{}, 커피가 준비 되었습니다. {}번 남았어요.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피 남은 수: {} 이므로, sold out".format(index))
customer = "침착맨"
person = "Unknown"
while person != customer:
    print("{}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세여?")
'''
# continue와 break
'''absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {} 은 교무실로 따라와".format(student))
        break
    print("{}번 책 읽어봐".format(student))

# 한 줄 for문
# 출석번호가 1, 2, 3, 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
student = [1, 2, 3, 4]
print(student)
student = [i + 100 for i in student] # student[1, 2, 3, 4] 총 4번 반복
# for 앞에 i + 100을 놓아놓고
print(student)

# 학생 이름을 길이로 변환
student = ["아이언맨", "침착맨", "룩삼"]
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
student = ["invasion", "customer", "looksam"]
student = [i.upper() for i in student]
print(student)

# 출석번호 1,2,3,4,5,6 앞에 1000 붙이기
student = [1, 2, 3, 4, 5, 6]
student = [i+1000 for i in student]
print(student)
# 학생 이름을 길이로 변환
student = ["fdsbdb","djhgdb","hrweg"]
student = [len(i) for i in student]
print(student)
# 학생 이름을 대문자로 변환
student = ["fdsbdb","djhgdb","hrweg"]
student = [i.upper() for i in student]
print(student)'''

# 퀴즈 #5
# 총 50명의 승객 중 나의 소요 시간과 매칭하는 총 탑승 승객 수 구하기
# 조건1 : 운행 소요 시간: 5분 ~ 50분 사이의 난수로 정해짐
# 조건2 : 나 소요 시간: 5분 ~ 15분 사이의 승객만 매칭
'''
from random import *
count = 0 # 총 탑승 승객 수
for i in range(1, 51):
    time = randint(5, 50)
    if 5 <= time <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분".format(i, time))
        count += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분".format(i, time))
print("총 탑승 승객 : {}분".format(count))
'''

# 함수
'''def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()'''

# 전달값과 반환값
'''
def deposit(value, money): # [입급] 잔액(value), 입금할 금액(money)
    print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(value + money))
    return value + money

def withdraw(value, money): # [출금] 잔액(value), 출금할 금액(money)
    if value >= money:
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(value - money))
        return value - money
    else:
        print("잔액 부족으로 출금을 실패합니다. 잔액은 {}원입니다.".format(value)) 
        
def withdraw_night(value, money): # 저녁에 출금
    commission = 500 # 수수료
    if value >= money:
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(value - money - commission))
        return commission, value - money - commission
    else:
        print("잔액 부족으로 출금을 실패합니다. 잔액은 {}원입니다.".format(value)) 

value = 1000
print("현재 잔액: {}원 입니다.".format(value))
value = deposit(value, 50000)
print(value)
print("현재 잔액: {}원 입니다.".format(value))
put = int(input("출금할 금액: "))
value = withdraw(value, put)
print(value)
# 밤에 출금
put = int(input("출금할 금액: "))
commission, value = withdraw_night(value, put)
print("밤에 출금할 시 수수료 {}원이 차감됩니다. ".format(commission))
print(value)
'''

# 기본값
def profile(name, age, main_lang):
    print("이름: {}\t나이: {}\t주 사용 언어: {}".format(name,age,main_lang))

profile("침착맨", 20, "파이썬")
profile("주호민", 25, "자바")

def profile(name, age = 25, main_lang = "파이썬"):
    print("이름: {}\t나이: {}\t주 사용 언어: {}".format(name,age,main_lang))
profile("룩삼")
profile("얍얍")

# 키워드값
def keyword(name, age, main_lang):
    print(name, age, main_lang)

keyword(name="침착맨",main_lang="파이썬", age=25)
keyword(main_lang="자바", age=24, name="주호민")

# 가변인자

#def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#    print("이름 : {}\t나이: {}\t".format(name,age), end=" ") # 문장이 끝나고 줄바꿈 없이 이어서 가기 end=" "
#    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
   print("이름 : {}\t나이: {}\t".format(name,age), end=" ") # 문장이 끝나고 줄바꿈 없이 이어서 가기 end=" "
   for i in language:
    print(i, end=" ")
   print()

profile("룩삼","30","자바","파이썬","C#","C++","C")
profile("얍얍","31","C#","C++","C"," "," ")

# 지역변수와 전역변수
gun = 10
# 전역변수 global
def checkpoint(soldiers): # 경계근무
    #global gun # 전역 공간에 있는 gun 사용
    gun=10
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

def checkpoint_ret(gun, soldiers): # 경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun

# print("전체 총: {}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {}".format(gun))

print("전체 총: {}".format(gun))
gun = checkpoint_ret(gun, 2) # 2명이 경계 근무 나감
print("남은 총 : {}".format(gun))

# 퀴즈 #6

# 표준 체중 구하기
# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#       * 함수명 : std_weight
#       * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# def std_weight(height, gender):
#     if gender == "남성":
#         height = float(height/100) * float(height/100) * 22
#         return height
#     elif gender == "여성":
#         height = float(height/100) * float(height/100) * 21
#         return height
# # round(weight, 2) ==> 소수점 둘째자리까지
# height = 175
# gender = "남성"
# weight= std_weight(height , gender)
# print("키 {}cm {}의 표준 체중은 {}.kg 입니다".format(height, gender, round(weight,2)))

# 표준 입출력 sep =
# 원래는 python은 줄 끝에 end [\n]으로 되어있다
print("Python","Java", sep=",")#, end="")

import sys
print("Python", "Java", file=sys.stdout) # 표준출력
print("Python", "Java", file=sys.stderr) # 에러코드 따로

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# # 은행 대기순번표
# # 001, 002, 003, 004, 005, 006, ...
# for num in range(1, 21):
#     print("대기번호 : "+str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 "+ answer + "입니다.")
# print(type(answer)) # 입력한 값은 항상 str 이다 주의 할 것

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리 마다 콤마를 찍어주기, +-부호도 붙이기
print("{0:+,}".format(-100000000000))
print("{0:+,}".format(100000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000)) # +100,000,000,000^^^^^^^^^^^^^^
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (.2f 소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

# 파일입출력
score_file = open("score.txt", "w", encoding="utf8") # write 쓰기 위한 목적임 "w"
print("수학 : 0", file=score_file) # "w" 작성 후 다음에도 "w"로 작성하면 덮어쓰기만 됨 추가x
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # append 이미 존재하는 파일에 이어쓰기 "a"
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt","r", encoding = "utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt","r", encoding = "utf8")
print(score_file.readline(),end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline())
score_file.close()

# # 파일이 몇 줄일지 모를때 읽어오기
# score_file = open("score.txt", "r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines() # list 형태로 저장
# print(type(lines))
# for line in lines:
#     print(line,end="")
# score_file.close()

# pickle
# import pickle
# # profile_file = open("profile.pickle", "wb") # "w" == write  "b" == binary라는 뜻인데 pickle를 쓰기위해서는 입력해야됨
# # profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r",encoding="utf8") as study_file:
#     print(study_file.read())

# 퀴주 #7
# for weeks in range(1, 51):
#     score_file = open(str(weeks) + "주차.txt", "w", encoding="utf8") # write 쓰기 위한 목적임 "w"
#     print("- "+str(weeks)+"주차 주간보고 -", file=score_file) # "w" 작성 후 다음에도 "w"로 작성하면 덮어쓰기만 됨 추가x
#     # score_file.write("- " + str(weeks) + "주차 주간보고 -")
#     print("부서 : ", file=score_file) # score_file.write("\n부서 : ")
#     print("이름 : ", file=score_file) # score_file.write("\n이름 : ")
#     print("업무 요약 : ", file=score_file) # score_file.write("\n업무 요약 : ")
#     score_file.close()

# # 클래스
# class Unit:
#     def __init__(self, name, hp, damage): # 클래스를 쓰면 자동으로 호출되는 함수 __init__
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {}, 공격력 {}".format(self.hp,self.damage))

# # __init__ 똑같이 설정한 갯수과 같도록 설정해야됨
# marin1 = Unit("마린", 40, 5)
# marin2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 멤버변수
# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name,wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 파이썬은 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있음.

# if wraith2.clocking == True:
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 메소드
# 일반 유닛 
# 상속
# 다중상속 부모가 2 이상
'''
class Unit: # 부모 클래스 상속을 줌
    def __init__(self, name, hp): 
        self.name = name
        self.hp = hp


class AttackUnit(Unit): # 자식 클래스 상속을 받음
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp = self.hp - damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 받는다고 가정
firebat1.damaged(5)

# 드랍쉽 : 공중 유닛, 수송기. /마린 / 파이어뱃 탱크 등을 수송. 공격 X
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp , damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name,"3시")
'''
# 연산자 오버로딩
class Unit: # 부모 클래스 상속을 줌
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

class AttackUnit(Unit): # 자식 클래스 상속을 받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp = self.hp - damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp , 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move() 재정의 ==> 그러면 Unit에 있는 move함수가 초기화되고 FlyableAttackUnit에 있는 move가 출력됨
        print("[공중 유닛 이동]")
        self.fly(self.name, location)    # 그냥 self가 아니라 self.name이기 때문에 이름 더 적을 필요 없음

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80 , 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly("배틀크루저", "9시")
battlecruiser.move("9시")

# pass 오류없이 그냥 넘어감
# 건물
'''
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
'''
# super 쓰임새 
# Unit.__init__(self, name, hp, 0)
# super().__init__(name, hp, 0)
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) 
        super().__init__(name, hp, 0)
        # super().__init__(~~)은 다중 상속을 받을 때 사용하면 안됨. 중복이 안되므로 마지막에 불려진 함수만 출력됨.
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
