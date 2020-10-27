products = []

print('輸入完畢請輸入q')
while True:
	name = input('請輸入花費名稱:')
	if name == 'q':
		break
	price = input('請輸入花費金額:')
	p = [name, price]
	products.append(p)

print('----------------------------------------')

sum_p = 0
num_p = 0
for p in products:
	print(p[0], '的花費是:', p[1] + '元')
	p[1] = int(p[1])
	sum_p += p[1]
	num_p += 1

average = sum_p / num_p
average = str(average)
print('平均花費是:', average + '元')

# print('第一個花費名稱是:', products[0][0])
# print('第一個花費金額是:', products[0][1])