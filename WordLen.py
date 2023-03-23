def shortest_word(s):
    if (s.endswith('.')):
        s=s.replace('.','')

        # print(s.split(' '),type(s.split(' ')))
    arr =s.split(' ')
    current_word=''
    current_len=0
    first_loop=True
    for word in arr:
        # print(word,len(word))
        if first_loop:
            # print(word)
            current_len=len(word)
            current_word=word
            # print(current_word,current_len)
            first_loop=False
        else:
            if current_len<= len(word):
                # print(current_word,current_len)
                continue
            else:
                current_len=len(word)
                current_word=word

    return(current_word,current_len)

sw=shortest_word('html nd i css C# a JAVA js php.')
print(sw)