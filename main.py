from utils import get_info_company, get_info_vacancy, h

company_id = [
    1413874,  # Булочные Ф. Вольчека
    1221656,  # НЭМО
]

def main():
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

    # for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1413874'):
    #     print(i)
    #     print(' ')
    #     print('*' * 100)
    #     print(' ')
    print(get_info_company('1740'))
    # for i in get_info_company('1740'):
    #     print(i)
    #     print('*' * 100)


if __name__ == '__main__':
    main()