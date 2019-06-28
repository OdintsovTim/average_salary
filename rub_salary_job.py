import json

import requests

from count_salary import predict_salary


def predict_rub_salary_job(lang, TOKEN):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    more_page = True
    all_salaries = []
    params = {
        'keyword' : f'программист {lang}',
        'town' : 'москва',
        'page' : 0
    }
    headers = {
        'X-Api-App-Id': TOKEN
    }
    
    while more_page:
        response = requests.get(url, headers=headers, params=params).json()
        more_page = response['more']
        params['page'] += 1

        all_salaries += get_salaries_for_superjob(response)
    
    vacancies_found = response['total']
    return {
        'vacancies_found' : vacancies_found,
        'vacancies_processed' : len(all_salaries),
        'average_salary' : sum(all_salaries) // len(all_salaries) if len(all_salaries) != 0 else 0
    }


def get_salaries_for_superjob(response):
    salaries = [predict_salary(vacancy['payment_from'], vacancy['payment_to'], vacancy['currency']) for vacancy in response['objects']]
    filtered_salaries = [salary for salary in salaries if salary is not None]
    
    return filtered_salaries