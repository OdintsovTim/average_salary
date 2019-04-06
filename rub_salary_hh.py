import json

import requests

def count_vacancies_hh(lang):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text' : 'Программист' + ' ' + lang,
        'area' : 1,
        'period' : 30
    }

    response = requests.get(url, params=params).json()
    count = response['found']
    return {
        'vacancies_found' : count
    }

def predict_rub_salary_hh(lang):
    url = 'https://api.hh.ru/vacancies'
    count_vacancies = 0
    sum_salary = 0
    pages_number = 0
    params = {
        'text' : 'Программист' + ' ' + lang,
        'area' : 1,
        'period' : 30,
        'only_with_salary' : 'True',
        'page' : 0
    }
    
    while params['page'] <= pages_number:
        response = requests.get(url, params=params)
        params['page'] += 1
        pages_number = response.json()['pages']
        
        for vacancy in response.json()['items']:
            if vacancy['salary']['currency'] == 'RUR':
                count_vacancies += 1
                if vacancy['salary']['to'] is None:
                    sum_salary += int(vacancy['salary']['from'] * 1.2)
                elif vacancy['salary']['from'] is None:
                    sum_salary += int(vacancy['salary']['to'] * 0.8)
                else:
                    sum_salary += int(vacancy['salary']['from'] + int(vacancy['salary']['to']) / 2)
        
    return {
        'vacancies_processed' :  count_vacancies,
        'average_salary' : sum_salary // count_vacancies
    }