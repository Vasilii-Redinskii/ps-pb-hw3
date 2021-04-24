#The function determines which form matches the number
def get_form_word (number):
    
    form_word = 0
    fnumber2 = [2,3,4]
    fnumber3 = [5,6,7,8,9,0]
    
    #determines teens to form 3 
    if len(number)>1 and int(number[-2])==1:
        form_word = 2
    #determines form 2
    elif int(number[-1]) in fnumber2:
        form_word = 1
    #determines form 2    
    elif int(number[-1]) in fnumber3:
        form_word = 3
    #determines form 1    
    else: form_word = 0
    
    return form_word


word_list = []

number = input ('Введите целое число: ')
# check numeric
if number.isnumeric():
    #input forms of word
    for i in range(1, 4):
        word_list.append({'Form': i, 'Fword': input(f'Введите форму слова {i}: ')})
    #print result
    print(f'{number} {word_list [get_form_word(number)].get("Fword")}')

else:  print('Вы ввели неверное число.')
