obj = {}
def read_text():
    with open('6madlibstext.txt', 'r') as f:
        text = f.read()
        return text

text = read_text()

words = set()
start_of_word = -1
for i, char in enumerate(text):
    if char =="<":
        start_of_word = i
    if char == ">" and start_of_word != -1:
        word = text[start_of_word: i+1]
        words.add(word)
        start_of_word=-1

    
for word in words:
    answer = input("Write your answer for "+ word) 
    obj[word] = answer

for word in words:
    text = text.replace(word, obj[word])

print(text)