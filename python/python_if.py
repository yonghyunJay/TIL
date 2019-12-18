print('-------------- TEST 1 --------------')

a = 30
if a > 30 : 
    print('30 초과')
elif a <= 20 :
    print('20 이하')
else :
    print('둘다아님')

print('-------------- TEST 2 --------------')

if 30 < a and a < 150 :
    print('두조건 만족')
elif a > 150 or a > 10 :
    print('두조건 중 하나만 만족')

print('-------------- TEST 3 --------------')

dust = 43

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해부세요.
if dust > 150 :
    dust_str = '매우 나쁨'#print('매우 나쁨')
elif dust <= 150 and dust > 80 :
    dust_str = '나쁨'#print('나쁨')
elif dust <= 80 and dust > 30 :
    dust_str = '보통'#print('보통')
else :
    dust_str = '좋음'#print('좋음')
print('{} 입니다.'.format(dust_str))