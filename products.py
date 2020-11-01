import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '項目,金額' in line:
				continue
			name, price = line.strip().strip('元').split(',')
			products.append([name, price])
	return products

#讓使用者輸入要紀錄的內容
def user_input(products):
	print('輸入完畢請輸入q')
	while True:
		name = input('請輸入開銷名稱:')
		if name == 'q':
			break
		price = input('請輸入花費金額:')
		p = [name, price]
		products.append(p)
	return products

# print('第一個花費名稱是:', products[0][0])
# print('第一個花費金額是:', products[0][1])

#印出所有紀錄
def print_products(products):
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

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('項目,金額\n')
		for p in products:
			p[1] = str(p[1])
			f.write(p[0] + ',' + p[1] + '元' + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('資料讀取成功!')
		products = read_file(filename)
	else:
		print('未找到之前的紀錄!')
		products = []
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
