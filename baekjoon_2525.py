#2525번 - 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

hour, min = input("시간과 분을 입력하세요 : ").split()
time_over = int(input("필요한 시간을 분 단위로 입력하세요:"))

hour = int(hour)
min = int(min)

hour = hour + (min + time_over) // 60
min = (min + time_over) % 60

if hour >= 24:
    hour = hour - 24

print(hour, min)