from clsUniversity import University

# создать объект базы данных
database_University = University()


# удаление по id спортсема
def delete_command(id):
    database_University.delete(id)
    print(f"Данные учителя  с id = {id} удалены")


# просмотр всех записей
def view_command():
    for row in database_University.view():
        print(row)


# основная программа
print("Список учителей")
view_command()

id_delete = int(input("Введите id учителей "))
delete_command(id_delete)

print("Список учителей")
view_command()
