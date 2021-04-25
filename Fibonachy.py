#Function makes list of fibonachy
def add_item_to_fib_list(fib_list):
    
    new_fib_list = []
    for element in fib_list:
        new_fib_list.append(element)
    new_item = new_fib_list[-1]+new_fib_list[-2]
    new_fib_list.append(new_item)
    return new_fib_list
# define first element in list of fibonachy
list_fib = [1, 1]
count_odd = []
sum_odd = 0
# check odd number and count and sum their
while list_fib[-1]<=10000000:
    if list_fib[-1] % 2 == 0:
        count_odd.append(list_fib[-1])
        sum_odd += list_fib[-1]
    list_fib_new = add_item_to_fib_list(list_fib)
    len_list = len(list_fib)
    list_fib = list_fib_new
#print results
print(len_list)
print(sum_odd)
print(count_odd)
print(list_fib[-2])
