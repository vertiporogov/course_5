from requests import get
import json


def get_info():
    word = 'python'
    hh_api = "https://api.hh.ru/employers/15478"
    # params = {
    #     'text': f'NAME:{word}',
    #     'area': 2,  # Поиск в зоне
    #     'page': 0,
    #     'per_page': 100  # Кол-во вакансий на 1 странице
    # }
    response = get(hh_api)
    vacancies = json.loads(response.content.decode())

    return vacancies

print(get_info())

# for i in get_info()['items']:
#     print(i)
#     print('*' * 100)