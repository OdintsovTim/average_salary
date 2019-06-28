import json

import requests

from count_salary import predict_salary


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

def get_salaries_total_for_hh(lang, moscow_id):
    url = 'https://api.hh.ru/vacancies'
    all_salaries = []
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
        
        all_salaries += get_salaries_for_hh(response)

        
    return {
        'vacancies_processed' :  len(all_salaries),
        'average_salary' : sum(all_salaries) // len(all_salaries)
    }


def get_salaries_for_hh(response):
    salaries = [predict_salary(vacancy['salary']['from'], vacancy['salary']['to'], vacancy['salary']['currency']) for vacancy in response['items']]
    filtered_salaries = [salary for salary in salaries if salary is not None]
    
    return filtered_salaries