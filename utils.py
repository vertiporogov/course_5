from typing import Any

from requests import get
import json


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


def create_database()