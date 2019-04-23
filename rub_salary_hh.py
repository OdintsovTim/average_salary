import json

import requests

from count_salary import count_avarage_salary


def count_vacancies_hh(lang, moscow_id):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text' : f'программист {lang}',
        'area' : moscow_id,
        'period' : 30
    }

    response = requests.get(url, params=params).json()
    count = response['found']
    return count

def predict_rub_salary_hh(lang, moscow_id):
    url = 'https://api.hh.ru/vacancies'
    vacancies_processed = 0
    sum_salary = 0
    pages_number = 1
    params = {
        'text' : f'программист {lang}',
        'area' : moscow_id,
        'period' : 30,
        'only_with_salary' : 'True',
        'page' : 0
    }
    
    while params['page'] < pages_number:
        response = requests.get(url, params=params).json()
        params['page'] += 1
        pages_number = response['pages']
        
        vacancies_processed, sum_salary = count_avarage_salary(response, 'hh', vacancies_processed, sum_salary)

        
    return {
        'vacancies_processed' :  vacancies_processed,
        'average_salary' : sum_salary // vacancies_processed
    }