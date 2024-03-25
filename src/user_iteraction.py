import psycopg2


def search_vacancy_by_keyword(keyword):
    conn = psycopg2.connect('headhunter')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM vacancies WHERE title LIKE ?', ('%' + keyword + '%',))
    results = cursor.fetchall()

    conn.close()

    return results


def search_employer_by_name(name):
    conn = psycopg2.connect('headhunter')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM vacancies WHERE company = ?', (name,))
    results = cursor.fetchall()

    conn.close()

    return results


def user_iteraction():
    while True:
        print("Выберите действие:")
        print("1. Поиск вакансии по ключевому слову")
        print("2. Поиск работодателя по названию")
        print("3. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            keyword = input("Введите ключевое слово для поиска вакансии: ")
            results = search_vacancy_by_keyword(keyword)
            for result in results:
                print(result)

        elif choice == '2':
            name = input("Введите название работодателя для поиска: ")
            results = search_employer_by_name(name)
            for result in results:
                print(result)

        elif choice == '3':
            print("До свидания!")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")
