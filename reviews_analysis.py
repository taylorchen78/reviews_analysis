data = []
count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))

print('Read done')
