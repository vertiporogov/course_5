from requests import get
import json


def get_info_company(id_company) -> str:

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


def get_info_vacancy(vacancy_url) -> str:

    vacancy_list = []

    hh_api = vacancy_url
    response = get(hh_api)
    vacancy = json.loads(response.content.decode())

    for i in vacancy['items']:
        vacancy_dict = {
            'vacancy_id': i['id'],
            'vacancy_name': i['name'],
            'salary': i['salary']
                        }
        vacancy_list.append(vacancy_dict)

    return vacancy_list

# for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=2104700')['items']:
#     print(i)
#     print('*' * 100)

# print(get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1740'))

for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1740'):
    print(i)
    print('*' * 100)

# for i in get_info()['items']:
#     print(i)
#     print('*' * 100)

