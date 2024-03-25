import psycopg2


class DBManager:
    def __init__(self, dbname='headhunter', user='val_k', password='1986', host='localhost', port='5432'):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()

    def insert_employer(self, employer):
        pass

    def insert_vacancy(self, param, employer_id):
        pass

    def create_tables(self):
        pass


def get_companies_and_vacancies_count(self):
    query = """
    SELECT company_name, COUNT(*)
    FROM vacancies
    GROUP BY company_name
    """
    self.cur.execute(query)
    return self.cur.fetchall()


def get_all_vacancies(self):
    query = """
    SELECT company_name, vacancy_title, salary, vacancy_link
    FROM vacancies
    """
    self.cur.execute(query)
    return self.cur.fetchall()


def get_avg_salary(self):
    query = """
    SELECT AVG(salary)
    FROM vacancies
    """
    self.cur.execute(query)
    return self.cur.fetchone()[0]


def get_vacancies_with_higher_salary(self):
    avg_salary = self.get_avg_salary()
    query = f"""
    SELECT company_name, vacancy_title, salary, vacancy_link
    FROM vacancies
    WHERE salary > {avg_salary}
    """
    self.cur.execute(query)
    return self.cur.fetchall()


def get_vacancies_with_keyword(self, keyword):
    query = f"""
    SELECT company_name, vacancy_title, salary, vacancy_link
    FROM vacancies
    WHERE vacancy_title ILIKE '%{keyword}%'
    """
    self.cur.execute(query)
    return self.cur.fetchall()


def close_connection(self):
    self.cur.close()
    self.conn.close()
