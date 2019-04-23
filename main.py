import argparse

from terminaltables import AsciiTable

from rub_salary_hh import predict_rub_salary_hh, count_vacancies_hh
from rub_salary_job import predict_rub_salary_job

prog_langs = ['Python', 'JavaScript', 'Java', 'PHP', 'C++', 'C#', 'C', 'Go', 'Objective-C', 'Scala', 'Swift']
moscow_id = 1

def make_table(langs_info_dict, table_name):
    table_data_job = [[
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
    ]]

    for lang, values in langs_info_dict.items():
        table_data_job.append([
            lang,
            values['vacancies_found'],
            values['vacancies_processed'],
            values['average_salary']
        ])

    table = AsciiTable(table_data_job, table_name)

    return table.table


def main():

    parser = argparse.ArgumentParser(description='This program displays data on average salaries for popular programming languages from hh.ru and job.ry')
    parser.add_argument('TOKEN')
    args = parser.parse_args()
    TOKEN = args.TOKEN

    langs_info_hh = {}
    langs_info_job = {}

    for lang in prog_langs:
        langs_info_hh[lang] = {}
        langs_info_hh[lang]['vacancies_found'] = count_vacancies_hh(lang, moscow_id)
        langs_info_hh[lang].update(predict_rub_salary_hh(lang, moscow_id))

    print(make_table(langs_info_hh, 'HeadHunter Moscow'))

    for lang in prog_langs:
        langs_info_job[lang] = {}
        langs_info_job[lang].update(predict_rub_salary_job(lang, TOKEN))

    print(make_table(langs_info_job, 'SuperJob Moscow'))


if __name__ == "__main__":
    main()

