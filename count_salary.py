def count_avarage_salary(response, site_name, vacancies_processed, sum_salary):
    hh_params = {'from': 'from', 'to': 'to'}
    job_params = {'from' : 'payment_from', 'to' : 'payment_to'}
    if site_name == 'hh':
        response = response['items']
        current_params = hh_params
    else:
        response = response['objects']
        current_params = job_params
    
    for vacancy in response:
        if site_name == 'hh':
            vacancy = vacancy['salary']

        if vacancy['currency'] == 'RUR' or vacancy['currency'] == 'rub':
            vacancies_processed += 1
            if not vacancy[current_params['from']]:
                sum_salary += int(vacancy[current_params['to']] * 0.8)
            elif not vacancy[current_params['to']]:
                sum_salary += int(vacancy[current_params['from']] * 1.2)
            else:
                sum_salary += int((vacancy[current_params['from']] + vacancy[current_params['to']]) / 2)

    return vacancies_processed, sum_salary