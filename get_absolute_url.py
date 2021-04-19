def get_absolute_url (url, *args, **kwargs):
    # add url to list
    absolute_url = [url]
    # add "/" to args
    for i in args:
        i="/"+i
        absolute_url.append(i)
    #add "?" to list  
    absolute_url.append('?') 
    #add kwargs to list
    for k, v in kwargs.items():
        absolute_url.append(f'{k}={v}')
        absolute_url.append('&')
    
    return ''.join(absolute_url[:-1])

print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))
