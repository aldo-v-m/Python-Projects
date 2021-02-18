# exercise 3

add_more_words = 'y'
my_dict=dict()

while add_more_words == 'y' or add_more_words =='Y':
	#This section tests the word before saving it 
	word_contains_digit = True
	while word_contains_digit == True:
		new_word = input('Give a word: ')
		for char in new_word:
			if char.isdigit():
				word_contains_digit = True
				print("Try again, I cannot accept words with numbers in it")
			else:
				save_word = new_word.lower()
				word_contains_digit = False

    #this section tests the class before saving it
	class_contains_digit = True
	while class_contains_digit == True:
		new_word_class = input('Give the class of the word: ')
		for char in new_word_class:
			if char.isdigit():
				class_contains_digit = True
				print("Try again, classes cannot have numbers")
			else:
				save_class = new_word_class.lower()
				class_contains_digit = False

	#Now add the word and class to my dictionary
	my_dict.update({save_word : save_class})
	print(my_dict)

	add_more_words = input('Do you want to add more words? (y/n): ')

keep_searching = 'y'

while keep_searching == 'y' or keep_searching =='Y': 

	find_word = input('What word are you looking for?, I will tell you the class it belongs to. ')

	class_word = my_dict.get(find_word, None)

	if class_word != None: 
		print(f"I searched for '{find_word}', it belongs to the class: '{class_word}'")
	else:
		print(f'The word you requested is not registered in the dictionary, try another word')

	keep_searching = input('Do you want to search more words? (y/n): ')


print('Program terminated, have a good day!')
