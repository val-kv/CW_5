import psycopg2


class TBCreator:
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cur = self.conn.cursor()


def create_tables(self):
    self.cur.execute("""
    CREATE TABLE IF NOT EXISTS employers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    )
    """)
    self.cur.execute("""
    CREATE TABLE IF NOT EXISTS vacancies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    employer_id INT,
    FOREIGN KEY (employer_id) REFERENCES employers(id)
    )
    """)
    self.conn.commit()


def insert_employer(self, name):
    self.cur.execute("INSERT INTO employers (name) VALUES (%s) RETURNING id", (name,))
    employer_id = self.cur.fetchone()[0]
    self.conn.commit()
    return employer_id


def insert_vacancy(self, title, employer_id):
    self.cur.execute("INSERT INTO vacancies (title, employer_id) VALUES (%s, %s)", (title, employer_id))
    self.conn.commit()


def close(self):
    self.cur.close()
    self.conn.close()
