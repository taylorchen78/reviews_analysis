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

word_count = {}
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 100:
		print(word, word_count[word])

print(len(word_count))


user_word = input('Please enter word: ')
if user_word in word_count:
	print(user_word, 'shows in ', word_count[user_word], ' times')
else:
	print(user_word, 'not in list')
