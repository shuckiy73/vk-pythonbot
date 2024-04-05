# Мой личный бот на python для ВК
####
Этот бот просто отвечает на поддерживаемые запросы в переписке с сообществом. Был написан мною в целях изучения python. Этот README является инструкцией по установке и использованию бота.
# Функции бота
Чтобы воспользоваться функциями бота, необходимо отправить команду и в некоторых случаях аргумент. Все команды начинаются с восклицательного знака

* **!h, !help, !п, !помощь** — бот отправляет список команд и их краткое описание из `help.txt`, а так же дату последнего обновления и ссылку на этот репозиторий
* **!my_id, !ид** — бот достаёт из вашего сообщения `user_id` и отправляет его вам
* **!user_id, !пользователь *id*** — бот отправляет *id* нужного вам пользователя в vk api методом `users.get` и отправляет вам полученные этим методом данные: имя, фамилия, id, пол, время последнего онлайна и платформы, закрыт ли профиль
* **!group_id, !группа *id*** — бот отправляет *id* нужного вам сообщества в vk api методом `groups.getById` и отправляет вам полученные этим методом данные: название, описание, id, количество подписчиков
* **!image, !картинка** — бот, с помощью костыля в виде сервисного ключа приложения, получает vk api методом `photos.get` фотографии альбома, выбирает с помощью функции в python `random.randrange` одну фотографию и отправляет вам её как attachment
* **!random, !рандом *число1* *число2*** — бот генерирует с помощью `random.randint()` случайное число и отправляет его вам. Если без аргументов, то число от 0 до 10. Если есть одно число, то от 0 до *число1*. Если есть оба числа, то от *число1* до *число2*
* **!weather, !погода *город*** — бот получает с помощью OpenWeather API текущую погоду в городе и отправляет её вам
* **!wiki, !вики *запрос*** — бот получает с помощью Wikipedia API краткое описание статьи по запросу и отправляет её вам
* **!byn, !белруб** — бот получает с помощью НБ РБ API текущий курс белорусского рубля и отправляет её вам
* **!echo, !эхо** — бот начинает повторять за вами, чтобы это остановить, надо написать *!echo off*
* **!game, !игра *камень/ножницы/бумага/статистика*** — бот играет с вами в "Камень, ножницы, бумага" и ведет статистику игр, которую записывает в файл БД
* **!midnight, !полночь** — бот будет уведомлять о каждом миднайте по Московскому времени. Введите ещё раз, чтобы отменить это
* **!subscribe, !подписаться** — бот будет уведомлять вас о каждом новом посте. Введите ещё раз, чтобы отменить это
* **!debug, !дебаг** — бот отправляет информацию о своём состоянии
* **!debug *log***, **!дебаг *лог*** — бот отправляет последние 10 строк из своего лога. Доступно только вам
* **!debug *bots***, **!дебаг *боты*** — бот отправляет информацию об объектах бота в памяти. Доступно только вам
* **!debug *game***, **!дебаг *игра*** — бот отправляет всю статистику по игре !game
* **!access *all/owner***, **!доступ *владелец/все*** — позволяет в беседе установить уровень доступа к командам *!midnight*, *!subscribe* и *!debug*. *all* - все могут пользоваться. *owner* - только вы. Доступно только вам
* **!turnoff, !выкл** — даёт боту команду на выключение. Доступно только вам
* **!admin_mode, !админмод** — если чат, в которой активируется команда, является беседой и в ней у бота есть полномочия администратора, то бот переходит в режим модерации. Пока что он может только кикать людей за @all и @online, реагировать на приход/уход участника беседы и дать возможность пользоваться командой *!ban*. Введите ещё раз, чтобы выключить режим модерации. Доступно только вам
* **!ban, !бан *@user*** — банит пользователя из беседы (в смысле выгоняет, юзер не сможет вернуться пока бот или админ не предложит). Требует режим модерации, могут воспользоваться только администраторы
* **!resist, !запретить *@user*** — запрещает пользователю пользоваться ботом, могут воспользоваться только администраторы
* **!restore, !разрешить *@user*** — снова разрешает пользователю пользоваться ботом, могут воспользоваться только администраторы
* **!spammer *add* *@user*, !спаммер *добавить* *@user*** — Добавляет пользователя в "базу спамеров". Если пользователь из этой базы попытается присоединится к беседе, в которой он внесён в эту самую базу, он тут же будет изгнан. Требует режим модерации, могут воспользоваться только администраторы
* **!spammer *remove* *@user*, !спаммер *удалить* *@user*** — Убирает пользователя из "базу спамеров". Требует режим модерации, могут воспользоваться только администраторы
* **бот дай денег** — Посылает вас нахуй

