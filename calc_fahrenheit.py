def calc_fahrenheit(c_temp):
    fahr_temp = ((9 / 5) * c_temp) + 32
    return fahr_temp

print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")

try:
    celcius = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요: "))

    fahrenheit = calc_fahrenheit(celcius)
except Exception as e:
    print(f"다음과 같은 예외가 발생했습니다: {e}")
else:    
    print(f"섭씨온도 : {celcius: >5.2f}", f"화씨온도 : {fahrenheit: >5.2f}", sep = "\n")