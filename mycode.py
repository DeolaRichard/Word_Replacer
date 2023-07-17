def replace_word():

    str = 'Hello, how are you doing today. Hello'
    word_to_replace = input("Enter word you want to replace")
    word_replacement = input("Enter the new word")
    print(str.replace(word_to_replace, word_replacement))

replace_word()
