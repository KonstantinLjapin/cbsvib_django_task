
# **Basic Features**
1. Проект и приложение на Django Rest Framework >= 3.12 (Django > =3.2).
2. Хранение номера телефона пользователя.
3. Email и пароль при создании и авторизации пользователя.
4. JWT Token для аутентификации пользователя.
5. Модель Организации со следующими полями: title, description, address, postcode.
6. Модель Мероприятия со следующими полями: title, description, organizations, image, date.
7. Запуск проекта Docker-compose

# **Quick Start**
### Linux(Debian), docker compose (version v2.21.0)
#### Клонируете ветку мастер проекта локально, по образцу .env.dist(введены переменные для примера) создаётся .env . 
#### Проект готов к запуску.

**Выполните эти команды для запуска** 
- $ sudo chmod +x test_start.sh
- $ ./test_start.sh

###  Open endpoint in browser or Postman.
#### -http://localhost:8000
#### -http://localhost:8000/orgcre/ #Создание организации