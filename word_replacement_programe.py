# Program that replace the existing word with new word.

def replace_word():
    
    string = "Hi guys, I am Junaid. Undergraduating software engineering."
    print("Original string:", string)
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    new_string = string.replace(word_to_replace, word_replacement)
    print("Modified string:", new_string)
        

replace_word()