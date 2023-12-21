def count_str(str_1,str_2):
    len_1 = len(tokens_1)
    len_2 = len(tokens_2)
    j = 0
    counter = 0
    while(j < len_1):
        if(tokens_1[j] == tokens_2[0]):
            if(tokens_1[j : j + len_2] == tokens_2):
                counter += 1
        j += 1
    return counter

str_1 = str(input())
str_2 = str(input())
tokens_1 = list(str_1)
tokens_2 = list(str_2)

count_str(tokens_1, tokens_2)


