def fizz_buzz(start_i, finish_i):
    #check interval and calculate sum
    if start_i <= finish_i:
        x = 0
        for i in range(start_i, finish_i+1):
            if i % 3 == 0 and i % 5 == 0:
                x += i
    else: x =0

    return x


#The function determines which form matches the number
def plural_form (int_number,form1,form2,form3):
    
    form_word = form1
    fnumber2 = [2,3,4]
    fnumber3 = [5,6,7,8,9,0]
    
    number=str(int_number)
    #determines teens to form 3 
    if len(number)>1 and int(number[-2])==1:
        form_word = form2
    #determines form 2
    elif int(number[-1]) in fnumber2:
        form_word = form1
    #determines form 2    
    elif int(number[-1]) in fnumber3:
        form_word = form3
    #determines form 1    
    else: form_word = form1
    
    return form_word


print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))

print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))