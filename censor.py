text = "this hack is wack hack"
word = "hack"

text_list = text.split()

new_word = ""

for w in word:
	new_word += "*"

print new_word

for i in text_list:
	if i == word:
		word_index = int(text_list.index(i))
		text_list.pop(word_index)
		text_list.insert(word_index, new_word)
new_text =" ".join(str(x) for x in text_list)
print new_text