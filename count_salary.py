def predict_salary(salary_from, salary_to, currency):
    if currency not in ('RUR', 'rub'):
        return
    
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)

    if salary_to and not salary_from:
        return int(salary_to * 0.8)
    
    if salary_from and not salary_to:
        return int(salary_from * 1.2)