products = []

print('輸入完畢請輸入q')
while True:
	name = input('請輸入花費名稱:')
	if name == 'q':
		break
	price = input('請輸入花費金額:')
	p = [name, price + '元']
	products.append(p)

print(products)

# print('第一個花費名稱是:', products[0][0])
# print('第一個花費金額是:', products[0][1])