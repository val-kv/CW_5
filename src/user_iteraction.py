from config import config
from tb_creator import create_database
from hh_api import HeadHunterAPI
from save_data import save_data_to_db
from src.db_manager import DBManager


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    input(f"""Привет. Я - программа  которая получает данные о компаниях и вакансиях с сайта hh.ru,
создает таблицы в БД PostgreSQL и загружает полученные данные в созданные таблицы.
Для продолжения нажми Enter""")
    params = config()
    create_database('hhcollector', params)  # Создает БД и таблицы
    companies = HeadHunterAPI.get_companies()  # Загружает с НН информацию о компаниях
    vacancies = HeadHunterAPI.get_vacancies()  # Загружает с НН информацию о вакансиях в выбранных компаниях
    save_data_to_db(companies, vacancies, 'hhcollector', params)  # Загружает информацию в таблицы БД
    db_manager = DBManager('hhcollector', params)  # Получение заданных результатов из БД
    i = "1"
    while i in ["1", "2", "3", "4", "5"]:
        i = input(f"""\nВведите номер действия. Для выхода из программы нажмите Enter
1. Список компаний и количество вакансий в компаниях
2. Список вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию
3. Cредняя зарплата по вакансиям
4. Cписок вакансий, у которых зарплата выше средней по всем вакансиям                 
5. Cписок вакансий в которых содержатся ключевые слова\n""")
        if i == "1":
            db_manager.get_companies_and_vacancies_count()
        elif i == "2":
            db_manager.get_all_vacancies()
        elif i == "3":
            db_manager.get_avg_salary()
        elif i == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif i == "5":
            db_manager.get_vacancies_with_keyword()
        else:
            break
    print("До свидания!")
