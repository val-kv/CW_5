from dataclasses import dataclass


@dataclass
class Employer:
    employer_id: int
    name: str
    open_vacancies: int
    area: str
    url: str

    def __str__(self) -> str:
        """
        Возвращает строковое представление работодателя
        """
        return (
            f"ID: {self.employer_id},\n"
            f"Name: {self.name},\n"
            f"Open Vacancies: {self.open_vacancies},\n"
            f"Area: {self.area},\n"
            f"URL: {self.url}\n"
        )


@dataclass
class Vacancy:
    name: str
    employer_id: int
    area: str
    salary_from: int
    salary_to: int
    currency: str
    url: str
    requirement: str
    responsibility: str

    def __str__(self) -> str:
        """
        Возвращает строковое представление вакансии.
        """
        return (
            f'Vacancy: {self.name}\n'
            f'Salary: {self.salary_from} {self.currency} - {self.salary_to} {self.currency} \n '
            f'requirement: {self.requirement}\n'
            f'URL: {self.url}\n'
        )

    def __repr__(self) -> str:
        """
        Возвращает строковое представление вакансии для отладки
        """
        return (
            f'Vacancy={self.name},\n'
            f'url={self.url},\n'
            f'salary_from={self.salary_from} {self.currency}, \n'
            f'salary_to={self.salary_to} {self.currency}, \n'
            f'requirement={self.requirement})\n'
        )
