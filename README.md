## Sprint_5

### Тестирование сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

### Технологии
- Pytest
- Selenium

### Реализованные тесты

#### Регистрация (test_registration.py)

- Позитивная проверка регистрации (test_registration_positive)
- Негативная проверка ошибки некорректного пароля (test_registration_negative_password)

#### Вход (test_sign_in.py)

- Проверка входа по кнопке "Войти" на главноей странице (test_sign_in_on_main_page)
- Проверка входа по кнопке "Личный кабинет" (test_sign_in_from_personal_account)
- Проверка входа по кнопке "Войти" в форме регистрации (test_sign_in_from_register)
- Проверка входа по кнопке "Войти" в форме восстановления пароля (test_sign_in_from_reset_password)

#### Выход (test_sign_out.py)

- Проверка выхода из аккаунта (test_sign_out)

#### Переход в личный кабинет (test_go_to_personal_account.py)

- Проверка перехода в личный кабинет (test_go_to_personal_account)

#### Переход в конструктор (test_go_to_personal_account.py)

- Проверка перехода кликом по "Конструктор" (test_go_from_personal_account_to_constructor)
- Провекра перехода по логотипу (test_go_from_personal_account_to_constructor_by_logo)

#### Секция Конструктор (test_constructor.py)

- Проверка перехода в раздел "Булки" (test_constructor_buns)
- Проверка перехода в раздел "Соусы" (test_constructor_sauces)
- Проверка перехода в раздел "Начинки" (test_constructor_fillings)