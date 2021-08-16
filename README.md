![example workflow](https://github.com/PatimatN/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)
# Продуктовый помощник. Foodgram

## Описание
Проект **Продуктовый помощник** - это сайт, который позволяет пользователям публиковать и делиться рецептами, добавлять чужие рецепты в избранное и подписываться на публикации других авторов, а также автоматически создавать список продуктов, , которые нужно купить для приготовления выбранных блюд, и скачивать его.

## Установка
Проект содержит четыре образа:

* backend - образ бэкенда
* frontend - образ фронтенда
* postgres - образ базы данных PostgreSQL v 12.04
* nginx
* 
### Команда клонирования репозитория:
> git clone https://github.com/PatimatN/foodgram-project-react.git

### Запуск проекта:
* Установите Докер
* Выполните команду:
> docker pull pavelkhan/foodgram-project-react :latest
Первоначальная настройка Django:
- docker-compose exec web python manage.py migrate --noinput
- docker-compose exec web python manage.py collectstatic --no-input
Создание суперпользователя:
- docker-compose exec web python manage.py createsuperuser

