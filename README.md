# fisha_map

Интерактивная карта интересных мест Москвы. Создано на Django.
 
## Как установить

1. Клонируйте репозиторий
1. Создайте виртуальное окружение в корневом каталоге проекта и установите необходимые библиотеки:
    ```console
    python3 -m venv venv
    . venv/bin/activate
    python -m pip install -r requirements.txt
    ```
1. Создайте `.env` файл по образцу `.env.sample`
1. Для подключения БД заполните необходимые переменные в `.env`

## Как пользоваться

### При разработке
Получите БД с тестовыми данными.
Для запуска сервера для разработки запустите команду:
```commandline
python manage.py runserver
```
[Сайт](http://127.0.0.1:8000/) и [админка](http://127.0.0.1:8000/admin/) станут доступны на локалхосте.


### Для продакшена
Настройте веб-сервер согласно документации к выбранному серверу.
Обратите внимание на настройку статики и медиа.

## О проекте
Это учебный проект для школы Python-разработчиков [dvmn.org](https://dvmn.org).
