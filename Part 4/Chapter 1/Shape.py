def shape(number_1 , word_1,number_2,word_2) :
  for i in range(1, number_1+1, 1):
    print(word_1 * i)
    

for y in range(number_2) :
    print(word_2 * number_1)

shape(int(input("Please type in a number: ")),str(input("Please type in a word: ")),int(input("Please type in a number: ")),str(input("Please type in a word: ")))
