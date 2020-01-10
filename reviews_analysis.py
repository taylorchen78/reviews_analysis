data = []
count = 0
reviews_len = 0

with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		reviews_len += len(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('\nRead done')
print('\nReviews length averge: ', reviews_len/count)
