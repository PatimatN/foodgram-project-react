![example workflow](https://github.com/PatimatN/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)  

Проект развернут по адресу http://84.252.139.205/
# Продуктовый помощник. Foodgram

## Описание
Проект **Продуктовый помощник** - это сайт, который позволяет пользователям публиковать и делиться рецептами, добавлять чужие рецепты в избранное и подписываться на публикации других авторов, а также автоматически создавать список продуктов, , которые нужно купить для приготовления выбранных блюд, и скачивать его.

## Установка
Проект содержит четыре образа:

* backend - образ бэкенда
* frontend - образ фронтенда
* postgres - образ базы данных PostgreSQL v 12.04
* nginx

### Команда клонирования репозитория:
```
git clone https://github.com/PatimatN/foodgram-project-react.git
```

### Заполнение .env:
Чтобы добавить переменную в .env необходимо открыть файл .env в корневой директории проекта и поместить туда переменную в формате имя_переменной=значение. Пример .env файла:

```
DB_ENGINE=my_db 
DB_NAME=db_name 
POSTGRES_USER=my_user 
POSTGRES_PASSWORD=my_pass 
DB_HOST=db_host 
DB_PORT=db_port
```

### Запуск проекта:
* Установите Докер
* Перейдите в папку в проекте *infra/*
* Выполните команду:
```
docker-compose up -d --build
```

### Первоначальная настройка Django:
```
- docker-compose exec backend python manage.py migrate --noinput
- docker-compose exec backend python manage.py collectstatic --no-input
```
### Создание суперпользователя:
```
- docker-compose exec backend python manage.py createsuperuser
```

## После каждого обновления репозитория (git push) происходит следующее:
* Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
* Сборка и доставка докер-образов на Docker Hub
* Автоматический деплой
* Отправка уведомления в Telegram

## Данные для входа
### Суперпользователь
**email**: admin@admin.ru  
**password**: admin  

### Тестовый пользователь
**email**: umar@yandex.ru  
**password**: MyPass111  
