import time
import webbrowser


def show(urls, interval):
    for url in urls:
        webbrowser.open(url)
        time.sleep(interval)


urls = []
for i in range(4):
    urls.append(input(f'url{i+1}: '))
interval = int(input('интервал в секундах: '))
show(urls, interval)

# https://dzen.ru
# https://www.google.ru
# https://vk.com/feed
# https://www.youtube.com
