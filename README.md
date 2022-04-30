# SRT_MACRO
 
1. python3 설치

2. pip3 install selenium

3. 코드 맨마지막에서 필요한 부분 수정
if __name__ == "__main__":
    driver = open_brower()
    driver = login(driver, '아이디', '비밀번호')
    search_train(driver, "출발역", "도착역", "예매 날짜", "예매시간") #기차 출발 시간은 반드시 짝수

4. python3 macro.py