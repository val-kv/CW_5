import psycopg2
from config import config


class DBManager:
    """
    Класс DBManager, который подключаетя к БДPostgreSQL и имеет следующие
    методы:
    """

    def __init__(self, database_name, params=config()):
        self.database_name = database_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT  e.name, COUNT(vacancies.id) AS vacancy_count 
                FROM employers e
                JOIN vacancies USING (employer_id)
                GROUP BY e.employer_id;
                """)

            data = cur.fetchall()
        conn.close()
        print("Список компаний и количество вакансий в компаниях:")
        for row in data:
            print(f"{row[0]} - {row[1]}")

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию.
        """
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT employers.name, v.name, salary_from,salary_to,v.url 
                FROM vacancies v
                JOIN employers  USING (employer_id);
                """)

            data = cur.fetchall()
        conn.close()
        print("Список всех вакансий с указанием названия компании,"
              "вакансии, зарплаты и ссылки на вакансию:")
        for row in data:
            print(f"{row[0]} - {row[1]} - Зарплата от: {row[2]} руб. - Зарплата до:{row[3]} руб. - Ссылка: {row[4]}")

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по компаниям.
        """
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT employers.name, ROUND(AVG((salary_to + salary_from)/2)) as average_salary
                FROM vacancies v
                JOIN employers USING (employer_id)
                GROUP BY employers.employer_id;
                """)

            data = cur.fetchall()
        conn.close()
        print("Cредняя зарплата по вакансиям:")
        for row in data:
            print(f"{row[0]} - {row[1]} руб.")

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата
        выше средней по всем вакансиям.
        """
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """
                 SELECT employers.name, v.name, v.area, v.url FROM vacancies v
                 JOIN employers USING (employer_id)
                 WHERE (salary_to + salary_from)/2 > (SELECT ROUND(AVG((salary_to + salary_from)/2)) FROM vacancies);
                """)

            data = cur.fetchall()
        conn.close()
        print("Cписок всех вакансий, у которых зарплата выше средней по всем вакансиям:")
        for row in data:
            print(f"{row[0]} - {row[1]} - Город: {row[2]} - Ссылка: {row[3]}")

    def get_vacancies_with_keyword(self):
        """
        Получает список всех вакансий, в названии которых содержатся
        переданные в метод слова, например python.

        """
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        keyword = input("Введите слово для поиска, например разработчик или python и нажмите Enter\n")
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT employers.name, v.name, v.area, v.url FROM vacancies v
            JOIN employers USING (employer_id)
            WHERE v.name LIKE '%{keyword}%' OR v.requirement LIKE '%{keyword}%'
            OR v.responsibility LIKE '%{keyword}%';
            """)

            data = cur.fetchall()
        conn.close()
        print("Список компаний и вакансий с заданным словом:")
        for row in data:
            print(f"{row[0]} - {row[1]} - Город:  {row[2]} - Ссылка: {row[3]}")
