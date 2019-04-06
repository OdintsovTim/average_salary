import json

import requests


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

        for vacancy in response['objects']:
            if vacancy['currency'] == 'rub':
                vacancies_processed += 1
                if vacancy['payment_from'] == 0:
                    sum_salary += int(vacancy['payment_to'] * 0.8)
                elif vacancy['payment_to'] == 0:
                    sum_salary += int(vacancy['payment_from'] * 1.2)
                else:
                    sum_salary += int((vacancy['payment_from'] + vacancy['payment_to']) / 2)
    
    vacancies_found = response['total']
    return {
        'vacancies_found' : vacancies_found,
        'vacancies_processed' : vacancies_processed - 1,
        'average_salary' : sum_salary // vacancies_processed
    }