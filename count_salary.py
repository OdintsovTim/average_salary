def count_sum_salary_hh(response, vacancies_processed, sum_salary):
    correct_response = []
    hh_params = {'from': 'from', 'to': 'to'}
    response = response['items']
    for vacancy in response:
        correct_response.append(vacancy['salary'])

    return count_sum_salary(correct_response, hh_params, vacancies_processed, sum_salary)


def count_sum_salary_job(response, vacancies_processed, sum_salary):
    job_params = {'from' : 'payment_from', 'to' : 'payment_to'}
    response = response['objects']

    return count_sum_salary(response, job_params, vacancies_processed, sum_salary)


def count_sum_salary(response, site_params, vacancies_processed, sum_salary):
    for vacancy in response:
        if vacancy['currency'] == 'RUR' or vacancy['currency'] == 'rub':
                vacancies_processed += 1
                if not vacancy[site_params['from']]:
                    sum_salary += int(vacancy[site_params['to']] * 0.8)
                elif not vacancy[site_params['to']]:
                    sum_salary += int(vacancy[site_params['from']] * 1.2)
                else:
                    sum_salary += int((vacancy[site_params['from']] + vacancy[site_params['to']]) / 2)
    
    return vacancies_processed, sum_salary
