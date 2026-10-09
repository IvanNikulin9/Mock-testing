import requests ### - нужна, чтобы отправлять HTTP-запросы

def get_joke():
    url = 'https://api.chucknorris.io/jokes/random' ### - лежит адрес API
    response = requests.get(url) ### - получаем ответ

    if response.status_code == 200: ### - статус 200 - запрос успешен
        joke = response.json()['value'] ### - превращает тело ответа (JSON-строку) в Python-словарь и берёт значение по ключу 'value'.
    else:
        joke = 'No jokes'

    return joke

def len_joke():
    joke = get_joke()

    # print()
    # print('The joke from get_joke:', joke)
    # print()

    return len(joke)

if __name__ == '__main__':
    print(get_joke())