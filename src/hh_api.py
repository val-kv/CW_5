import requests

from db_manager import DBManager

HH_API_URL = 'https://api.hh.ru/vacancies'
DB_HOST = 'localhost'
DB_NAME = 'your_db_name'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'

db_manager = DBManager(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
db_manager.create_tables()

employers = ['Company1', 'Company2', 'Company3', 'Company4', 'Company5', 'Company6', 'Company7', 'Company8', 'Company9',
             'Company10']

for employer in employers:
    employer_id = db_manager.insert_employer(employer)
    params = {
        'text': '',
        'employer_id': employer_id
    }
response = requests.get(HH_API_URL, params=params)
vacancies = response.json()['items']
for vacancy in vacancies:
    db_manager.insert_vacancy(vacancy['name'], employer_id)
db_manager.close()