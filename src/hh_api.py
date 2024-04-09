from configparser import ParsingError
import requests
import json
from src.data import Employer, Vacancy

COMPANIES = {"Яндекс": "1740",
             "СБЕР": "3529",
             "ПАО МТС": "3776",
             "SberTech": "906557",
             "Skillbox": "2863076",
             "Rambler&Co": "8620",
             "VK": "15478",
             "ozon": "2180",
             "fix_price": "196621",
             }


class HeadHunterAPI:
    """
    Класс получения данных  for HeadHunter API
    """

    #    def __init__(self):

    @staticmethod
    def get_vacancies():  # list
        """
        Функция для получения данных по вакансиям из компаний,
        перечисленных  в словаре COMPANIES
        :return:
        """
        api_url = "https://api.hh.ru/vacancies?employer_id="
        params = {
            "area": 113,
            "pages": 0,
            "per_page": 100,
            "only_with_vacancies": True,
            "only_with_salary": True
        }
        vacancies_list = []
        for company in COMPANIES.values():
            response = requests.get(f"{api_url}{company}", params=params)
            if response.status_code != 200:
                raise ParsingError(f"Error while trying to get Vacancies, Status: {response.status_code}")
            else:
                data = json.loads(response.text)['items']
                for vacancy in data:
                    if vacancy["snippet"]["requirement"] is None:
                        vacancy["snippet"]["requirement"] = "НЕТ"
                    if vacancy["snippet"]["responsibility"] is None:
                        vacancy["snippet"]["responsibility"] = "НЕТ"
                    if vacancy["salary"]["from"] is None:
                        vacancy["salary"]["from"] = 0
                    if vacancy["salary"]["to"] is None:
                        vacancy["salary"]["to"] = int(vacancy["salary"]["from"]) * 2
                    vacancies_list.append(
                        Vacancy(
                            name=vacancy['name'],
                            employer_id=vacancy['employer']['id'],
                            area=vacancy['area']['name'],
                            salary_from=vacancy["salary"]["from"],
                            salary_to=vacancy["salary"]["to"],
                            currency="RUB",
                            url=vacancy['alternate_url'],
                            requirement=vacancy["snippet"]["requirement"],
                            responsibility=vacancy["snippet"]["responsibility"]
                        )
                    )
        return vacancies_list

    @staticmethod
    def get_companies():  # list
        """
        Функция для получения данных по компаниям,
        перечисленных  в словаре COMPANIES
        """
        employer_list = []
        for company in COMPANIES.values():
            response = requests.get(f"https://api.hh.ru/employers/{company}")
            if response.status_code != 200:
                raise ParsingError(f"Error while trying to get Employer, Status: {response.status_code}")
            employer = json.loads(response.text)
            employer_list.append(
                Employer(
                    employer_id=(employer['id']),
                    name=employer['name'],
                    area=employer['area']['name'],
                    open_vacancies=employer['open_vacancies'],
                    url=employer['alternate_url']
                ))
        return employer_list
