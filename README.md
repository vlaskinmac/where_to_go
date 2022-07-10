# [Куда сходить?](https://tesseractmaks.pythonanywhere.com/)

Это проект сайта-интерактивной карты. Он предназначен для размещения на нём "точек интереса" - локаций для досуга. Посетители сайта смогут найти поблизости от себя места интересные для посещения. 

Наполнение сайта ведется через интерфейс администрирования по адресу https://tesseractmaks.pythonanywhere.com/admin/

* Войдите в систему введя логин и пароль:

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](https://user-images.githubusercontent.com/78322994/177935966-4751c6eb-cd8f-4f4c-8a72-0f723346980c.png)

* Напротив пункта `Локации` нажмите кнопку `Добавить`
![](https://user-images.githubusercontent.com/78322994/177937112-1de1949f-b6ff-474d-8291-ea2f410c7436.png)

* Заполните поля описания локации, в "полном описании" можно использовать форматирование. Долгота и широта места указываются в градусах.
![](https://user-images.githubusercontent.com/78322994/177937549-c7a718fe-f773-419f-8569-eb8864bb4c07.png)


[Демка сайта](https://devmanorg.github.io/where-to-go-frontend/).

* Добавьте изображения локации. После добавления изображения можно сортировать путем перетаскивания мышкой.

![](https://user-images.githubusercontent.com/78322994/177937885-b78c4317-c81a-4bef-a6c3-1d0d608c902e.png)

## Как редактировать локации
В списке локаций доступен поиск по наименованию локации - найдите нужную. Перейдите в искомый объект. Вы сможете изменить поля описания локации, изменить порядок картинок путем перемещения их мышкой. Ненужную картинку можно удалить поставив соответствующий флажок и сохранив локацию.

## Административное добавление локаций
Для администратора, имеющего доступ к консоли сервера, существует консольная команда `load_place` для добавления локаций из json-файлов. Например:

```bash
python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json
```

Доступно множественное добавление ссылок (запятые между ссылками не ставить)

Файл с описанием локации должен иметь следующую структуру:

```
{
    "title": <Название локации>,
    "imgs": [
        <Cсылка на картинку>,
        ...
        <Cсылка на картинку>,
    ],
    "description_short": <Краткое описание локации>,
    "description_long": <Полное описание локации с HTML-форматированием>,
    "coordinates": {
        "lng": <Долгота в  градусах>,
        "lat": <Широта в градусах>
    }
}
```
Файлы с описаниями локаций для демо-сайта были получены по адресу https://github.com/devmanorg/where-to-go-places


### Установка проекта

Для работы проекта необходим установленный python3. Проект создан на фреймворке Django.

* Установите необходимые зависимости командой
```bash
pip install -r requirements.txt
```
* Создайте файл .env. В нем будут расположены параметры фреймворка:

* Обязательные параметры (в примере указаны значения по-умолчанию):

`SECRET_KEY = 'secret_key'`

`DATABASE_URL = sqlite:////home/user/project/db.sqlite3` 

`DEBUG = False`

`ALLOWED_HOSTS = 'localhost', '127.0.0.1'`

`STATIC_URL = '/static/'`

`STATIC_ROOT = 'static/'`

`MEDIA_URL = '/media/'`

`MEDIA_ROOT = 'media/'`

`LANGUAGE_CODE = 'en-us'`

`USE_I18N = True`

`USE_TZ = True`

`TIME_ZONE = 'UTC'`


* Создайте базу данных

```bash
python3 manage.py migrate
```
* Создайте учетную запись администратора
```bash
python3 manage.py createsuperuser
```
* Для локального запуска выполните команду
```bash
python3 manage.py runserver
```
* При успешном запуске в консоль выведется сообщение:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 21, 2022 - 20:25:17
Django version 3.2.13, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

* Сайт будет доступен по адресу http://127.0.0.1:8000. 
* Интерфейс администрирования сайта по адресу http://127.0.0.1:8000/admin/.



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).


