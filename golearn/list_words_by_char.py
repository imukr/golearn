def get_dict_words(text):
    word_list = text.split(' ')
    word_dict = {}
    for i in word_list:
        word = word_dict.get(i[0])
        if word:
            word.append(i)
        else:
            word_dict[i[0]]=[i]
    print (word_dict)


get_dict_words('''есплатный онлайн-переводчик усовершенствован с помощью словарных определений, примеров произношения и синонимов.
Он поддерживает 19 языков, наиболее часто''')
