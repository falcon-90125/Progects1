def get_absolute_url(url, *args, **kwargs):
    
    way = url
    for i in args:
        way += '/' + i
    way += '?'
    for k, v in kwargs.items():
        way += k + '=' + v + '&'
    way = way[:-1]
    return way

print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))



# Требуемый результат
# www.yandex.ru/posts/news?id=24&author=admin
# www.google.com/images?id=24&category=auto&color=red&size=small
