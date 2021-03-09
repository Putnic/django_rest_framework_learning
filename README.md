# Задание

## 1. Развернуть Django-приложение для сайта-каталога

### Модели и поля

1. Категории и подкатегории (вложенность неограниченна, но >2):  
   1.1. Название;  
   1.2. Внешний ID (уникальное);  
   1.3. Родитель;

2. Цвета:  
   1.1. Название (уникальное);  
   1.2. Внешний ID (уникальное);  
   1.3. hex-код (уникальное);

3. Товары:  
   1.1. Название;  
   1.2. Внешний ID (уникальное);  
   1.3. Цвет (отношение к модели Цветов);  
   1.4. Категория (отношение к модели Категории);  
   1.5. Цена

```bash
  python3 -m venv my-env

  pip install django djangorestframework celery[redis]
  # OR
  pip install -r requirements.txt
```

## 2. Написать Celery-таск для импорта каталога из JSON

JSON-фикстура каталога представлена в репозитории использовать её.
Ввиду особенностей JSON, кириллические и пробельные символы в названиях закодированы.
Для валидного отображения в каталоге их нужно декодировать.
(Можно использовать библиотеку `urllib` или любую другую)

This will create a json file which can be imported again by using

```bash
  python manage.py dumpdata catalog --format=json --indent=2 -o catalog/fixt ures/data_1.json

  ./manage.py dumpdata > databasedump.json # full database
  ./manage.py dumpdata myapp > databasedump.json # only 1 app
  ./manage.py dumpdata myapp.mymodel > databasedump.json # only 1 model (table)
```

load data from json

```bash
  manage.py loaddata <fixturename>

  ./manage.py loaddata databasedump.json
  python manage.py loaddata data_1.json --format=json
```

Removes all data from the database and re-executes any post-synchronization handlers.
python manage.py flush --noinput

## 3. Написать точку API для обзора категории (список товаров категории) и карточки товара

Для написания API используется Django Rest Framework.  
Обзор категории имеет следующую структуру данных:

1. Описание данных категории (название, pk, родительская категория, цена)
2. Карточка товара (название, pk, категория, цвет, цена)

## 4. Выложить проект на Github или Bitbucket в публичный репозиторий

```bash
  # run redis
  service redis-server restart

  # run celery
  celery -A site_catalog worker --pool=solo -l info
```
