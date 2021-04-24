def add_item_to_fib_list(fib_list):
    
    new_fib_list = []
    for element in fib_list:
        new_fib_list.append(element)
    new_item = new_fib_list[-1]+new_fib_list[-2]
    new_fib_list.append(new_item)
    return new_fib_list

list_fib = [1, 1]
count_odd = 0
sum_odd = 0
while list_fib[-1]<=10000000:
    if list_fib[-1] % 2 == 0:
        count_odd += 1
        sum_odd += list_fib[-1]
    list_fib_new = add_item_to_fib_list(list_fib)
    list_fib = list_fib_new
x=0
for i in range(1000,20000):
    if i % 3 == 0 and i % 5 == 0:
        x+=i

    
list_fib.remove(list_fib[-1])
len_list = len(list_fib)
print(list_fib[-2])
print(len_list)
print(count_odd)
print(x)
print(sum_odd)