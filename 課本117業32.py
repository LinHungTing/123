vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
word = input("Enter word to translate: ")
#if the 1st letter of a word is "aeiou", add "way" to the end of the word 
if word[0] in vowels:
    print(word + "way")

elif word[0] and word[1] in consonants:  
    print(word[2:] + word[0:2] + "ay") 

else:
    print(word[1:] + word[0] + 'ay')
    
    
    
    
    
    
   # 呂惠新wrong的
    word = str(input("Enter word to translate:"))
    if word[0] == "a" or "e"or "i" or "o" or "u":
        print(word + "way") 
    elif word[:2] == "ch" or "sh":
        word = word[2:] + word[:2]
        print(word + "ay")
    else:
        word = word[1:] + word[:1]
        print(word + "ay")
        