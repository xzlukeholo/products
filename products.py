import os #operating system
products = []

#讀取檔案
if os.path.isfile('products.csv'):    #檢查是否有檔案
	print('資料讀取成功!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '項目,金額' in line:
				continue
			name, price = line.strip().strip('元').split(',')
			products.append([name, price])

else:
	print('未找到之前的紀錄!')

#讓使用者輸入要紀錄的內容
print('輸入完畢請輸入q')
while True:
	name = input('請輸入開銷名稱:')
	if name == 'q':
		break
	price = input('請輸入花費金額:')
	p = [name, price]
	products.append(p)
# print('第一個花費名稱是:', products[0][0])
# print('第一個花費金額是:', products[0][1])
print('----------------------------------------')

#印出所有紀錄
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
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('項目,金額\n' )
	for p in products:
		p[1] = str(p[1])
		f.write(p[0] + ',' + p[1] + '元' + '\n')
		