import psycopg2


def save_data_to_db(data1: list, data2: list, database_name: str, params: dict):
    """Сохранение данных о каналах и видео в базу данных."""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for employer in data1:
            cur.execute(
                """
                INSERT INTO employers (employer_id, name, open_vacancies, area, url)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING employer_id
                """,
                (employer.employer_id, employer.name, employer.open_vacancies,
                 employer.area, employer.url))
        employer.employer_id = cur.fetchone()[0]
        for vacancie in data2:
            cur.execute(
                """
                INSERT INTO vacancies (name, employer_id, area, salary_from, salary_to,
                salary_currency, url, requirement, responsibility)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (vacancie.name, vacancie.employer_id, vacancie.area, vacancie.salary_from,
                 vacancie.salary_to, vacancie.currency, vacancie.url,
                 vacancie.requirement, vacancie.responsibility)
            )
    print("Данные загружены в таблицы")
    conn.commit()
    conn.close()
