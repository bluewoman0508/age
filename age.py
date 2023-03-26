#使用年齡判斷是否能夠開車
age = input('請輸入年齡')
age = int(age)
driving = input ('請問你有開車嗎?')
if driving == '有':
	if age >= 18:
		print('有守法!')
	else:
		print('報警處理!!請考駕照!')
elif driving == '沒有':
	if age >= 18:
		print('是時候考駕照了~')
	else:
		print('你有乖~')
else:
	print('請依題意回答')


    