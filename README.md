# EngGeo

####Резюме за 3 дня: <br>
Задачу не выполнили <br>
Дофигачивать пришлось мне самому, что меня не порадовало. <br>
Какие проблемы есть: <br>
1. Отсутствие понимания технологий контроля версий
2. Сложности с локальной разработкой
3. Не умение сводить работу воедино

## Маша
####Favicon
http://habrahabr.ru/post/260777/
Нарисовать и установить в html
####Лендинг 
C текущим дизайном карты у меня плохо согласуется.
Если у тебя ок - то готовь финальную версию. В вс утром, дизайн должен быть у меня на руках в законченном состоянии
####Реструктуризация
Вынести файл https://github.com/AxeInPeace/ngspro/tree/master/scrsht в https://github.com/AxeInPeace/ngspro/wiki на отдельную страницу. Никаких html. https://help.github.com/articles/adding-images-to-wikis/ Активно пользуемся якорями #
####Ajax авторизация и регистрация.
В файле lib/auth/views.py есть логика авторизации с сообщениями.<br>
В папке tpl/inc/ есть reg_form.html и auth_form.html.
Нужно:
1. сделать так, чтобы после регистрации/авторизации появляся исчезали кнопки и появлялся профиль пользователя
2. Корректная обработка ошибок
####Главная страница
Либо делаем боковое меню<br>
Либо переделываем текущее. Выезжать должно плавно примерно 0.5 секунды. Не должно появляться скролов.
В навбаре надо писать Имя пользователя (Где думаешь сама)<br>
Мне не нравится, что полосочки вызывающие меню справа от лого.

## Паша
0. Все шаблоны должны лежать в папка соответствующих по названию приложениям, которые их используют
1. Делаем базовый шаблон, в заголовках объявляем все общие скрипты(bootstrap, jquery)
2. От базового шаблона наследуем все страницы. Соответственно переделываем tpl/index.html
3. inc не трогаем
4. Максимально раскладываем код из index.html по отдельным файлам в inc/
5. Доделки по админке?
6. Разобраться с urls.py
7. Сервер-сайд добавления материалов пользователем
8. Прикрутить аватарки пользователям