# Установка и запуск бота
Лучшим решением будет иметь платный аккаунт на [pythonanywhere](https://www.pythonanywhere.com/), чтобы запускать бота, как Always-on task. Можно, конечно, запускать бота в консоли, но pythonanywhere может выключить вашу консоль, если вы долго не будете посещать её.
## Основа
Итак, заходим на pythonanywhere, входим или регистрируемся.

Создаём консоль на bash и прописываем:

`git clone https://github.com//pythonbot.git`

Эта команда создаст папку `pythonbot` и поместит туда бота.

Теперь заходим в директорию бота (`cd pythonbot/`) и устанавливаем необходимые библиотеки:

`pip3 install vk-api pyowm Wikipedia-API --user`

Эта команда установит все необходимые библиотеки для работы бота.

Настроим ваше сообщество для работы с ботом: заходим в *Управление -> Работа с API*. Здесь создаём токен сообщества с правами доступа к сообщениям, фотографиям и стене. Идем в *Long Poll API*, включаем его и ставим последнюю доступную версию (бот тестировался на версии 5.120). В *Типы событий* должны стоять галочки на следующих событиях: Входящее сообщение, Запрет на получение, Добавление записи на стене.

Создадим файл конфигурации для бота: В pythonanywhere тыкаем на *Files*, переходим в директорию *dan63047pythonbot* и создаём там новый фаил с названием `config.py`. В нём должно быть написано следующее:
```python
vk_group_token = "vk_group_token" # Токен сообщества
group_id = -- # Цифровой ид группы
owner_id = -- # Цифровой ид вашей страницы вк, чтобы вы могли управлять ботом в переписке
admins = [--, --] # Список ид аккаунтов администраторов, которые в любом случае тоже смогут получать доступ к командам администрирования, оставьте пустым, если их нет
vk_service_token = "vk_service_token" # Сервисный ключ доступа для команды !image. Оставьте None, если хотите выключить эту команду
album_for_command = -- # Цифровой ид альбома для команды !image. Оставьте None, если хотите выключить эту команду
openweathermap_api_key = 'openweathermap_api_key' # Ключ OpenWeather API. Оставьте None, если хотите выключить команду !weather
```
## Если вы будете использовать команду !image
Разберёмся с костылём для метода `photos.get`: Идем на `vk.com/dev`, нажимаем на *Мои приложения* и кликаем по *Создать приложение*. Новое приложение может называться как угодно, от него нам необходимо всего лишь сервисный ключ доступа, который можно найти, если нажать на *Настройки*
## Если вы будете использовать команду !weather
Перейдите по `openweathermap.org`, пройдите там регистрацию и создайте API ключ
## Запуск бота
Если аккаунт платный: в pythonanywhere тыкаем на *Tasks*, создаём и запускаем в *Always-on tasks* задачу `python3.8 /home/pythonanywhere_nickname/pythonbot/longpulling.py`, где вместо pythonanywhere_nickname должен быть ваш никнейм на pythonanywhere. После небольшого тупления pythonanywhere запустит вашего бота.

Если аккаунт бесплатный: в bash консоли переходим в директорию бота и прописываем `python3 longpulling.py`. Консоль можно оставить в покое, но лучше раз в день проверять её чтобы консоль не отключили
## Другие варианты запуска бота
Скорее всего, вы можете найти где-нибудь VPS или организовать всё на своём компьютере. Там вы просто скачиваете и устанавливаете Python последней версии, настраиваете конфиг бота и запускаете его.
# botconsole.py
Если вы введёте команду `pyhton3 botconsole.py`, то запустится консоль бота. Она пока находится в разработке и не может управлять именно ботом, скорее вы просто будете выполнять действия от лица бота. Вот список поддерживаемых команд:
* **help** — выводит список доступных команд
* **exit** — завершает работу консоли
* **message *peer_id* *message*** — отправляет *message* в переписку *peer_id* от имени сообщества
* **msg_history *peer_id* *count*** — возвращает историю переписки, последние *count* сообщений. Если *count* не указано, то последние 20 сообщений
На следующей команде хотелось бы уделить особое внимание, ведь с помощью неё можно вызывать функции бота
## Команда **bot**
Если просто вызвать эту команду, то она покажет список существующих объектов ботов. Однако так же у команды есть и большое количество аргументов:
* **bot *update*** — обновляет список объектов ботов и их состояние
* **bot *create* *peer_id*** — создаёт объект бота для переписки *peer_id*
* **bot *delete* *peer_id*** — удаляет существующий объект бота для переписки *peer_id*
* **bot *changeMidnightFlag* *peer_id*** — меняет флаг в объекте бота *peer_id*, по которому он определяет, надо ли оповещать о Midnight
* **bot *midnight* *peer_id*** — инициирует ивент Midnight для объекта бота *peer_id*
# Использованные библиотеки
* [vk_api](https://github.com/python273/vk_api) — модуль для создания скриптов для социальной сети Вконтакте
* [pyowm](https://github.com/csparpa/pyowm) — модуль для получения погоды через OpenWeather API
* [Wikipedia-API](https://github.com/martin-majlis/Wikipedia-API) — модуль для получения статей из Wikipedia
# Дополнительно

Буду рад помощи и поддержке
