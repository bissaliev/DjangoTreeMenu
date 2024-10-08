# DjangoTreeMenu

## Описание

Проект реализует древовидное меню, соблюдая следующие условия:

- Меню реализовано через `template tag`
- Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
- Хранится в БД.
- Редактируется в стандартной админке `Django`
- Активный пункт меню определяется исходя из URL текущей страницы
- Меню на одной странице может быть несколько. Они определяются по названию.
- При клике на меню происходит переход по заданному в нем URL.
- На отрисовку каждого меню требуется ровно 1 запрос к БД.

Проект позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию:

```django
{% draw_menu 'main_menu' %}
```

## Технологии

- `Python 3.10`
- `Django 5.1.1`

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:bissaliev/DjangoTreeMenu.git
cd DjangoTreeMenu/
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Перейти в директорию `tree_menu` и выполнить миграции:

```bash
python3 manage.py migrate
```

Запустить сервер разработчика:

```bash
python3 manage.py runserver
```

[Перейти на сайт](http://localhost:8000/)

### Автор

[Биссалиев Олег](https://github.com/bissaliev)
