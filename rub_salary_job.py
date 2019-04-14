import json

import requests

from count_salary import count_avarage_salary


def predict_rub_salary_job(lang, TOKEN):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    next_page = True
    sum_salary = 0
    vacancies_processed = 1
    params = {
        'keyword' : f'программист {lang}',
        'town' : 'москва',
        'page' : 0
    }
    headers = {
        'X-Api-App-Id': TOKEN
    }
    
    while next_page == True:
        response = requests.get(url, headers=headers, params=params).json()
        next_page = response['more']
        if next_page:
            params['page'] += 1

        vacancies_processed, sum_salary = count_avarage_salary(response, 'job', vacancies_processed, sum_salary)
    
    vacancies_found = response['total']
    return {
        'vacancies_found' : vacancies_found,
        'vacancies_processed' : vacancies_processed - 1,
        'average_salary' : sum_salary // vacancies_processed
    }