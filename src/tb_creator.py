import psycopg2


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о работадателях  и вакансиях."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
                    employer_id INT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    open_vacancies INT,
                    area VARCHAR(100),
                    url VARCHAR
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
          CREATE TABLE vacancies (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR NOT NULL,
                    employer_id INT REFERENCES employers(employer_id),
                    area VARCHAR(50),
                    salary_from INT,
                    salary_to INT,
                    salary_currency VARCHAR(5),
                    url VARCHAR,
                    requirement TEXT,
                    responsibility TEXT
            )
        """)
    print("База данных и таблицы созданы")
    conn.commit()
    conn.close()