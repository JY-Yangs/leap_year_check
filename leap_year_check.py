# 確認是否為年閏年, 閏年 => return True ; 不是閏年 => return False

def is_leap():
	year = int(input('請輸入年份: '))
	if year % 4 != 00:
		return False
	elif year % 100 != 0: # year % 4 == 0 and 不用寫, 因為year % 4一定是等於0才會跳過第一個if的loop
		return True
	elif year % 400 != 0: # year % 100 == 0 and 不用寫, 因為year % 100一定是等於0才會跳過第二個if的loop
		return False
	elif year % 3200 != 0: # year % 400 == 0 and 不用寫, 因為year % 400一定是等於0才會跳過第三個if的loop
		return True
	else:
		print('無法判斷') # 題目沒交代可被3200整除的話是閏年還是平年
print(is_leap())