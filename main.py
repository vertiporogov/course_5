from typing import List, Dict, Any

from requests import get
import json

company_id = [
    1413874,   # Булочные Ф. Вольчека
    1221656,   # НЭМО
]


def get_info_company(id_company) -> dict[str, Any]:

    hh_api = f"https://api.hh.ru/employers/{id_company}"
    response = get(hh_api)
    company = json.loads(response.content.decode())
    company_dict = {
        'company_id': company['id'],
        'company_name': company['name'],
        'company_url': company['alternate_url'],
        'vacncies_url': company['vacancies_url']
                    }

    return company_dict


def h(dd):
    hh_api = dd
    response = get(hh_api)
    vacancy = json.loads(response.content.decode())
    return vacancy


def get_info_vacancy(vacancy_url) -> list[dict[str, Any]]:

    vacancy_list = []

    hh_api = vacancy_url
    response = get(hh_api)
    vacancy = json.loads(response.content.decode())

    for i in vacancy['items']:

        if i['salary'] is None:
            vacancy_dict = {
                'vacancy_id': i['id'],
                'vacancy_name': i['name'],
                'salary': 0,
                'area': i['area']['name']
                            }
            vacancy_list.append(vacancy_dict)

        else:
            if i['salary']['from'] is None:
                vacancy_dict = {
                    'vacancy_id': i['id'],
                    'vacancy_name': i['name'],
                    'salary': 0,
                    'area': i['area']['name']
                                }
                vacancy_list.append(vacancy_dict)

            else:
                if i['salary']['currency'] == 'RUR':
                    vacancy_dict = {
                        'vacancy_id': i['id'],
                        'vacancy_name': i['name'],
                        'salary': i['salary']['from'],
                        'area': i['area']['name']
                    }
                    vacancy_list.append(vacancy_dict)

    return vacancy_list

# for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=2104700')['items']:
#     print(i)
#     print('*' * 100)

# print(get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1740'))

# print(h('https://api.hh.ru/vacancies?employer_id=1740'))
# for i in h('https://api.hh.ru/vacancies?employer_id=1740')['items']:
#     print(i)
#     print(' ')
#     print('*' * 100)
#     print(' ')


for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1740'):

    print(i)
    print(' ')
    print('*' * 100)
    print(' ')

# for i in get_info()['items']:
#     print(i)
#     print('*' * 100)
