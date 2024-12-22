import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

ExitPh = InlineKeyboardMarkup()
ExitPh.add(InlineKeyboardButton('назад', callback_data='exitphoto'))

Exitt = InlineKeyboardMarkup()
Exitt.add(InlineKeyboardButton('назад', callback_data='exit'))

Delete2 = InlineKeyboardMarkup()
Delete2.add(InlineKeyboardButton('назад', callback_data='delete2'))

Delete3 = InlineKeyboardMarkup()
Delete3.add(InlineKeyboardButton('назад', callback_data='delete3'))

Delete4 = InlineKeyboardMarkup()
Delete4.add(InlineKeyboardButton('назад', callback_data='delete4'))

Delete5 = InlineKeyboardMarkup()
Delete5.add(InlineKeyboardButton('назад', callback_data='delete5'))

Delete6 = InlineKeyboardMarkup()
Delete6.add(InlineKeyboardButton('назад', callback_data='delete6'))

Delete7 = InlineKeyboardMarkup()
Delete7.add(InlineKeyboardButton('назад', callback_data='delete7'))

Delete8 = InlineKeyboardMarkup()
Delete8.add(InlineKeyboardButton('назад', callback_data='delete8'))

#КНОПКИ ГЛАВНОГО МЕНЮ

markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton('Процессы, обязанности и правила ВТР', callback_data='one'))
# Процессы, обязанности и правила ВТР подглавы
oneglav = InlineKeyboardMarkup(row_width=1)
oneglav.add(InlineKeyboardButton('• В офисе •', callback_data='one1'))
oneglav.add(InlineKeyboardButton('• На выезде •', callback_data='one2'))
button1 = InlineKeyboardButton('назад', callback_data='exit')
oneglav.add(button1)

markup.add(InlineKeyboardButton('Устройства/Настройки ТА', callback_data='two'))
markup.add(InlineKeyboardButton('Платежные системы', callback_data='three'))

# Платежные системы подглавы
doppay = InlineKeyboardMarkup()
doppay.add(InlineKeyboardButton('• Монетоприемники •', callback_data='pay'))

# Платежные системы - монетоприемники
dopmon = InlineKeyboardMarkup()
dopmon.add(InlineKeyboardButton('• NRI •', callback_data='nri'))
dopmon.add(InlineKeyboardButton('• MEI •', callback_data='mei'))
button1 = InlineKeyboardButton('назад', callback_data='exit')
dopmon.add(button1)

# Платежные системы подглавы
doppay.add(InlineKeyboardButton('• Купюроприемники •', callback_data='kupur'))
doppay.add(InlineKeyboardButton('• Безналичные системы •', callback_data='beznal'))

# Платежные системы - безналичные системы
doppay2 = InlineKeyboardMarkup()
doppay2.add(InlineKeyboardButton('MatiPay', callback_data='four'))
doppay2.add(InlineKeyboardButton('Банковский терминал', callback_data='five'))
doppay2.add(InlineKeyboardButton('App (приложение)', callback_data='six'))
doppay2.add(InlineKeyboardButton('назад', callback_data='exit'))

# Платежные системы подглавы
doppay.add(InlineKeyboardButton('• MDB •', callback_data='mdb'))
doppay.add(InlineKeyboardButton('назад', callback_data='exit'))

markup.add(InlineKeyboardButton('Гидросистема', callback_data='seven'))
markup.add(InlineKeyboardButton('Кофемолка', callback_data='eight'))
markup.add(InlineKeyboardButton('Кофе', callback_data='nine'))
markup.add(InlineKeyboardButton('Кофе-группа', callback_data='ten'))
markup.add(InlineKeyboardButton('Ошибки ТА', callback_data='eleven'))
markup.add(InlineKeyboardButton('Кофе-машины', callback_data='podglava'))

# Кофе-машины подглавы
dop = InlineKeyboardMarkup()
dop.add(InlineKeyboardButton('• Koro Prime •', callback_data='twelve'))
dop.add(InlineKeyboardButton('• Kaleo •', callback_data='thirteen'))
dop.add(InlineKeyboardButton('• Krea •', callback_data='fourteen'))
dop.add(InlineKeyboardButton('• Bianchi Gaia •', callback_data='fifteen'))
dop.add(InlineKeyboardButton('• Biepi MC1 •', callback_data='Biepi'))
button1 = InlineKeyboardButton('назад', callback_data='exit')
dop.add(button1)

markup.add(InlineKeyboardButton('Общение с клиентом', callback_data='sixteen'))
markup.add(InlineKeyboardButton('Инструкции', callback_data='seventeen'))
markup.add(InlineKeyboardButton('Видео-Инструкции', callback_data='videoinstr'))

# Видео-Инструкции подглавы
dopvid = InlineKeyboardMarkup()
dopvid.add(InlineKeyboardButton('• Работа с пальмом •', callback_data='videoinstr1'))
dopvid.add(InlineKeyboardButton('Полная оклейка, пример', callback_data='videoinstrokleyka'))
dopvid.add(InlineKeyboardButton('назад', callback_data='exit'))

markup.add(InlineKeyboardButton('Инструкции по моделям ТА', callback_data='instrta'))

markup.add(InlineKeyboardButton('Таблицы доз напитков по аппаратам', callback_data='dozer'))

markup.add(InlineKeyboardButton('Каталоги запчастей', callback_data='catalog'))

markup.add(InlineKeyboardButton('Размещение допоборудования на ТА', callback_data='dopoborydovanie'))

# КНОПКИ ВОПРОСОВ

# 1.1 В офисе - кнопки вопроса
one1 = InlineKeyboardMarkup()
one1.add(InlineKeyboardButton('Заявление на отпуск', callback_data='1.15'))
one1.add(InlineKeyboardButton('Сроки годности продуктов в сети', callback_data='1.24'))
one1.add(InlineKeyboardButton('Склад не выдал запчасть по предзаказу', callback_data='1.29'))
one1.add(InlineKeyboardButton('Как можно получить запчасти/продукты на складе?', callback_data='1.1'))
one1.add(InlineKeyboardButton('Предзаказ', callback_data='1.39'))
one1.add(InlineKeyboardButton('Подъезд в офис и инвентаризация', callback_data='1.2'))
one1.add(InlineKeyboardButton('Вам необходимо приехать в офис', callback_data='1.6'))
one1.add(InlineKeyboardButton('День обязательного подъезда в офис', callback_data='1.7'))
one1.add(InlineKeyboardButton('Получение запчастей/продуктов без предзаказа', callback_data='1.8'))
one1.add(InlineKeyboardButton('Сдача на склад продуктов, снятых с ТА', callback_data='1.25'))
button1 = InlineKeyboardButton('назад', callback_data='exit')
one1.add(button1)

# 1.2 На выезде - кнопки вопроса
one2 = InlineKeyboardMarkup()
one2.add(InlineKeyboardButton('Если не смог починить ТА', callback_data='1.40'))
one2.add(InlineKeyboardButton('Виды ТО и что в них входит', callback_data='1.41'))
one2.add(InlineKeyboardButton('Срок выполнения задачи в Bitrix', callback_data='1.11'))
one2.add(InlineKeyboardButton('Неисправность ТА по вине оператора', callback_data='1.16'))
one2.add(InlineKeyboardButton('Оповещение изменения ПС в ТА', callback_data='1.17'))
one2.add(InlineKeyboardButton('Сроки выполнения заказ-нарядов', callback_data='1.18'))
one2.add(InlineKeyboardButton('Обновление пальма', callback_data='1.19'))
one2.add(InlineKeyboardButton('Статус аксессуара', callback_data='1.27'))
one2.add(InlineKeyboardButton('Чат «Информация с ТП»', callback_data='1.36'))
one2.add(InlineKeyboardButton('ПРИОРИТЕТ ЗАЯВОК', callback_data='1.12'))
one2.add(InlineKeyboardButton('Заявка «заказ-наряд»', callback_data='1.3'))
one2.add(InlineKeyboardButton('Действие после закрытия любой заявки', callback_data='1.4'))
one2.add(InlineKeyboardButton('Закончился бензин после 17:00', callback_data='1.5'))
one2.add(InlineKeyboardButton('«Подъезд к кофейному ТА»', callback_data='1.9'))
one2.add(InlineKeyboardButton('«Выгрузка/загрузка» продуктов из СТА/КТА', callback_data='1.10'))
one2.add(InlineKeyboardButton('Промо акция с выключением цен в ТА', callback_data='1.13'))
one2.add(InlineKeyboardButton('Оставление Продуктов в ТА при изменении конфигурации', callback_data='1.14'))
one2.add(InlineKeyboardButton('Замена спирали на продукте в снеке', callback_data='1.20'))
one2.add(InlineKeyboardButton('Тесты напитков,сделанных в ТА', callback_data='1.21'))
one2.add(InlineKeyboardButton('Программа профилактики поломок', callback_data='1.22'))
one2.add(InlineKeyboardButton('Настройка напитков у клиента HoReCa или OCS', callback_data='1.23'))
one2.add(InlineKeyboardButton('Пустая загрузка при подъезде к кофе-поинтам', callback_data='1.26'))
one2.add(InlineKeyboardButton('Закрытие заказ-наряда без изменений в ТА', callback_data='1.28'))
one2.add(InlineKeyboardButton('Отсутствие звонков в пальме', callback_data='1.30'))
one2.add(InlineKeyboardButton('Оплата парковки (только филиал СПб)', callback_data='1.31'))
one2.add(InlineKeyboardButton('Работа после 17:00', callback_data='1.32'))
one2.add(InlineKeyboardButton('Переделка ТА на другой формат стаканов', callback_data='1.34'))
one2.add(InlineKeyboardButton('Осмотр ТП на филиале', callback_data='1.35'))
one2.add(InlineKeyboardButton('Оповещение о выезде на заявку по проблеме', callback_data='1.37'))
one2.add(InlineKeyboardButton('Действие перед выездом на заявку по проблеме', callback_data='1.38'))
button1 = InlineKeyboardButton('назад', callback_data='exit')
one2.add(button1)

# 2. Устройства/Настройки ТА - кнопки вопроса
two = InlineKeyboardMarkup()
two.add(InlineKeyboardButton('• FAS •', callback_data='fas'))
two.add(InlineKeyboardButton('• FAS ADV •', callback_data='fasfv'))
two.add(InlineKeyboardButton('• TCN •', callback_data='tcn'))
two.add(InlineKeyboardButton('Отличия гидросистемы Kikko от Concerto', callback_data='2.1'))
two.add(InlineKeyboardButton('Диспенсер крышек Kikko Max ToGo и Kikko Es6 ToGo', callback_data='2.2'))
two.add(InlineKeyboardButton('Дозы воды Kikko Max/Es6', callback_data='2.27'))
two.add(InlineKeyboardButton('Отличие ТА обычных от ТА ToGo', callback_data='2.3'))
two.add(InlineKeyboardButton('После копирования настроек - ошибка «носики»', callback_data='2.29'))
two.add(InlineKeyboardButton('Калибровка доз порошков', callback_data='2.4'))
two.add(InlineKeyboardButton('Телеметрия', callback_data='2.5'))
two.add(InlineKeyboardButton('Как открыть «Умный холодильник»', callback_data='2.6'))
two.add(InlineKeyboardButton('Кнопки в ColibriC5/C4 в режиме программирования', callback_data='2.7'))
two.add(InlineKeyboardButton('Регулировка контрастности дисплея Colibri', callback_data='2.8'))
two.add(InlineKeyboardButton('Тестирование выдачи напитков', callback_data='2.9'))
two.add(InlineKeyboardButton('Просмотр ошибок ТА', callback_data='2.10'))
two.add(InlineKeyboardButton('SnakkyMax – рандомно выдает/не выдает продукты', callback_data='2.11'))
two.add(InlineKeyboardButton('Canto/Maestro - размешиватели из одного ряда', callback_data='2.12'))
two.add(InlineKeyboardButton('Canto/Maestro при вкл сразу выдает размеш-ль и сахар', callback_data='2.28'))
two.add(InlineKeyboardButton('Зависает молоко в бункере Canto/Concerto/Opera', callback_data='2.13'))
two.add(InlineKeyboardButton('Перепрошивка ТА', callback_data='2.15'))
two.add(InlineKeyboardButton('Замена платы ЦПУ/управления', callback_data='2.16'))
two.add(InlineKeyboardButton('Snakky Max при подъезде не работает', callback_data='2.17'))
two.add(InlineKeyboardButton('Не работает мотор контейнера раств-х Canto/Maestro', callback_data='2.19'))
two.add(InlineKeyboardButton('Потребляемая мощность ТА', callback_data='2.23'))
two.add(InlineKeyboardButton('Подключение оптического датчика Canto', callback_data='2.24'))
two.add(InlineKeyboardButton('Подключение оптического датчика Concerto', callback_data='2.25'))
two.add(InlineKeyboardButton('назад', callback_data='exit'))

# 2.1 FAS вопрос
fas = InlineKeyboardMarkup()
fas.add(InlineKeyboardButton('Fas продает с пустой ячейки', callback_data='2.14'))
fas.add(InlineKeyboardButton('Настройка Fas', callback_data='2.20'))
fas.add(InlineKeyboardButton('Тест продукта Fas', callback_data='2.21'))
fas.add(InlineKeyboardButton('Высоты полок Fas', callback_data='2.26'))
fas.add(InlineKeyboardButton('В Fas не купить товар по банковскому терминалу', callback_data='3.29'))
fas.add(InlineKeyboardButton('Установка двойной спирали в FAS', callback_data='2.18'))
fas.add(InlineKeyboardButton('Инструкция по эксплуатации FAS', callback_data='Fast900/1000'))
fas.add(InlineKeyboardButton('Каталог запчастей FAS', callback_data='FAS1050'))
fas.add(InlineKeyboardButton('назад', callback_data='exit'))

# 2.2 FAS ADV вопрос
fasfv = InlineKeyboardMarkup()
fasfv.add(InlineKeyboardButton('Установка Price-Holding в FAS ADV', callback_data='fasfv1'))
fasfv.add(InlineKeyboardButton('Русификация меню покупателя FAS ADV', callback_data='fasfv2'))
fasfv.add(InlineKeyboardButton('назад', callback_data='exit'))

# 2.3 TCN вопрос
tcn = InlineKeyboardMarkup()
tcn.add(InlineKeyboardButton('Пароль для входа в техническое меню', callback_data='tcn.4'))
tcn.add(InlineKeyboardButton('Инструкция по эксплуатации TCN', callback_data='tcn.1'))
tcn.add(InlineKeyboardButton('Технические характеристики TCN', callback_data='tcn.2'))
tcn.add(InlineKeyboardButton('Высоты полок для ТА TCN', callback_data='tcn.3'))
tcn.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3. Платежные системы - кнопки вопроса
three = InlineKeyboardMarkup()
three.add(InlineKeyboardButton('• Монетоприемники •', callback_data='pay'))
three.add(InlineKeyboardButton('• Банкнотоприемники •', callback_data='kupur'))
three.add(InlineKeyboardButton('• Безналичные системы •', callback_data='beznal'))
three.add(InlineKeyboardButton('• MDB •', callback_data='mdb'))
three.add(InlineKeyboardButton('Когда снимать статистику', callback_data='3.34'))
three.add(InlineKeyboardButton('Cнятие статистики два раза при замене МП', callback_data='3.11'))
three.add(InlineKeyboardButton('Платежные системы и Cashless', callback_data='3.33'))
three.add(InlineKeyboardButton('ТА принимает старые 5 рублевые монеты', callback_data='3.12'))
three.add(InlineKeyboardButton('Частичная оплата товара наличными и безналом', callback_data='3.19'))
three.add(InlineKeyboardButton('Работа нескольких устройств на одном cashless', callback_data='3.22'))
three.add(InlineKeyboardButton('Покупка дорогого товара в снеке по цене дешевого', callback_data='3.28'))
three.add(InlineKeyboardButton('ПС выдает ошибку «Нет связи/ответа с ТА»', callback_data='3.32'))
three.add(InlineKeyboardButton('Протоколы обмена информации между ТА и ПС', callback_data='3.10'))
three.add(InlineKeyboardButton('Базовая единица/Scaling factor', callback_data='3.8'))
three.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.1.1 Платежные системы - NRI - кнопки вопроса
three1 = InlineKeyboardMarkup()
three1.add(InlineKeyboardButton('Замена NRI', callback_data='nri.13'))
three1.add(InlineKeyboardButton('Настройка NRI', callback_data='nri.12'))
three1.add(InlineKeyboardButton('Cashless NRI', callback_data='nri.11'))
three1.add(InlineKeyboardButton('Прошивка аудита NRI + установка даты и времени', callback_data='nri.14'))
three1.add(InlineKeyboardButton('Проверка NRI', callback_data='nri.2'))
three1.add(InlineKeyboardButton('Отличие МП NRI от MEI', callback_data='nri.3'))
three1.add(InlineKeyboardButton('Назначение проводов в NRI', callback_data='nri.4'))
three1.add(InlineKeyboardButton('Просмотр оптических датчиков кассеты NRI', callback_data='nri.5'))
three1.add(InlineKeyboardButton('Батарейка аудит-модуля NRI', callback_data='nri.6'))
three1.add(InlineKeyboardButton('NRI не принимает монеты', callback_data='nri.7'))
three1.add(InlineKeyboardButton('Отображение прайсов в линии цен NRI', callback_data='nri.8'))
three1.add(InlineKeyboardButton('NRI – не меняется код монетоприемника', callback_data='nri.9'))
three1.add(InlineKeyboardButton('Kikko Es6. NRI не принимает монеты', callback_data='nri.10'))
three1.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.1.2 Платежные системы - MEI - кнопки вопроса
three2 = InlineKeyboardMarkup()
three2.add(InlineKeyboardButton('Замена MEI', callback_data='mei.8'))
three2.add(InlineKeyboardButton('Настройка MEI', callback_data='mei.7'))
three2.add(InlineKeyboardButton('Cashless MEI', callback_data='mei.6'))
three2.add(InlineKeyboardButton('Проверка MEI', callback_data='mei.2'))
three2.add(InlineKeyboardButton('Отличие МП NRI от MEI', callback_data='mei.3'))
three2.add(InlineKeyboardButton('Назначение проводов в MEI', callback_data='mei.4'))
three2.add(InlineKeyboardButton('Не работает безнал на Mei', callback_data='mei.5'))
three2.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.2 Купюроприемники вопросы - кнопки вопроса
kupur = InlineKeyboardMarkup()
kupur.add(InlineKeyboardButton('Десятичная точка. Вкл/откл в купюроприемниках', callback_data='kup.1'))
kupur.add(InlineKeyboardButton('Купюра не укладывается в стакер', callback_data='kup.2'))
kupur.add(InlineKeyboardButton('ICT принимает купюры, но не отображает их', callback_data='kup.3'))
kupur.add(InlineKeyboardButton('SMW отображает 100р как 1р', callback_data='kup.4'))
kupur.add(InlineKeyboardButton('100р новые (10.10.24) принимаются как 200р', callback_data='kup.5'))
kupur.add(InlineKeyboardButton('MEI при установке не выходит в работу', callback_data='kup.6'))
kupur.add(InlineKeyboardButton('MEI сигнализирует, что застряла купюра', callback_data='kup.7'))
kupur.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.3.1 Безналичные системы - Matipay - кнопки вопроса
four = InlineKeyboardMarkup()
four.add(InlineKeyboardButton('Что такое «Matipay»', callback_data='4.1'))
four.add(InlineKeyboardButton('MatiTech', callback_data='4.2'))
four.add(InlineKeyboardButton('Установка Audit-кабеля в МП NRI/MEI (ENG)', callback_data='17.2'))
four.add(InlineKeyboardButton('Установка Audit-кабеля в МП NRI/MEI (RUS)', callback_data='17.22'))
four.add(InlineKeyboardButton('Проверка продаж Matipay', callback_data='4.18'))
four.add(InlineKeyboardButton('Создание/редактирование устройств Matipay_PDF', callback_data='4.12'))
four.add(InlineKeyboardButton('Создание/удаление Matipay через Matitech', callback_data='4.16'))
four.add(InlineKeyboardButton('Создание/удаление Matipay + App через Matitech', callback_data='4.14'))
four.add(InlineKeyboardButton('Создание/удаление Matipay + Vendotek VL', callback_data='4.15'))
four.add(InlineKeyboardButton('Cashless при создании нового уcтройства MatiPay', callback_data='4.7'))
four.add(InlineKeyboardButton('Прошивка карты памяти Matipay на Iphone', callback_data='4.17'))
four.add(InlineKeyboardButton('Частые проблемы и методы их устранения', callback_data='4.3'))
four.add(InlineKeyboardButton('Сим-карты для Matipay', callback_data='1.33'))
four.add(InlineKeyboardButton('Замена модуля на «Умном холодильнике»', callback_data='4.5'))
four.add(InlineKeyboardButton('Уровень сотового сигнала', callback_data='4.8'))
four.add(InlineKeyboardButton('Завис  модуль MatiPay', callback_data='4.9'))
four.add(InlineKeyboardButton('Просмотр ошибок ТА', callback_data='4.10'))
four.add(InlineKeyboardButton('Проверка Matipay', callback_data='4.11'))
four.add(InlineKeyboardButton('При установке приложения Matipay не выходит на связь', callback_data='4.13'))
four.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.3.2 Безналичные системы - Банковский терминал - кнопки вопроса
five = InlineKeyboardMarkup()
five.add(InlineKeyboardButton('• Ошибки в ЛК ТТ •', callback_data='errorLK'))
five.add(InlineKeyboardButton('Частые проблемы и методы их устранения', callback_data='5.1'))
five.add(InlineKeyboardButton('Сим-карты для банковских терминалов', callback_data='1.33'))
five.add(InlineKeyboardButton('Установка/замена банк терминала', callback_data='5.2'))
five.add(InlineKeyboardButton('Отличие Vendotek V3/VN/VL', callback_data='5.3'))
five.add(InlineKeyboardButton('Сервисное меню Vendotek VL', callback_data='5.4'))
five.add(InlineKeyboardButton('Сервисное меню Vendotek V3/VN', callback_data='5.5'))
five.add(InlineKeyboardButton('Обновление Vendotek VL', callback_data='5.6'))
five.add(InlineKeyboardButton('Factory reset/Долго загружается Vendotek VL', callback_data='5.7'))
five.add(InlineKeyboardButton('Код «СЕ»', callback_data='5.8'))
five.add(InlineKeyboardButton('Монетоприемники vs банковские терминалы', callback_data='5.9'))
five.add(InlineKeyboardButton('Терминал пишет "Выберите товар"', callback_data='5.10'))
five.add(InlineKeyboardButton('Постоянный ребут NRI+Vendotek V3/VN+CashCode', callback_data='5.11'))
five.add(InlineKeyboardButton('В Fas не купить товар по банковскому терминалу', callback_data='5.12'))
five.add(InlineKeyboardButton('Руководство по эксплуатации Vendotek V3', callback_data='5.13'))
five.add(InlineKeyboardButton('Руководство по эксплуатации Vendotek VN', callback_data='5.14'))
five.add(InlineKeyboardButton('Руководство по эксплуатации Vendotek VL', callback_data='5.15'))
five.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.3.2.1 Безналичные системы - Банковский терминал - Ошибки_ЛК_ТТ - кнопки вопроса
errorLK = InlineKeyboardMarkup()
errorLK.add(InlineKeyboardButton('Tamper', callback_data='errorLK1'))
errorLK.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.3.3 Безналичные системы - АПП - кнопки вопроса
six = InlineKeyboardMarkup()
six.add(InlineKeyboardButton('Создание/удаление Matipay + App через Matitech', callback_data='4.14'))
six.add(InlineKeyboardButton('Не подключиться по приложению к App', callback_data='6.1'))
six.add(InlineKeyboardButton('Индикация работы App', callback_data='6.2'))
six.add(InlineKeyboardButton('Варианты подключения к App', callback_data='6.3'))
six.add(InlineKeyboardButton('Будет ли работать App одновременно с Vendotek VL', callback_data='6.4'))
six.add(InlineKeyboardButton('Монетоприемники vs App', callback_data='6.5'))
six.add(InlineKeyboardButton('Принцип работы NFC-брелока', callback_data='6.6'))
six.add(InlineKeyboardButton('Не купить/не видит/не пополнить  NFC-брелок', callback_data='6.7'))
six.add(InlineKeyboardButton('назад', callback_data='exit'))

# 3.4 MDB - кнопки вопроса
mdb = InlineKeyboardMarkup()
mdb.add(InlineKeyboardButton('Maestro/Canto/Opera', callback_data='mdb.1'))
mdb.add(InlineKeyboardButton('Maestro/Canto/Opera с Vendotek VL', callback_data='mdb.5'))
mdb.add(InlineKeyboardButton('Замена платежной системы MDB в Fas', callback_data='mdb.2'))
mdb.add(InlineKeyboardButton('Concerto', callback_data='mdb.3'))
mdb.add(InlineKeyboardButton('Snakky Jazz', callback_data='mdb.4'))
mdb.add(InlineKeyboardButton('назад', callback_data='exit'))

# 4. Гидросистема - кнопки вопроса
seven = InlineKeyboardMarkup()
seven.add(InlineKeyboardButton('Недолив напитка после долгого простоя ТА', callback_data='7.1'))
seven.add(InlineKeyboardButton('Нижний насос не качает, напряжение не приходит', callback_data='7.2'))
seven.add(InlineKeyboardButton('При замене помпы она сразу же сгорает', callback_data='7.3'))
seven.add(InlineKeyboardButton('Проверка гидросистемы от эйр-брейка к счетчику воды', callback_data='7.4'))
seven.add(InlineKeyboardButton('Проверка катушки/корпуса клапана на бойлере', callback_data='7.5'))
seven.add(InlineKeyboardButton('Проверка гидросистемы', callback_data='7.6'))
seven.add(InlineKeyboardButton('Проверка счетчика воды', callback_data='7.7'))
seven.add(InlineKeyboardButton('Проверка бойлера', callback_data='7.8'))
seven.add(InlineKeyboardButton('Допустимые помпы подкачки воды на ТА Krea', callback_data='7.9'))
seven.add(InlineKeyboardButton('Для чего нужен Bypass на помпе', callback_data='7.10'))
seven.add(InlineKeyboardButton('Зачем на клапан эспр надевается шланг сверху', callback_data='7.11'))
seven.add(InlineKeyboardButton('Отличие гидросистемы Kikko от Concerto LB', callback_data='7.12'))
seven.add(InlineKeyboardButton('Регулировка температуры на Colibri', callback_data='7.13'))
seven.add(InlineKeyboardButton('Помпы, используемые в сети Сиба-Вендинг', callback_data='7.14'))
seven.add(InlineKeyboardButton('назад', callback_data='exit'))

# 5. Кофемолка - кнопки вопроса
eight = InlineKeyboardMarkup()
eight.add(InlineKeyboardButton('Оп/Кан/Конч делает несколько оборотов и встает', callback_data='8.1'))
eight.add(InlineKeyboardButton('Тестирование кофемолки', callback_data='8.2'))
eight.add(InlineKeyboardButton('Регулировка дозы кофе в Opera', callback_data='8.3'))
eight.add(InlineKeyboardButton('Жженый кофе', callback_data='8.4'))
eight.add(InlineKeyboardButton('Настройка помола', callback_data='8.5'))
eight.add(InlineKeyboardButton('Жидкая таблетка', callback_data='8.6'))
eight.add(InlineKeyboardButton('Взаимозаменяемость кофемолки Калео', callback_data='8.7'))
eight.add(InlineKeyboardButton('назад', callback_data='exit'))

# 6. Кофе - кнопки вопроса
nine = InlineKeyboardMarkup()
nine.add(InlineKeyboardButton('Жженый кофе', callback_data='9.1'))
nine.add(InlineKeyboardButton('Температура воды при заварке кофе', callback_data='9.2'))
nine.add(InlineKeyboardButton('Настройка помола', callback_data='9.3'))
nine.add(InlineKeyboardButton('Жидкая таблетка на выходе из пресса 42/46', callback_data='9.4'))
nine.add(InlineKeyboardButton('12 факторов влияющих на приготовление кофе', callback_data='9.5'))
nine.add(InlineKeyboardButton('Обзор блендов кофе Lavazza', callback_data='9.6'))
nine.add(InlineKeyboardButton('Теоретический курс кофе', callback_data='9.7'))
nine.add(InlineKeyboardButton('назад', callback_data='exit'))

# 7. Кофе-группа - кнопки вопроса
ten = InlineKeyboardMarkup()
ten.add(InlineKeyboardButton('Принцип работы кофе-группы Lavazza', callback_data='10.1'))
ten.add(InlineKeyboardButton('Отличие зерновых прессов ToGo от обычных', callback_data='10.2'))
ten.add(InlineKeyboardButton('Проверка коф пресса', callback_data='10.3'))
ten.add(InlineKeyboardButton('Жидкая таблетка', callback_data='10.4'))
ten.add(InlineKeyboardButton('Объем камеры пресса KORO FR', callback_data='10.5'))
ten.add(InlineKeyboardButton('Зависает молотый кофе в дозаторе кофе на Kaleo', callback_data='10.6'))
ten.add(InlineKeyboardButton('Кофе-блок', callback_data='10.7'))
ten.add(InlineKeyboardButton('Блок-капсул', callback_data='10.8'))
ten.add(InlineKeyboardButton('Постоянно застревает капсула в прессе LB', callback_data='10.9'))
ten.add(InlineKeyboardButton('назад', callback_data='exit'))

# 8. Ошибки ТА - кнопки вопроса
eleven = InlineKeyboardMarkup()
eleven.add(InlineKeyboardButton('Просмотр ошибок ТА', callback_data='11.1'))
eleven.add(InlineKeyboardButton('Счетчик воды', callback_data='11.2'))
eleven.add(InlineKeyboardButton('Бойлер', callback_data='11.3'))
eleven.add(InlineKeyboardButton('Air-Break', callback_data='11.4'))
eleven.add(InlineKeyboardButton('Заберите напиток', callback_data='11.5'))
eleven.add(InlineKeyboardButton('Кофе-блок', callback_data='11.6'))
eleven.add(InlineKeyboardButton('Дозер', callback_data='11.7'))
eleven.add(InlineKeyboardButton('Блок-капсул', callback_data='11.8'))
eleven.add(InlineKeyboardButton('Инсталляция', callback_data='11.9'))
eleven.add(InlineKeyboardButton('Носики', callback_data='11.10'))
eleven.add(InlineKeyboardButton('Инициализация', callback_data='11.11'))
eleven.add(InlineKeyboardButton('Обслуживание', callback_data='11.12'))
eleven.add(InlineKeyboardButton('Ошибка выдачи стакана', callback_data='11.13'))
eleven.add(InlineKeyboardButton('назад', callback_data='exit'))

# 9.1 Koro Prime - кнопки вопроса
twelve = InlineKeyboardMarkup()
twelve.add(InlineKeyboardButton('Сброс ошибок', callback_data='12.1'))
twelve.add(InlineKeyboardButton('Капучинатор в Koro Prime', callback_data='12.2'))
twelve.add(InlineKeyboardButton('Не поступает молоко из капучинатора', callback_data='12.3'))
twelve.add(InlineKeyboardButton('Регулировка доз воды/порошков', callback_data='12.4'))
twelve.add(InlineKeyboardButton('Ошибка «Waste Full»', callback_data='12.5'))
twelve.add(InlineKeyboardButton('Просмотр неисправностей на экране', callback_data='12.6'))
twelve.add(InlineKeyboardButton('Перепрошивка КМ', callback_data='12.7'))
twelve.add(InlineKeyboardButton('Выдает ошибку «Очистить контейнер» каждые 5-6 напитков', callback_data='12.8'))
twelve.add(InlineKeyboardButton('Загрузка настроек на Google-диск', callback_data='12.9'))
twelve.add(InlineKeyboardButton('Жидкая таблетка', callback_data='12.10'))
twelve.add(InlineKeyboardButton('В конце приготовления - «плюется в стакан»', callback_data='12.27'))
twelve.add(InlineKeyboardButton('Объем камеры пресса', callback_data='12.11'))
twelve.add(InlineKeyboardButton('Американо 350мл за одно приготовление', callback_data='12.12'))
twelve.add(InlineKeyboardButton('Забрасывание молока в регулятор подачи воздуха', callback_data='12.13'))
twelve.add(InlineKeyboardButton('Счетчик отходов кофе', callback_data='12.14'))
twelve.add(InlineKeyboardButton('КМ периодически перезагружается', callback_data='12.15'))
twelve.add(InlineKeyboardButton('Количество Cashless', callback_data='12.16'))
twelve.add(InlineKeyboardButton('Постоянно ошибка «нет воды»', callback_data='12.17'))
twelve.add(InlineKeyboardButton('Наливает холодное молоко', callback_data='12.18'))
twelve.add(InlineKeyboardButton('Зависает растворимое молоко в бункере', callback_data='12.26'))
twelve.add(InlineKeyboardButton('Долгое удержание кнопки для выбора напитка', callback_data='12.19'))
twelve.add(InlineKeyboardButton('Не работают кнопки «вперед»/«назад» в  операторском меню', callback_data='12.20'))
twelve.add(InlineKeyboardButton('Код доступа в сервисное меню', callback_data='12.21'))
twelve.add(InlineKeyboardButton('Универсальная прош/настр KORA fm0.2 HoReCa', callback_data='12.22'))
twelve.add(InlineKeyboardButton('Универсальная прош/настр KORA fm0.3 Vending', callback_data='12.23'))
twelve.add(InlineKeyboardButton('Пользовательская инструкция', callback_data='12.24'))
twelve.add(InlineKeyboardButton('Инструкция по эксплуатации', callback_data='12.25'))
twelve.add(InlineKeyboardButton('назад', callback_data='exit'))

# 9.2 Kaleo - кнопки вопроса
thirteen = InlineKeyboardMarkup()
thirteen.add(InlineKeyboardButton('Отсутствует контейнер', callback_data='13.1'))
thirteen.add(InlineKeyboardButton('Молоко брызгает во все стороны в Калео', callback_data='13.2'))
thirteen.add(InlineKeyboardButton('Постоянно зависает молотый кофе в дозаторе кофе', callback_data='13.3'))
thirteen.add(InlineKeyboardButton('Почему не поступает вода в паровой бойлер Калео', callback_data='13.4'))
thirteen.add(InlineKeyboardButton('Сломался счетчик воды, нового нет', callback_data='13.5'))
thirteen.add(InlineKeyboardButton('Количество Cashless', callback_data='13.6'))
thirteen.add(InlineKeyboardButton('Низкое давление', callback_data='13.7'))
thirteen.add(InlineKeyboardButton('Регистрир-ся продажи за наличные (как бесплатные/нулевые)', callback_data='13.8'))
thirteen.add(InlineKeyboardButton('Код доступа в техническое меню', callback_data='13.9'))
thirteen.add(InlineKeyboardButton('Объемный счетчик', callback_data='13.10'))
thirteen.add(InlineKeyboardButton('Взаимозаменяемость кофемолки', callback_data='13.11'))
thirteen.add(InlineKeyboardButton('Прошивка и настройка', callback_data='13.12'))
thirteen.add(InlineKeyboardButton('Инструкция по эксплуатации', callback_data='13.13'))
thirteen.add(InlineKeyboardButton('назад', callback_data='exit'))

# 9.3 Krea - кнопки вопроса
fourteen = InlineKeyboardMarkup()
fourteen.add(InlineKeyboardButton('Отсутствует контейнер', callback_data='14.1'))
fourteen.add(InlineKeyboardButton('Зависает молотый кофе в дозаторе кофе', callback_data='14.2'))
fourteen.add(InlineKeyboardButton('Дергается помпа подачи воды на Креа', callback_data='14.3'))
fourteen.add(InlineKeyboardButton('Количество Cashless', callback_data='14.4'))
fourteen.add(InlineKeyboardButton('Регистрир-ся продажи за наличные (как бесплатные/нулевые)', callback_data='14.5'))
fourteen.add(InlineKeyboardButton('Комплект слива жидких отходов (через отверстие в поддоне)', callback_data='14.6'))
fourteen.add(InlineKeyboardButton('Код доступа в техническое меню', callback_data='14.8'))
fourteen.add(InlineKeyboardButton('Код бесплатной продажи напитков', callback_data='14.16'))
fourteen.add(InlineKeyboardButton('Клиент бесплатно получает напитки (при включенных ценнах)', callback_data='14.7'))
fourteen.add(InlineKeyboardButton('Допустимые помпы подкачки воды на ТА Krea', callback_data='14.9'))
fourteen.add(InlineKeyboardButton('Krea + Vendotek V3 периодически отваливается ПС', callback_data='14.10'))
fourteen.add(InlineKeyboardButton('Включение LOG-файлов на КМ KREA', callback_data='14.15'))
fourteen.add(InlineKeyboardButton('Прошивка KreaTouch_1.11.7', callback_data='14.12'))
fourteen.add(InlineKeyboardButton('Настройки для HoReCa', callback_data='14.13'))
fourteen.add(InlineKeyboardButton('Настройки для Vending', callback_data='14.14'))
fourteen.add(InlineKeyboardButton('Инструкция по эксплуатации', callback_data='14.11'))
fourteen.add(InlineKeyboardButton('назад', callback_data='exit'))

# 9.4 Bianchi Gaia - кнопки вопроса
fifteen = InlineKeyboardMarkup()
fifteen.add(InlineKeyboardButton('Сброс ошибок', callback_data='15.1'))
fifteen.add(InlineKeyboardButton('Регулировка доз воды/порошков', callback_data='15.2'))
fifteen.add(InlineKeyboardButton('Ошибка «WasteFull»', callback_data='15.3'))
fifteen.add(InlineKeyboardButton('Сервисный ключ Bianchi', callback_data='15.8'))
fifteen.add(InlineKeyboardButton('Выставляем пресс в «нулевое» положение', callback_data='15.9'))
fifteen.add(InlineKeyboardButton('Пресс раскрывается при приготовлении напитка', callback_data='15.10'))
fifteen.add(InlineKeyboardButton('Просмотр неисправностей на экране', callback_data='15.4'))
fifteen.add(InlineKeyboardButton('Прошивка ТА', callback_data='15.5'))
fifteen.add(InlineKeyboardButton('Пользовательская инструкция', callback_data='15.6'))
fifteen.add(InlineKeyboardButton('Инструкция по эксплуатации', callback_data='15.7'))
fifteen.add(InlineKeyboardButton('назад', callback_data='exit'))

# 9.5 Biepi MC1 - кнопки вопроса
Biepi = InlineKeyboardMarkup()
Biepi.add(InlineKeyboardButton('Рекламная брошюра', callback_data='bi.1'))
Biepi.add(InlineKeyboardButton('Инструкция', callback_data='bi.2'))
Biepi.add(InlineKeyboardButton('Сервис-мануал', callback_data='bi.3'))
Biepi.add(InlineKeyboardButton('назад', callback_data='exit'))

# 10. Общение с клиентом - кнопки вопроса
sixteen = InlineKeyboardMarkup()
sixteen.add(InlineKeyboardButton('Возврат денег', callback_data='16.1'))
sixteen.add(InlineKeyboardButton('Возврат товара', callback_data='16.2'))
sixteen.add(InlineKeyboardButton('Поврежденный ТА', callback_data='16.3'))
sixteen.add(InlineKeyboardButton('Клиент не доволен качеством/вкусом напитка', callback_data='16.4'))
sixteen.add(InlineKeyboardButton('Клиент просит угостить его кофе', callback_data='16.5'))
sixteen.add(InlineKeyboardButton('Клиент просит разменять деньги', callback_data='16.6'))
sixteen.add(InlineKeyboardButton('Изменение конфигурации КМ HoReCa', callback_data='16.7'))
sixteen.add(InlineKeyboardButton(' Допуск по электробезопасности', callback_data='16.8'))
sixteen.add(InlineKeyboardButton('назад', callback_data='exit'))

# 11. Инструкции - кнопки вопроса
seventeen = InlineKeyboardMarkup()
seventeen.add(InlineKeyboardButton('Подъезд техника к ТА', callback_data='17.3'))
seventeen.add(InlineKeyboardButton('назад', callback_data='exit'))

# 12. Видео-инструкции - кнопки вопроса
videoinstr = InlineKeyboardMarkup()
videoinstr.add(InlineKeyboardButton('Полная оклейка ТА, пример', callback_data='videoinstrokleyka'))

# 12.1 Видео-инструкции - Работа с пальмом - кнопки вопроса
videoinstr1 = InlineKeyboardMarkup()
videoinstr1.add(InlineKeyboardButton('Выбор заявки', callback_data='videocreatezv'))
videoinstr1.add(InlineKeyboardButton('Приложение Matitech', callback_data='videocreatezv2'))
videoinstr1.add(InlineKeyboardButton('Создание заявки по типу Другое', callback_data='videocreatezv3'))
videoinstr1.add(InlineKeyboardButton('Создание заявок', callback_data='videocreatezv4'))
videoinstr1.add(InlineKeyboardButton('Комментарий к заявке', callback_data='videocreatezv5'))
videoinstr1.add(InlineKeyboardButton('Закрытие заявки как невыполненная', callback_data='videocreatezv6'))
videoinstr1.add(InlineKeyboardButton('Время работы ТП', callback_data='videocreatezv7'))
videoinstr1.add(InlineKeyboardButton('Ищем просроченное ТО', callback_data='videocreatezv8'))
videoinstr1.add(InlineKeyboardButton('Отмечаем правильно ТО', callback_data='videocreatezv9'))
videoinstr1.add(InlineKeyboardButton('Заводим заявку на загрузку ТА для оператора', callback_data='videocreatezv10'))
videoinstr1.add(InlineKeyboardButton('Отмечаем 2 работы на одной ТП', callback_data='videocreatezv11'))
videoinstr1.add(InlineKeyboardButton('Замена узла, участвующего в ТО', callback_data='videocreatezv12'))
videoinstr1.add(InlineKeyboardButton('Работы при изменении конфигурации СТА', callback_data='videocreatezv13'))
videoinstr1.add(InlineKeyboardButton('Делаем предзаказ', callback_data='videocreatezv14'))
videoinstr1.add(InlineKeyboardButton('Прошивка карты памяти Matipay на Iphone', callback_data='videocreatezv15'))
videoinstr1.add(InlineKeyboardButton('Замена платежной системы', callback_data='videocreatezv16'))
videoinstr.add(InlineKeyboardButton('назад', callback_data='exit'))
videoinstr1.add(InlineKeyboardButton('назад', callback_data='exit'))

# 13. Инструкции - кнопки вопроса
instrta = InlineKeyboardMarkup()
instrta.add(InlineKeyboardButton('Fast', callback_data='Fast900/1000'))
instrta.add(InlineKeyboardButton('назад', callback_data='exit'))

# 14. Таблицы доз по напиткам - кнопки вопроса
dozer = InlineKeyboardMarkup()
dozer.add(InlineKeyboardButton('Canto X2 Double Cup, 300мл', callback_data='dozer1'))
dozer.add(InlineKeyboardButton('Canto X2 Double Cup, 250мл', callback_data='dozer2'))
dozer.add(InlineKeyboardButton('Canto Big Cup, 250мл', callback_data='dozer3'))
dozer.add(InlineKeyboardButton('Canto LB, 200мл', callback_data='dozer4'))
dozer.add(InlineKeyboardButton('Canto LB, 150мл', callback_data='dozer5'))
dozer.add(InlineKeyboardButton('Opera ToGo, 300мл', callback_data='dozer6'))
dozer.add(InlineKeyboardButton('Opera ToGo, 250мл', callback_data='dozer7'))
dozer.add(InlineKeyboardButton('Concerto LB, 200мл', callback_data='dozer8'))
dozer.add(InlineKeyboardButton('Concerto LB, 150мл', callback_data='dozer9'))
dozer.add(InlineKeyboardButton('Kikko Max ToGo, 300мл', callback_data='dozer10'))
dozer.add(InlineKeyboardButton('Kikko Max ToGo, 250мл', callback_data='dozer11'))
dozer.add(InlineKeyboardButton('Kikko Es6 ToGo, 200мл', callback_data='dozer12'))
dozer.add(InlineKeyboardButton('Kikko Max & Kikko Es6, 150мл', callback_data='dozer13'))
dozer.add(InlineKeyboardButton('Kalea/Krea, 250мл', callback_data='dozer14'))
dozer.add(InlineKeyboardButton('назад', callback_data='exit'))

# 15. Каталоги запчастей - кнопки вопроса
catalog = InlineKeyboardMarkup()
catalog.add(InlineKeyboardButton('Maestro X2 Double Cup Double', callback_data='Maestro_X2_Double_Cup_Double_Cup_BIG'))
catalog.add(InlineKeyboardButton('Canto X2 Double Cup', callback_data='Canto_Double_Cup'))
catalog.add(InlineKeyboardButton('CantoLB Big Cup, 250ml', callback_data='CantoLB_Big_Cup_250ml'))
catalog.add(InlineKeyboardButton('Canto LB', callback_data='Canto_LB'))
catalog.add(InlineKeyboardButton('Oper ToGo', callback_data='Opera_ToGo'))
catalog.add(InlineKeyboardButton('Opera', callback_data='Opera'))
catalog.add(InlineKeyboardButton('Concerto LB', callback_data='Concerto_LB'))
catalog.add(InlineKeyboardButton('Kikko Max', callback_data='Kikko_Max'))
catalog.add(InlineKeyboardButton('Kikko Es', callback_data='Kikko_Es'))
catalog.add(InlineKeyboardButton('Koro FM', callback_data='KORO_FM'))
catalog.add(InlineKeyboardButton('Koro сухое молоко', callback_data='Koro'))
catalog.add(InlineKeyboardButton('Krea', callback_data='Krea'))
catalog.add(InlineKeyboardButton('Kalea', callback_data='Kalea'))
catalog.add(InlineKeyboardButton('Gaia', callback_data='Gaia'))
catalog.add(InlineKeyboardButton('BiepiMC 1', callback_data='BiepiMC_1'))
catalog.add(InlineKeyboardButton('FAS 1050', callback_data='FAS1050'))
catalog.add(InlineKeyboardButton('Snakky Jazz', callback_data='Snakky_Jazz'))
catalog.add(InlineKeyboardButton('Snakky LX', callback_data='Snakky_LX'))
catalog.add(InlineKeyboardButton('Snakky Max', callback_data='Snakky_Max'))
catalog.add(InlineKeyboardButton('Bianchi', callback_data='Bianchi'))
catalog.add(InlineKeyboardButton('назад', callback_data='exit'))

# 16. Размещение допоборудования на ТА
dopoborydovanie = InlineKeyboardMarkup()
dopoborydovanie.add(InlineKeyboardButton('Maestro/Canto', callback_data='dopMaestro/Canto'))
dopoborydovanie.add(InlineKeyboardButton('Opera', callback_data='dopOpera'))
dopoborydovanie.add(InlineKeyboardButton('Concerto', callback_data='dopConcerto'))
dopoborydovanie.add(InlineKeyboardButton('Kikko Max', callback_data='dopKikkoMax'))
dopoborydovanie.add(InlineKeyboardButton('Kikko Es6', callback_data='dopKikkoEs6'))
dopoborydovanie.add(InlineKeyboardButton('Snakky Jazz', callback_data='dopSnakkyJazz'))
dopoborydovanie.add(InlineKeyboardButton('Snakky Max', callback_data='dopSnakkyMax'))
dopoborydovanie.add(InlineKeyboardButton('Snakky LX', callback_data='dopSnakkyLX'))
dopoborydovanie.add(InlineKeyboardButton('назад', callback_data='exit'))

import sqlite3

def create_db():
# Подключаемся к базе данных или создаем её
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

# Создаем таблицу users (если она не существует)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE  )''')

# Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

def check_user(user_id):
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()

# Если пользователь найден, вернуть True, иначе False
    return result is not None

token = '7808319236:AAHc37Iyv_7cVSDyC026JjSQIRv6JjuNyfk'
bot = telebot.TeleBot('7808319236:AAHc37Iyv_7cVSDyC026JjSQIRv6JjuNyfk')
MODERATOR_USER_ID = "5767007798"

create_db()

@bot.message_handler(commands=['checkme'])
def handle_checkme(message):
    user_id = message.from_user.id

# Проверяем, существует ли пользователь в базе данных
    if check_user(user_id):
        bot.send_message(message.chat.id, "Доступ разрешен")
    else:
        bot.send_message(message.chat.id, "Ваш user_id НЕ найден в базе данных.")

@bot.message_handler(commands=['start'])
def main(message):
    user_id = message.from_user.id
    if check_user(user_id):
        username = message.from_user.username if message.from_user.username else "Неизвестно"
        bot.send_message(
            MODERATOR_USER_ID,  # Отправляем в личные сообщения модератору
            f"""Пользователь: @{username}"""
        )
        bot.send_message(message.chat.id, '''• ВЫБЕРИТЕ ИНТЕРЕСУЮЩИЙ РАЗДЕЛ • ''', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Доступ запрещен")

@bot.callback_query_handler(func=lambda callback: True)

# Название глав над списком вопросов
def callback_message(callback):
    if callback.data == 'one':
        bot.send_message(callback.message.chat.id, 'Процессы, обязанности и правила ВТР', reply_markup=oneglav)
    if callback.data == 'one1':
        bot.send_message(callback.message.chat.id, 'В офисе', reply_markup=one1)
    if callback.data == 'one2':
        bot.send_message(callback.message.chat.id, 'На выезде', reply_markup=one2)
    elif callback.data == 'two':
        bot.send_message(callback.message.chat.id, 'Устройства/Настройки ТА', reply_markup=two)
    elif callback.data == 'fas':
        bot.send_message(callback.message.chat.id,'FAS', reply_markup=fas)
    elif callback.data == 'fasfv':
        bot.send_message(callback.message.chat.id,'FAS ADV', reply_markup=fasfv)
    elif callback.data == 'tcn':
        bot.send_message(callback.message.chat.id,'TCN', reply_markup=tcn)
    elif callback.data == 'three':
        bot.send_message(callback.message.chat.id, 'Платежные системы', reply_markup=three)
    elif callback.data == 'podglavapay':
        bot.send_message(callback.message.chat.id, 'Платежные системы', reply_markup=doppay)
    elif callback.data == 'pay':
        bot.send_message(callback.message.chat.id, 'Монетоприемники', reply_markup=dopmon)
    elif callback.data == 'mei':
        bot.send_message(callback.message.chat.id, 'MEI', reply_markup=three2)
    elif callback.data == 'nri':
        bot.send_message(callback.message.chat.id, 'NRI', reply_markup=three1)
    elif callback.data == 'kupur':
        bot.send_message(callback.message.chat.id, 'Банкнотоприемники', reply_markup=kupur)
    elif callback.data == 'beznal':
        bot.send_message(callback.message.chat.id, 'Безналичные системы', reply_markup=doppay2)
    elif callback.data == 'four':
        bot.send_message(callback.message.chat.id, 'MatiPay', reply_markup=four)
    elif callback.data == 'five':
        bot.send_message(callback.message.chat.id, 'Банковский терминал', reply_markup=five)
    elif callback.data == 'six':
        bot.send_message(callback.message.chat.id, 'App (приложение)', reply_markup=six)
    elif callback.data == 'mdb':
        bot.send_message(callback.message.chat.id, 'MDB', reply_markup=mdb)
    elif callback.data == 'seven':
        bot.send_message(callback.message.chat.id, 'Гидросистема', reply_markup=seven)
    elif callback.data == 'eight':
        bot.send_message(callback.message.chat.id, 'Кофемолка', reply_markup=eight)
    elif callback.data == 'nine':
        bot.send_message(callback.message.chat.id, 'Кофе', reply_markup=nine)
    elif callback.data == 'ten':
        bot.send_message(callback.message.chat.id, 'Кофе-группа', reply_markup=ten)
    elif callback.data == 'eleven':
        bot.send_message(callback.message.chat.id, 'Ошибки ТА', reply_markup=eleven)
    elif callback.data == 'podglava':
        bot.send_message(callback.message.chat.id, 'Кофе-машины', reply_markup=dop)
    elif callback.data == 'twelve':
        bot.send_message(callback.message.chat.id, 'Koro Prime', reply_markup=twelve)
    elif callback.data == 'thirteen':
        bot.send_message(callback.message.chat.id, 'Kaleo', reply_markup=thirteen)
    elif callback.data == 'fourteen':
        bot.send_message(callback.message.chat.id, 'Krea', reply_markup=fourteen)
    elif callback.data == 'fifteen':
        bot.send_message(callback.message.chat.id, 'Bianchi Gaia', reply_markup=fifteen)
    elif callback.data == 'Biepi':
        bot.send_message(callback.message.chat.id, 'Biepi MC1', reply_markup=Biepi)
    elif callback.data == 'sixteen':
        bot.send_message(callback.message.chat.id, 'Общение с клиентом', reply_markup=sixteen)
    elif callback.data == 'seventeen':
        bot.send_message(callback.message.chat.id, 'Инструкции', reply_markup=seventeen)
    elif callback.data == 'videoinstr':
        bot.send_message(callback.message.chat.id, 'Видео-Инструкции', reply_markup=dopvid)
    elif callback.data == 'videoinstr1':
        bot.send_message(callback.message.chat.id, 'Работа с пальмом', reply_markup=videoinstr1)
    elif callback.data == 'okleyka':
        bot.send_message(callback.message.chat.id, 'Работа с пальмом', reply_markup=videoinstr)
    elif callback.data == 'instrta':
        bot.send_message(callback.message.chat.id, 'Инструкции по моделям ТА', reply_markup=instrta)
    elif callback.data == 'dozer':
        bot.send_message(callback.message.chat.id, 'Таблицы доз напитков по аппаратам', reply_markup=dozer)
    elif callback.data == 'catalog':
        bot.send_message(callback.message.chat.id, 'Каталог запчастей', reply_markup=catalog)
    elif callback.data == 'dopoborydovanie':
        bot.send_message(callback.message.chat.id, 'Размещение допоборудования на ТА', reply_markup=dopoborydovanie)
    elif callback.data == 'errorLK':
        bot.send_message(callback.message.chat.id, 'Ошибки в ЛК ТТ', reply_markup=errorLK)

# Кнопки "назад"
    elif callback.data == 'exit':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)

    elif callback.data == 'delete2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)

    elif callback.data == 'delete3':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)

    elif callback.data == 'delete4':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 3)

    elif callback.data == 'delete5':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 3)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 4)

    elif callback.data == 'delete6':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 3)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 4)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 5)

    elif callback.data == 'delete7':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 3)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 4)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 6)

    elif callback.data == 'delete8':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 3)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 4)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 5)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 6)
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 7)

# ОТВЕТЫ

# 1.1 В офисе - кнопки вопроса
    elif callback.data == '1.40':
        bot.send_message(callback.message.chat.id, '''
• сообщить руководителю о ситуации

• закрываем заявку как невыполненную

В конце пальм сам спрашивает - работает дистрибьютор или нет. Заявка остается на карте и нет необходимости создавать новую, дублирующую''')
        bot.send_video(callback.message.chat.id,open('./Palm_video/Закрытие заявки как невыполненная.mp4','rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == '1.1':
        bot.send_message(callback.message.chat.id, '''
• запчасти/продукты получаются по предзаказу, отправленному на склад до 15.00 за день до приезда в офис

• если надо срочно получить запчасть для ремонта ТА день в день, то необходимо подойти к руководителю для решения этого вопроса
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.2':
        bot.send_message(callback.message.chat.id, '''
1. Сделать предзаказ до 15.00 за день до приезда в офис

2. По приезду в офис считать штрих-код «Вход в офис»

3. Визит в кассу для сдачи мешков с инкассацией

4. Руководителю Отдела Сервисного обслуживания для получения списка использованных
запчастей, которые необходимо сдать на склад

5. Визит на склад для сдачи запчастей

6. Визит в Логистику для сдачи/получения путевых листов, для получения списка запчастей,
которые необходимо «посчитать» при проведении инвентаризации

7. Провести инвентаризацию при необходимости

8. Визит в Логистику для закрытия накладной при проведении инвентаризации

9. Визит на склад для получения запчастей

10. Визит в Логистику для сдачи погрузочных листов

11. Считать штрих-код «Выход из офиса»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.3':
        bot.send_message(callback.message.chat.id, '''
«Заказ-наряд» – заявка на изменение цен/ассортимента/установки доп. оборудования в ТА

• закрытие заявки по заказ-наряду вносит ряд изменений в настройках точки продаж, соответствующих изменениям в самом заказ-наряде (тип платежной системы, конфигурация ТП, цены)

• закрытие заявки носит необратимый характер, поэтому, прежде чем ее закрывать, надо быть уверенным, что в наличие есть все для успешного выполнения задачи

• случайное закрытие не допустимо
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.4':
        bot.send_message(callback.message.chat.id,
'Написать комментарий о проделанной работе на ТП, описать причину возникновения неисправности')
        bot.send_video(callback.message.chat.id,open('./Palm_video/Комментарий к заявке.mp4','rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == '1.5':
        bot.send_message(callback.message.chat.id, '''
• заправиться за свой счет, чтобы хватило до следующего рабочего дня. Чек сохранить. При визите в офис написать заявление на возврат денежных средств.
Чек прикрепить к заявлению, которое необходимо отдать офис-менеджеру. Копию чека прикрепить к путевому листу. Дождаться оповещения о возврате денежных средств в кассе

• заправка по топливной карте до 9 часов утра и после 16 часов дня запрещена'''
, protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.6':
        bot.send_message(callback.message.chat.id, '''Согласовать дату своего подъезда в офис с руководителем
''', reply_markup=Exitt)
    elif callback.data == '1.7':
        bot.send_message(callback.message.chat.id, '''
• в первый рабочий день каждого месяца для сдачи мешков с инкассацией и сдачи путевых листов

• в свой день, обозначенный в «Графике приездов в офис выездных сервисных инженеров», для выполнения действий при подъезде в офис
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.8':
        bot.send_message(callback.message.chat.id, '''
В этом случае надо отправить предзаказ на день следующего подъезда согласно «Графику приездов в офис выездных сервисных инженеров».
Если запчасть требуется для выполнения заявки типа «Проблема», то необходимо подойти к руководителю для решения этого вопроса
''', reply_markup=Exitt)
    elif callback.data == '1.9':
        bot.send_message(callback.message.chat.id,
'См. инструкцию «Инструкция действий ТЕХВН при подъезде к ТА», пункт 4.1.а', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.10':
        bot.send_message(callback.message.chat.id, '''
• с помощью терминала

• по погрузочному листу оператора с указанием даты и времени, номера ТП, своего номера по Веге
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.11':
        bot.send_message(callback.message.chat.id, '''4 рабочих дня с момента постановки задачи на «ответственного»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.12':
        bot.send_photo(callback.message.chat.id, open('./Приоритет звонков.jpg','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
1. задымление/ утечка воды

2. ТА выкл/не работает

3. Если на ТА блокирующая ошибка

4. ТА с более высокими показателями продажи

При наличие звонков с разных ТП с одинаковой проблемой ехать в первую очередь туда, где больше средних продаж''', protect_content=True)

        bot.send_photo(callback.message.chat.id, open('./Средние продажи в заявке.jpg','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
При этом не забывать о сроках выполнения работ. Заявка, срок выполнения которой подходит к 8 часам, должна быть в приоритете
''', protect_content=True, reply_markup=Delete4)
    elif callback.data == '1.13':
        bot.send_message(callback.message.chat.id, '''
1. снять статистику

2. ообщить в логистику о том, что была выгружена статистика с Промо

3. выставить цены в «0»

4. тест продаж — снять статистику

При повторном подъезде для включения цен:

1. снять статистику

2. обновить пальм

3. сообщить в логистику о том, что была выгружена статистика с Промо с нулевыми ценами

4. включить цены

5. сделать тест продажи

6. снять статистику
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.14':
        bot.send_message(callback.message.chat.id,
'''Только в том случае, если договоренность с оператором и продукты не будут мешать нормальной работе ТА
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.15':
       bot.send_message(callback.message.chat.id,
'''Написать заявление на отпуск за 14 календарных дней до начала отпуска
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.16':
        bot.send_message(callback.message.chat.id,
'''Сообщить об этом в чат «Операторский отдел vs техники», закрыть заявку с соответствующей отметкой — "ошибка оператора"
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.17':
       bot.send_message(callback.message.chat.id,
'''Руководителю необходимо написать номер ТА и тип платежной системы, которая будет в ТА, к примеру: Та 3002098- замена мэй на нрай, ПС: Nrai + Credit Card
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.18':
        bot.send_message(callback.message.chat.id,
'''14 календарных дней, если не указан иной срок
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.19':
        bot.send_message(callback.message.chat.id, '''
• в конце рабочего дня

• в начале рабочего дня

• при изменении цен во время проведения «Промо»

• для получения актуальной информации из Веги
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.20':
        bot.send_message(callback.message.chat.id, '''
1. Заменить спираль физически на продукте на правильную

2. написать Руководителю отдела сервисного обслуживания или старшему мастеру номер ТП, номер ячейки и какую спираль поставили
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.21':
        bot.send_message(callback.message.chat.id, '''
• оставлять для оператора в ТА бумагу с записанным количеством сделанных тестов

• количество сделанных тестов попадает в Вегу только при снятии статистики

*делать тесты без стакана, только порошки/кофе зерновой нельзя, так как они не считаются по счетчику напитков
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.22':
        bot.send_message(callback.message.chat.id, '''
Программа профилактики поломок - это мероприятия, цель которых заключается в недопущении поломок ТА. Это внеплановые подъезды на ТП и диагностирование ТА, на предмет возможных неисправностей. Включает в себя превентивное ТО, направленное на поддержание ТА в исправном состоянии.
Цель ППП - увеличение продаж, довольный и лояльный клиент, уменьшение количества заявок по проблемам в сети в целом, и повторных в частности.
На начальном этапе выездной техник должен руководствоваться следующим алгоритмом действий:

1. при отсутствии заявок по проблемам, выезжать на ближайшую ТП из списка в соответствующей задаче в Bitrix («ТП, участвующие в программе профилактики поломок»)

2. количество подъездов на каждую ТП - максимум 1 раз в 2 недели (дальше сроки будем корректировать, нужна статистика)

3. осмотр ТА необходимо выполнять полный, включая визуальный осмотр полки бойлера

4. выполнять ТО необходимо по факту текущего состояния узлов, не основываясь на цифры по количеству дней и оставшихся напитков в пальме, в разделе просроченных ТО
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.23':
        bot.send_message(callback.message.chat.id,
'''Напитки настраиваются по соответствующей задаче в Bitrix по таблице, в которой указаны новые параметры КМ в присутствии ЛПР
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.24':
        bot.send_message(callback.message.chat.id,
''''Максимум за 2 месяца до окончания срока годности продукты необходимо сдать на склад
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.25':
        bot.send_message(callback.message.chat.id,
'''Производим в Maga, обязательно выбирая «Повторную погрузку»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.26':
        bot.send_message(callback.message.chat.id, '''
При подъезде к КМ на кофе-поинтах необходимо делать пустую загрузку по пальму в случаях:

• замены цен

• замены системы оплаты

• замены модуля MatiPay

Отписываться в Отдел статистики и аналитики, чтобы они снимали статистику больше не надо.
При выполнении пустой погрузки Вега автоматом статистику снимает
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.27':
        bot.send_message(callback.message.chat.id,'''
Аксессуары это:

• монетоприменик

• купюроприемник

• стакер купюроприемника

• модуль внутренний Matipay

• модуль наружний Matipay

• банковский терминал

• стабилизатор напряжения

• антенна усиленная

• дисплей QR-кода

• модуль телеметрии Telemetron

• стакер купюроприемника

Статус аксессуара необходимо изменить для того, чтобы снятый аксессуар с одного
ТА можно было бы установить на другой ТА.
Для этого необходимо отписаться в чат со складом/руководителю - приложить
фото аксессуара с номером аксессуара, и попросить «изменить статус аксессуара»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.28':
        bot.send_message(callback.message.chat.id, '''
• при закрытии любого заказ-наряда снятие статистики обязательно

• даже если вы ничего не делали физически, в заказ-наряде все равно присутствуют
определенные изменения, отсчет по которым должен вестись в аппарате с момента последней статистики
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.29':
        bot.send_message(callback.message.chat.id, '''
• попросить выдать отсутствующую запчасть

• отметить/записать артикул недостающей запчасти

• получить штрих-код отсутствующей запчасти

• заказать в следующем предзаказе
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.30':
        bot.send_message(callback.message.chat.id, '''
1. запросить у руководителя информацию о новых звонках

2. при отсутствии ответа/обратной связи самостоятельно принять решение, исходя из программы профилактики поломок
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.31':
        bot.send_message(callback.message.chat.id, '''
Парковка оплачивается компанией путем использования в приложении «Парковки Санкт-Петербург» банковской карты,
номер которой выдает Руководитель отдела сервисного обслуживания. В процессе оплаты парковки необходимо делать скриншот чека,
который показывает приложение после каждой оплаты парковки. Скриншот присылать руководителю отдела сервисного обслуживания в начале каждого рабочего дня
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.32':
        bot.send_message(callback.message.chat.id, '''
• если вы не успеваете/не планируете выполнять какую-либо заявку по проблеме после 17.00, то необходимо сообщить об этом руководителю

• работа после 17.00 оплачивается отдельно с повышенным коэффициентом
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.33':
        bot.send_message(callback.message.chat.id, '''
В торговой сети компании Сиба-Вендинг используются следующие сим-карты:

• билайн — отдельно для мати и отдельно для банк терминалов, заблокированы, нужно
разблокировать в личном кабинете билайна самостоятельно

• мегафон — универсальные, не заблокированы

• мтс — универсальные, не заблокированы
''', protect_content=True, reply_markup=Exitt)




# 1.2 На выезде - кнопки вопроса
    elif callback.data == '1.34':
        bot.send_message(callback.message.chat.id,
'''После переделки ТА на другой формат стаканов необходимо написать об этом руководителю для внесения изменений в Веге
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.35':
        bot.send_message(callback.message.chat.id,
'''При подъезде по заявке на ТП, в филиале которой есть еще несколько ТП, вы обязаны проверить на работоспособность все ТП на нем
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.36':
        bot.send_message(callback.message.chat.id, '''
1. фото внутреннего вида ТА

2. фото внешнего вида ТА в режиме готовности

3. скриншот с ЛК MatiPay с информацией о последней БЕЗНАЛИЧНОЙ (по банк терминалу) продаже и уровне связи

4.	фото технического меню банк терминала с уровнем связи (если терминал установлен в ТА)'''
, protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.37':
        bot.send_message(callback.message.chat.id,
'''Указать в пальме куда едете. Нажать кнопку «В пути» в меню соответствующей заявки и указать расчетное время подъезда
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.38':
        bot.send_message(callback.message.chat.id, '''
Посмотреть продажи в ЛК MatiPay. Возможно причина*, по которой заведена заявка устранилась и все работает.

*к примеру, застрявший стакан вытащили и ТА дальше торгует
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '1.39':
        bot.send_message(callback.message.chat.id, '''
Предзаказ - это список того. что вы хотите получить на складе к моменту своего подъезда в офис.
Как вы знате, у каждого из вас есть свой день подъезда в офис. И вот на этот день вам надо будет в течение всей рабочей недели кидать предзаказ.
Он формируется автоматически из используемых вами запчастей в процессе работы. Также в него вы можете добавить сами все, что хотите.
Важный нюанс - отправлять предзаказ надострого перед каждым обновлением пальма, иначе список использованных запчастей пропадет.
Именно поэтому это надо делать в течение всей рабочей недели, а не прямо перед подъездом.
В день своего подъезда вы приезжаете в офис и вас уже будет ждать ящик с собранными запчастями.
Все что нужно сделать - это проверить чтобы все соответствовало погрузочному листу и на всех запчастях были наклеены штрих-кода.
Предзаказ надо делать каждый раз перед обновлением пальма, то есть по сути каждый день.
На ДЕНЬ СВОЕГО ПОДЪЕЗДА
''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Palm_video/Делаем предзаказ.mp4','rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == '1.41':
        bot.send_message(callback.message.chat.id, '''
Кофейные аппараты:

• Вентиляционная группа

Заменить.
Также в это ТО входит замена втулок/сальников миксера.
По пальму провести работу как
«PREV Профилактика - C096 Вентиляционная группа»


• Замена фильтра воды

Проверить. Заменить при необходимости (если грязный)
По пальму провести работу как
«PREV Профилактика - C027 Замена фильтра воды»


• Бойлер кофе-группы

Проверить визуально. При необходимости заменить.
По пальму провести работу как
PREV Профилактика - C014 Бойлер кофе-группы»


• Бойлер растворимых

Проверить визуально. При необходимости заменить.
По пальму провести работу как
«PREV Профилактика - C103 Бойлер растворимых»


• Картридж фильтра водопровода

Заменить.
По пальму провести работу как
«PREV Профилактика - C028 Картридж фильтра водопровода»


• Кофейная группа

Проверить визуально, сделать тесты. При необходимости заменить.
Также в это ТО входит чистка или замена Дозатора кофе.
По пальму провести работу как
«PREV Профилактика - C047 Кофейная группа»


• Кофемолка

Проверить визуально, сделать тесты. При необходимости заменить.
По пальму провести работу как
«PREV Профилактика - C052 Кофемолка»


• Кофейная группа LB

Проверить визуально, сделать тесты. При необходимости заменить.
По пальму провести работу как
«PREV Профилактика - C110 Кофейная группа LB»


• Комплексная очистка

В это ТО входит чистка КМ.
По пальму провести работу как
«PREV Профилактика - C114 Комплексная очистка»


• Контроль настроек

В это ТО входит проверка настроек КМ - обьем напитков и дозы порошка.
По пальму провести работу как
«PREV Профилактика - C116 Контроль настроек»


Снековые аппараты:

• Чистка модуля охлаждения

В это ТО входит чистка СТА.
По пальму провести работу как
«PREV Профилактика - С123 Чистка модуля охлаждения»


Пурифайер/кулер:

• Чист и дезинфекция ТА

В это ТО входит чистка.
По пальму провести работу как
«PREV Профилактика - A919 Чист и дезинфекция ТА»


• Картридж фильтра водопровода

Заменить.
По пальму провести работу как
«PREV Профилактика - C028 Картридж фильтра водопровода»


• Чистка фризера

В это ТО входит чистка самого пурифайера/кулера.
По пальму провести работу как
«PREV Профилактика - C071 Чистка фризера»


• Трубки подачи воды

В это ТО входит чистка подающих воду шлангов и кранов пурифайера/кулера.
По пальму провести работу как
«PREV Профилактика - C094 Трубки подачи воды»


• Бойлер растворимых

Проверить визуально. При необходимости заменить пурифайер/кулер в сборе. На месте не ремонтируем.
По пальму провести работу как
«PREV Профилактика - C103 Бойлер растворимых»
''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Palm_video/Отмечаем правильно ТО.mp4','rb'), protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Palm_video/Замена узла, участвующего в ТО.mp4','rb'), protect_content=True, reply_markup=Delete3)





# 2. Устройства/Настройки ТА - кнопки вопроса
    elif callback.data == '2.1':
        bot.send_message(callback.message.chat.id, '''
В Concerto LB дополнительно присутствует:

• клапан LB

• второй фильтр воды после счетчика воды перед бойлером эспрессо

• два бойлера – бойлер эспрессо и бойлер растворимых напитков

• два счетчика воды

• две верхних помпы
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.2':
        bot.send_message(callback.message.chat.id, '''
• Kikko Max ToGo – держатель крепится двумя саморезами в крышу ТА + нижняя часть приклеивается черным двусторонним скотчем

• Kikko Es6 mini ToGo – отпиливается «козырек» держателя, перевешивается крышка держателя и держатель приклеиваются на черный двусторонний скотч
''', reply_markup=Exitt)
    elif callback.data == '2.3':
        bot.send_message(callback.message.chat.id, '''
• отличаются объемом стакана

• видом засыпаемого кофе

• внешним видом ТА

• температурой заварки кофе

•	другая раскладка напитков
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.4':
        bot.send_message(callback.message.chat.id, '''
1. взвесить на электронных весах, то что выдает ТА до калибровки и записать в таблицу «Таблица для измерения доз порошков»

2. Калибровка шнеков – указать ТА сколько он выдает порошка из каждого контейнера

3. Калибровка доз порошков непосредственно каждого напитка

Особенность: в Opera, Concerto&Canto калибровка происходит на медленной скорости вращения шнеков и на большой.
Все действия по калибровке доз проводятся с помощью электронных весов. Измерения проводятся на полной выдаче напитков
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.5':
        bot.send_message(callback.message.chat.id, '''
Телеметрия передает данные через Matipay о состоянии ТА, и в случае поломки ТА автоматически заводит звонок. Если ТА выходит в рабочий режим и ошибка пропадает, то звонок автоматически закрывается.
Подключается через разъем rs232, который находится на ТА и на проводе от Matipay.

ТА не поддерживающие телеметрию – Bianchi (все модели), Colibri (нет актуальной прошивки), FAS, Kikko Max ToGo (зависают в нагреве)

Включение:

Concerto LB, Opera, Canto LB/Big Cup/Double Cup, Jazz, Melodia:

1. техн. 6.2.Х

2. communicat. protocol DDCMP ENHANCED

3. передача данных TELEMETRY

4. EVADTS TYPE ENHANCED

5. serial baudrate 2400

Kikko LB/ES/Max, Snakky LX/Max, Koro Prime:

1. техн. 5.3.Х

2. код доступа 0000

3. код безопасности 0000

4. протокол EVADTS DDCMP

5. режим ALWAYS EVADTS

6. тип ENHANCED

7. serial baudrate 2400

8. undefined length on/вкл

Проверка:

1. поднимаем поплавок в ведре отходов

2. ждем пару секунд

3. заходим на сайт мати, вбиваем номер ТА

4. в разделе Alarms смотрим чтобы появилась ошибка'''
, protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.6':
        bot.send_message(callback.message.chat.id, '''
• Подключиться по приложению

• Нажать на кнопку открытия двери, расположенную на задней стенке аппарата слева вверху, если стоять лицом к ТА
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.7':
        bot.send_message(callback.message.chat.id, '''
1. Предыдущая функция

2. Размолоть и выдать дозу кофе

3. Выдать сахар

4. Автотест

5. Следующая функция

6. Повернуть кофейный модуль

7. Выдать чашку

8. Опустошить воздушную пробку'''
, protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.8':
        bot.send_message(callback.message.chat.id, '''
Потенциометр на плате кнопок'''
, protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.9':
        bot.send_message(callback.message.chat.id, '''
• сделать несколько полных тестов разных напитков в стакан

• убедиться в правильности работы ТА, выдачи всех ингредиентов и аксессуаров
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.10':
        bot.send_message(callback.message.chat.id, '''
• в истории ошибок в меню ТА

• на сайте мати в разделе Alarms/Events
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.11':
        bot.send_message(callback.message.chat.id, '''
• отключить замок лотка

• переделать питание подсветки – отключить заводскую плату управления подсветкой и подключить блок питания 12 В'''
, protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.12':
        bot.send_message(callback.message.chat.id, '''
• в настройках ТА стоит параметр выдачи размешивателей по очереди – сначала выдает полностью с одного ряда, потом с другого

• в одном из рядов застрял размешиватель

• в одном из рядов сломан выбрасыватель размешивателей, отломана направляющая с кулачком
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.13':
        bot.send_message(callback.message.chat.id, '''
• отсутствует пружина колеса бункера

• отсутствует колесо бункера

• прогнулась ось колеса бункера, что препятствует зацеплению верхнего и нижнего колес

• износились втулки/резинки на оси колеса бункера, в следствие чего появился люфт колеса бункера и периодически отсутствует зацепление верхнего и нижнего колес
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.14':
        bot.send_message(callback.message.chat.id, '''
Поставить "1" в меню 73 (включение фотоэлементов) на все ячейки
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.15':
        bot.send_message(callback.message.chat.id, '''
1. Скопировать с компьютера на UPKEY необходимую версию прошивки и настроек

2. Перед прошивкой выключить ТА

3. Вставить UPKEY в плату

4. Включить ТА

5. Дождаться завершения прошивки

6. Выключить ТА

7. Вытащить UPKEY

8. Включить ТА

9. Сделать инициализацию

10. Вставить UPKEY

11. Скопировать настройки на ТА

12. Откалибровать шнеки порошков
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.16':
        bot.send_message(callback.message.chat.id, '''
1. платы меняем на любом аппарате в сборе - ЦПУ и плату управления

2. платы прошиваем в офисе ВСЕГДА, вне зависимости от того, что на ней написано, и что вам утверждают другие сотрудники

3. на апкей заливаем прошивку + настройки для соответствующего ТА, на котором эти платы будут меняться
''', reply_markup=Exitt)
    elif callback.data == '2.17':
        bot.send_message(callback.message.chat.id, '''
1. напряжение в сети

2. предохранители сгорели

• компрессор

• вентиляторы обдува

• блок питания светодиодной ленты

• реле вкл компрессора

• неисправен замок лотка – он должен быть выключен

Предохранители в норме, ТА вкл, но не морозит - вентилятор обдува испарителя не работает
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.18':
        bot.send_message(callback.message.chat.id, '''
После установки двойной спирали необходимо сделать:

• перепривязку цен к номеру выбора в снеке в меню 3

• отображение цен на дисплее в меню 5
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.19':
        bot.send_message(callback.message.chat.id, '''
Если мотор контейнера растворимых напитков (порошков) на Canto/Maestro делает полоборота
и перестает дальше работать, то одной из причин может быть мотор миксера. Его необходимо заменить
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.20':
        bot.send_document(callback.message.chat.id, open(r"./FAS_пособие по настройке.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.21':
        bot.send_message(callback.message.chat.id, '''
Кратковременно нажать на кнопку программирования на плате CPU. Сделать выбор тестируемого продукта на клавиатуре и нажать «В».
Для выхода из режима тестирования продукта закрыть дверь или нажать «А»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.23':
        bot.send_document(callback.message.chat.id, open(r"./Потребляемая мощность ТА.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.24':
        bot.send_document(callback.message.chat.id, open(r"./Подключение датчика наличия стаканов в Canto.jpg", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.25':
        bot.send_document(callback.message.chat.id, open(r"./Подключение опт датчика в Кончерто.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.26':
        bot.send_document(callback.message.chat.id, open(r"./Высоты полок для ТА FAS 09.2024.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.27':
        bot.send_document(callback.message.chat.id, open(r"./Дозировки воды для Kikko Es6 и Kikko Max.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '2.28':
        bot.send_message(callback.message.chat.id, '''
Залип микровыключатель размешивателей в одном из крайних положений. Фото самого микровыключателя:''',protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Canto_razmesh/Canto_razmesh.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Canto_razmesh/Canto_razmesh1.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Canto_razmesh/Canto_razmesh2.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Canto_razmesh/Canto_razmesh3.jpg", 'rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
Почистить микровыключатель. Проверить работу по видео ниже (ТА делает автотест)''',protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Canto_razmesh/Canto_razmesh.mp4','rb'), protect_content=True, reply_markup=Delete7)
    elif callback.data == '2.29':
        bot.send_message(callback.message.chat.id, '''
Проявляется следующим образом - после копирования настроек на ТА с другого ТА с помощью Up-key, при выдаче напитка
носики и сахар одновременно движутся и сталкиваются в опеределенной точке.
В итоге аппарат уходит в ошибку «носики».
Необходимо заливать настройки скопированные только с компьютера на Up-key, а не сдругого ТА в сети''', protect_content=True, reply_markup=Exitt)





#FAS ADV - кнопки ответа
    elif callback.data == 'fasfv1':
        bot.send_document(callback.message.chat.id, open(r"./FAS_ADV/Установка Price-Holding в FAS ADV.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'fasfv2':
        bot.send_message(callback.message.chat.id, '''
В поле «Customization» вбить кодовое слово - «COLDMACHINERUS»''',protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./FAS_ADV/Русификация меню покупателя FAS ADV.pdf", 'rb'), protect_content=True, reply_markup=Delete2)





#TCN - кнопки ответа
    elif callback.data == 'tcn.1':
        bot.send_document(callback.message.chat.id, open(r"./TCN/Инструкция по эксплуатации TCN.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'tcn.2':
        bot.send_document(callback.message.chat.id, open(r"./TCN/Технические характеристики TCN.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'tcn.3':
        bot.send_document(callback.message.chat.id, open(r"./TCN/Высоты полок TCN 10.2024.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'tcn.4':
        bot.send_message(callback.message.chat.id, '''000000''',protect_content=True, reply_markup=Exitt)



# 3. Платежные системы - кнопки ответа
    elif callback.data == '3.8':
        bot.send_message(callback.message.chat.id, '''
Множитель, на который умножается  номинал принимаемых денег для того, чтобы можно было устанавливать необходимую десятичную точку (ДТ). Базовая единица должна быть установлена одинаково на как в ТА, так и во всех платежных устройствах, подключенных к нему.
Пример: клиент вставляет в ТА купюру 50р. Нам необходимо, чтобы они отображались с ДТ 2. Если базовую единицу не трогать, то на дисплее сумма отобразится как 0,50 р.  Ставим Базовую единицу 100.
50 х 100 = 5000, ДТ = 2, поэтому  получаем 50,00
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.10':
        bot.send_message(callback.message.chat.id, '''
• «Executive Price Holding» - все команды поступают от платежной системы. Протокол Executive поддерживается подавляющим большинством новых и б/у автоматов.
В этом случае все цены устанавливаются на монетоприемнике, а каждому продукту на торговом автомате присваивается ценовая линия.
При этом в данном случае, перед передачей значения ценовой линии в монетоприемник, оно делится на scaling factor.
Общение автомата с платежкой происходит следующим образом:
Автомат сообщает: "выбран товар: ценовая линия / scaling factor"
Монетоприемник анализирует стоимость этой ценовой линии, далее все, как в Executive standard:
Вы подошли и опустили энную сумму в монетоприемник. Монетоприемник ее принял, подсчитал ее значение и вывел информацию о ней на дисплей,
то есть выдал несколько управляющих команд по линии Тх (см. рис. 1). Далее вы нажимаете кнопку интересующего Вас продукта.
Торговый автомат по линии Rx отправляет некоторую последовательность сигналов, таким образом сообщая монетоприемнику, что у него выбран, например, кофе эспрессо.
Монетоприемник анализирует информацию о цене данного продукта и выдает автомату по линии Тх последовательность команд, суть которых сводится к следующему:
выдать, или не выдать, но показать недостающую сумму, или показать стоимость данного товара. Если с кредитом все в порядке, и пошла команда от монетоприемника на выдачу товара,
торговый автомат начинает выдачу, о чем сообщает монетоприемнику. Получив этот сигнал, монетоприемник производит подсчет необходимой сдачи. Далее в зависимости от того,
как настроена функция продажи (одиночные продажи - выдача сдачи после выбора товара, множественные продажи - остаточный кредит высвечивается на дисплее),
происходит либо выбор товара на сумму остаточного кредита, либо нажатием кнопки "получение сдачи" покупатель инициирует выдачу сдачи.
В альтернативном варианте автомат, вычитает стоимость товара из суммы кредита. После выдачи товара автомат посылает сигнал монетнику:
выдача товара прошла удачно (или неудачно); в первом случае всё возвращается в начальное положение, во втором - монетник выдает стоимость товара сдачей.

• «MDB» - в данном случае мозгом платежной системы является контроллер торгового автомата.
Все устройства (монетоприемник, банкнотоприемник, системы безналичной оплаты) подсоединяются к общей шине (набор проводов).
При включении торгового автомата (ТА), контроллер ТА производит опрос по этой шине и таким образом узнает о наличии различных платежных устройств в системе.
После этого ТА непрерывно опрашивает каждое устройство и узнает его состояние.
Например, Вы подошли к автомату и опустили 10 рублей в банкнотоприемник; ТА последовательно опрашивает каждый компонент платёжной системы одним вопросом: "у тебя что?"
Монетник отвечает: "у меня ничего", то же самое отвечает и система безналичной оплаты.
А вот банкнотоприемник ответит: "у меня 10 рублей". ТА проанализирует ответ и выдаст команду: "принять" или "не принять" банкноту.
После принятия купюры Вы выбираете напиток, ну, предположим, за 6 рублей; ТА его Вам выдаст, после чего даст команду монетоприемнику выдать 4 рубля сдачи.
В общем, главным думающим элементом в этом случае является торговый автомат.

• «Executive Standard» - не используется

• «BDV» - применяется только в Германии, похож на «Executive Price Holding»

• «ValidPulse» - пульсами передает сколько денег принял ТА. Не используется
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.11':
        bot.send_message(callback.message.chat.id, '''
1. При первом снятии статистика снимается со старого монетоприемника, в ней фиксируются все продажи и при этом обнуляется файл статистики аудит-модуля

2. При втором снятии статистики с нового монетоприемника (после тестовой продажи, при которой создается новый файл аудита) фиксируется правильность настройки монетоприемника, установки цен и загрузки мелочи для сдачи
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.12':
        bot.send_message(callback.message.chat.id, '''
Чтобы исключить прием старых 5 рублевых монет необходимо установить монетоприемник на MEI
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.19':
        bot.send_message(callback.message.chat.id,'''
Частичная оплата товара наличными и безналичными средствами запрещена.
Чтобы исключить данный вид оплаты необходимо установить монетоприемник MEI с выставленной настройкой

• Optsii Executive - Cash Disables Card – Da
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.22':
        bot.send_message(callback.message.chat.id, '''
Работа нескольких устройств на одном кэшлессе  невозможна,  потому что:

• каждому устройству заранее присваивается свой идентификатор обмена данными, который соответствует  определенному адресу на шине MDB (номеру кэшлесс)

• при одновременном подключении нескольких устройств на один кэшлесс ТА/СТА/КМ или монетоприемник не смогут правильно идентифицировать устройство, с которым происходит обмен данными
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.28':
        bot.send_message(callback.message.chat.id, '''
Глюк прошивки ТА (обычно СТА). Установить монетоприемник MEI, выставить следующую настройку:

• Безналичные системы - основное меню - pre-selection — net(выкл)

На FAS работать данная настройка не будет
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.29':
        bot.send_message(callback.message.chat.id, '''
Необходимо включить следующую настройку в монетприемнике MEI:

• Безналичные системы - основное меню - pre-selection - da(вкл)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.32':
        bot.send_message(callback.message.chat.id, '''
• нет связи ТА с платежной системой - проверить провода соединения платежной системы и ТА

• неправильно выставлена платежная система в настройках ТА

• платежная система неисправна

• на плате CPU микровыключатель MDB стоит в положении «On» (вкл режим MDB)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.33':
        bot.send_document(callback.message.chat.id, open(r"./Платежные системы и Cashless.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '3.34':
        bot.send_message(callback.message.chat.id, '''
• при изменении конфигурации снека или кофейного аппарата

• при любом вмешательстве в монетоприемник (цены/настройки и прочее), чтобы не потерять данные о продажах, если что-то пойдет не так

• при замене батарейки аудита в NRI

При установке допоборудования (АПП, банк терминал, QR дисплей, Oscar Reader), если это не влечет за собой вмешательств в монетоприемник, статистику снимать НЕ НАДО
''', protect_content=True, reply_markup=Exitt)





# 3.1.1 Платежные системы - NRI - кнопки ответа
    elif callback.data == 'nri.2':
        bot.send_message(callback.message.chat.id, '''
Проверить:

• петли передней крышки валидатора.  При наличии трещин обязательно замена монетоприемника

• оптические датчики определения диаметра монет под передней крышкой валидатора – визуально (все должно быть чистым) и программно, через меню «Henri» программатора NRI

• оптические датчики всех туб, через меню «Diagnostic» программатора NRI

• работу моторедукторов узла выдачи сдачи, путем выгрузки поочередно нескольких монет из каждой тубы (проверка на ошибку «CoinJam»)

• версию прошивки модулей Audit, Changer. Перепрошить, если устаревшая версия прошивки через меню «Henri» программатора NRI
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.3':
        bot.send_message(callback.message.chat.id, '''
Основное отличие заключается в способе контроля туб монетоприемника:

• NRI – за пополнение монетоприемника отвечают оптические датчик

• MEI – за пополнение монетоприемника отвечают ультразвуковые датчики

Меньше туб, чем в NRI. Меню на русском транслите, в NRI полностью на английском языке.
Монетоприемники MEI предпочтительнее ставить в ТА, которые будут стоять в грязных помещениях (цеха заводов, уличные ТА и тп)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.4':
        bot.send_message(callback.message.chat.id, '''
• Разъем питания EXE

• Провод EXE

• Провод MDBPeripheral

• Провод MDB
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.5':
        bot.send_message(callback.message.chat.id, '''
Через программатор NRI в меню Diagnostic:

• Filling level sensors, left

• Filling level sensors, middle

• Filling level sensors, right

Чем выше значение, тем лучше. Наличие знака «1» рядом с любым значением сенсоров о том, что сенсоры неисправны или загрязнены или загрязнена кассета
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.6':
        bot.send_message(callback.message.chat.id, '''
Батарейка аудит-модуля позволяет сохранять всю информацию аудита автономно при отсутствии питания сети.

При замене батарейки необходимо:

1. инкассировать ТА, снять статистику

2. заменить батарейку на плате аудит-модуля под задней крышкой монетоприемника

3. обнулить в монетоприемнике аудит/статистику в соответствующем меню

• «Settings» - «AuditModule» - «Machine number» - вбить код обнуления аудита «979899» - нажать «OK» - нажать «EXIT»

4. перезагрузить ТА

5. после этого зайти в меню аудита и удостовериться, что все данные обнулились: «Audit» - «Vends» - «Sales of all payment sources» - везде должны стоять нули

6. если не все обнулилось, то зайти в меню программатора «Henri», нажав кнопку с нарисованным ежом. Далее «B-Extent. func.» - «A-c2 stat. data» - «B-delete».

7. после этого вернуться в меню «Machine number» и вбить номер ТА

8. перезагрузить ТА

9. сделать тестовую продажу

10. снять статистику

При замене батарейки аудита-модуля выгружать/загружать разменные деньги в кассете не требуется.

Симптомы разряженной батарейки аудита в монетприемнике NRI:

• не обнуляется предыдущая статистика

• различные символы (не номер ТА) в поле «Machine number»

• напряжение 2,8В или меньше
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.7':
        bot.send_message(callback.message.chat.id, '''
• отщелкнулась задняя прозрачная крышка валидатора («головы»)

• не работают оптические датчики определения диаметра монеты. Передернуть шлейф датчиков под задней прозрачной крышкой валидатора

• сломалась петля крепления передней крышки валидатора. Замена монетоприемника
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.8':
        bot.send_message(callback.message.chat.id, '''
Должно отображаться  три прайса в каждой линии, в настройках надо выставить 3х75 в противном случае NRI начинает продавать по рандомным ценам (7р, 9р и так далее)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.9':
        bot.send_message(callback.message.chat.id, '''
Стоит прошивка «Premium», села батарейка аудита.  В этой прошивке код монетоприемника хранится в энергонезависимой памяти.
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.10':
        bot.send_message(callback.message.chat.id, '''
Выскочил кожух окна выдачи сдачи из крепления и перекрыл щель в монетоприемнике, через которую монеты падают в ведро для мелочи. Монеты не выпадают и начинают накапливаться за задней стенкой монетоприемника, пока не доходят до верхних оптических датчиков, и NRI перестает принимать деньги
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.11':
        bot.send_message(callback.message.chat.id, '''
NRI корректно работает только на Cashless 1. На Cashless 2 может продавать по рандомным ценам

На Cashless 1 работает следующее оборудование:

• NRI + Vendotek Lite

• NRI + Vendotek V3/VN

• NRI + APP (Приложение/Модуль внешний) (в настройках платежной системы ТП выставить NRI+MSK)

Меню установки цен в NRI/Cashless:

Price 001:
Cash      0045    наличная цена
List 1    0000    Cashless 1
List 2    0000    Cashless 2 (не используется)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.12':
        bot.send_document(callback.message.chat.id, open(r"./Настройка NRI.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.13':
        bot.send_document(callback.message.chat.id, open(r"./Замена NRI.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'nri.14':
        bot.send_message(callback.message.chat.id, '''
• зайти в меню «Henri»

• A - FW update

• D - Audit

• подтвердить прошивку E - Yes

• ждать окончания прошивки

• выйти из меню прошивки F - Exit

• перейти в меню программирования «Menu»

• E - Settings

• листать вниз до пункта «Audit module» и зайти в него

• в пункте «Set system Date» - выставить текущую дату

• в пункте «Set system Time» - выставить текущее время

''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Прошивка аудита NRI+дата и время.mp4','rb'), protect_content=True, reply_markup=Delete2)





# 3.1.2 Платежные системы - MEI - кнопки ответа

    elif callback.data == 'mei.2':
        bot.send_message(callback.message.chat.id, '''
Проверить:

• чистоту валидатора

• наличие ошибок через меню монетоприемника «Oshibki»

• ход шторок, распределяющих монеты в валидаторе. При попытке нажать на любую шторку, ход должен быть мягким и до упора. При обнаружении заеданий необходима замена монетоприемника для его ремонта в условиях мастерской
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mei.3':
        bot.send_message(callback.message.chat.id, '''
Основное отличие заключается в способе контроля туб монетоприемника:

• NRI – за пополнение монетоприемника отвечают оптические датчик

• MEI – за пополнение монетоприемника отвечают ультразвуковые датчики

Меньше туб, чем в NRI. Меню на русском транслите, в NRI полностью на английском языке.
Монетоприемники MEI предпочтительнее ставить в ТА, которые будут стоять в грязных помещениях (цеха заводов, уличные ТА и тп)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mei.4':
        bot.send_message(callback.message.chat.id, '''
• Разъем питания EXE

• Провод EXE

• Провод MDBperipheral

• Провод MDB

• Провод audit
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mei.5':
        bot.send_message(callback.message.chat.id, '''
Необходимо включить функцию Cashsale в настройках безнала
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mei.6':
        bot.send_message(callback.message.chat.id, '''
MEI корректно работает c Cashless 1 и Cashless 2. Используется там, где необходимо наличие двух безналичных систем одновременно (MEI+Cashless 1+Cashless 2):

• MEI + Vendotek V3/VN (Cashless 1) + APP (Приложение/Модуль внешний) (Cashless 2)

• MEI + Oscar Reader (Cashless 1) + APP (Приложение/Модуль внешний) (Cashless 2)

При отсутствии монетоприемника NRI допускаются следующие варианты установки:

• MEI + Vendotek Lite (Cashless 1)

• MEI + Vendotek V3/VN (Cashless 1)

• MEI + APP (Приложение/Модуль внешний) (Cashless 2)

Меню установки цен в MEI/Cashless:

Beznal tseny - Cashless 1
Card 2 prices - Cashless 2
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mei.7':
        bot.send_document(callback.message.chat.id, open(r"./Настройка MEI.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mei.7':
        bot.send_document(callback.message.chat.id, open(r"./Замена MEI.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 3.2 Купюроприемники вопросы - кнопки ответа

    elif callback.data == 'kup.2':
        bot.send_message(callback.message.chat.id, '''
• не исправен купюроприемник

• в настройках монетоприемника стоит включенной опция «Escrow» - если клиент придумал, то при нажатии на кнопку сдачи, купюра ему вернется. В ТА нашей сети эта функция выключена

• купюроприемник стоит в режиме работы «Пульс». При этом не будет отображаться кредит и не будет укладываться купюра в стакер
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'kup.3':
        bot.send_message(callback.message.chat.id, '''
Купюроприемник стоит в режиме работы «Пульс». При этом не будет отображаться кредит и не будет укладываться купюра в стакер
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'kup.1':
        bot.send_message(callback.message.chat.id, '''
Десятичная точка – количество нулей после точки, отображаемых в кредите/цене на дисплее. Обычно используется «0» или «2».
Десятичная точка должна быть одинаково выставлена как на ТА, так и в монетоприемнике и купюроприемнике.
Банкнотоприемники - выставляем десятичную точку «2»:

• MEI – 6 переключатель ВЫКЛ

• CashCode – 5 переключатель под крышкой ВЫКЛ

• CashCodeSMV – 4 переключатель ВКЛ

• ICT – 1 переключатель из 4х под крышкой ВКЛ
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'kup.4':
        bot.send_message(callback.message.chat.id, '''
Выкл-вкл 4й дип-переключатель
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'kup.5':
        bot.send_message(callback.message.chat.id, '''
Новых прошивок нет, поэтому отключаем прием купюр больше 100р ДИП-выключателями на боковой стороне банкнотоприемника (они подписаны):

• ICT A7 – 4 и 5

• MEI – тестируем, в зависимости от прошивки может вообще не принимать

• SMW – 5 и 6

• CashCode – 4 и 5
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'kup.6':
        bot.send_message(callback.message.chat.id, '''
Проверить 6й дип-переключатель. Он отвечает за десятичную точку. Должен быть включен (десятичная точка 1).
3й и 8й дип-переключатели должны быть выключены при этом
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'kup.7':
        bot.send_message(callback.message.chat.id, '''
• застряла купюра

• грязный светоотражатель приема купюр. Почистить''', protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Mei_otrazh/mei_otrazh1.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Mei_otrazh/mei_otrazh2.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Mei_otrazh/mei_otrazh3.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Mei_otrazh/mei_otrazh4.jpg", 'rb'), protect_content=True, reply_markup=Delete5)





# 3.3.1 Безналичные системы - Matipay - кнопки ответа
    elif callback.data == '4.1':
        bot.send_message(callback.message.chat.id, '''
Модуль телеметрии для передачи данных о продажах, ошибках ТА''', reply_markup=Exitt)
    elif callback.data == '4.2':
        bot.send_message(callback.message.chat.id, '''
Приложение для работы с устройствами MatiPay на Android (доступно для загрузки из Google Play) для смартфонов.

!!! Создавать прошивку для Matipay с Vendotek Lite в данном приложении НЕТ ВОЗМОЖНОСТИ !!!

Создание возможно только через ЛК на сайте https://vendingapp.matipay.com''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Приложение Matitech.mp4','rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == '4.3':
        bot.send_message(callback.message.chat.id, '''
• зависает модуль при обновлении – перезагрузить нажатием кнопки на модуле

• не ловит сеть – установить усиленную антенну, вставить сим-карту МТС, вывести комплектную антенну на улицу

• не приходят данные о наличных или безналичных (до этого приходили) продажах – замена модуля

• не приходят данные о безналичных (до этого не приходили тоже) продажах – замена интерфейсного кабеля на доработанный''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.5':
        bot.send_message(callback.message.chat.id, '''
Используется  другой модуль Matipay. Он может устанавливаться только в «Умные холодильники»

При этом:

• прошивку и конфигурацию можно скачать с сайта Matipay только при создании устройства

• скачать прошивку и конфигурацию для действующего устройства можно только в приложении MatiTech
для смартфонов на Android (доступно для загрузки из Google Play) во вкладке «Сбросить карту SD»''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.7':
        bot.send_message(callback.message.chat.id, '''
Cashless 1

• TA c NRI+App (MSK)

• TA с Vendotek Lite

• Kora FM с Vendotek Lite или App

• Kora FM/Krea/Kaleo без Vendotek Lite/App/Vendotek V3/VN (КМ для HoReCa/OSC)

• Krea/Kalea с Vendotek Lite или App

Cashless 2

• TA без Vendotek V3/VN/Vendotek Lite/App

• TA с App/Vendotek V3/VN

• Kora FM с Vendotek V3/VN

• Krea/Kalea с Vendotek V3/VN

• Krea/Kalea с Vendotek V3/VN и App''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./cashless.mp4','rb'), reply_markup=Delete2)
    elif callback.data == '4.8':
        bot.send_message(callback.message.chat.id, '''
Проверить уровень связи можно в ЛК MatiPay на странице модуля в разделе «Device State». Минимальный уровень - 12.
Повысить уровень сигнала можно путем замены сим-карты на другого оператора или установки внешней усиливающей антенны''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.9':
        bot.send_message(callback.message.chat.id, '''
1. отключить питание от сети

2. отключить аккумулятор

3. дождаться, когда погаснут все светодиоды

4. подключить все обратно*

5. удостовериться, что модуль вышел на связь на ЛК MatiPay

подключить все обратно* - обратно подключить аккумулятор только в случае, если в паре с модулем MatiPay стоит внешний модуль Matipay (App, Приложения)

Прошивать модуль Matiрay нельзя, так как пропадет вся информация о продажах. Данное действие выполнять только после согласования с руководителем''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.10':
        bot.send_message(callback.message.chat.id, '''
в разделе Alarms/Events''', reply_markup=Exitt)
    elif callback.data == '4.11':
        bot.send_document(callback.message.chat.id, open(r"./Проверка Matipay.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.12':
        bot.send_document(callback.message.chat.id, open(r"./Создание_редактирование устройств мати 16.03.24.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.13':
        bot.send_message(callback.message.chat.id, '''
• Matipay может не загружаться из-за некорректно работающего внешнего модуля приложения (Апп) - заменить

• антенна не подключена

• сим-карта заблоокирована

• в помещении плохой уровень связи''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.14':
        bot.send_message(callback.message.chat.id, '''
• выключаем устройство Matipay

• достаем карту памяти, вставляем в смартфон и удаляем с нее всю информацию

• заходим в приложение Matitech

• удаляем действующее устройство

• создаем новое - «добавить Новый модуль» - «Полное устройство»

• копируем файлы на карту памяти

• карту памяти вставляем обратно в модуль Matipay. Включаем Matipay

• возможно понадобится один раз перезагружать Matipay - первый раз (после включения) устанавливается прошивка, второй раз - конфигурация
''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Удаление и создание Matipay_App.mp4','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
проверяем, что процесс идет - желтый кружочек означает, что обновление в процессе''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Ждем обновление.mp4','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
• проверяем, что прошивка и конфигурация встали - синие кружки с галочкой на «Статус прошивки» и «Статус параметров»

• проверяем «Качество сигнала» - не ниже 10

• делаем тестовую продажу продажу за наличные/по приложению/по банковской карте

  Видим их отображение -  синие кружки с галочкой на:

  • «Считывание продаж наличными»

  • «Считывание продаж с ключами» - это продажа по банковской карте

  • «Считывание продаж по приложению с телеметрии» и «Считывание продаж по приложению со смартфона» - должно совпадать''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Проверка работы и продажа.mp4','rb'), protect_content=True, reply_markup=Delete6)
    elif callback.data == '4.15':
        bot.send_message(callback.message.chat.id, '''
Создать новое устройство Matipay + Vendotek Lite возможно только через личный кабинет на сайте https://vendingapp.matipay.com

• заходим на сайт https://vendingapp.matipay.com в раздел «Телеметрия» - «Список устройств»

• находим и деактивируем устройство Matipay

• создаем новое устройство Matipay

• скачиваем архив с прошивкой и конфигурацию''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Matipay+Vendotek_Lite/Создаем устройство Mati+Lite.mp4','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
• достаем карту памяти, вставляем в смартфон и удаляем с нее всю информацию

• извлечь из скачанного архива прошивку

• копируем скачанные прошивку и файл конфигурации на карту памяти. Файл конфигурации должен именоваться CONFIG.INI

• карту памяти вставляем обратно в модуль Matipay. Включаем Matipay

• возможно понадобится один раз перезагружать Matipay - первый раз (после включения) устанавливается прошивка, второй раз - конфигурация''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Matipay+Vendotek_Lite/Скидываем на карту прошивку.mp4','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''

• проверяем, что прошивка и конфигурация встали - синие кружки с галочкой на «Статус прошивки» и «Статус параметров»

• проверяем «Качество сигнала» - не ниже 10

• делаем тестовую продажу продажу за наличные/по приложению/по банковской карте''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Matipay+Vendotek_Lite/Запускаем и проверяем.mp4','rb'), protect_content=True, reply_markup=Delete6)
    elif callback.data == '4.16':
        bot.send_message(callback.message.chat.id, '''
• выключаем устройство Matipay

• достаем карту памяти, вставляем в смартфон и удаляем с нее всю информацию

• заходим в приложение Matitech

• удаляем действующее устройство

• создаем новое - «Добавить новый модуль» - «Только телеметрия»

• Cashless выставляем в зависимости от оборудования (см. пункт «Cashless при создании нового уcтройства MatiPay»)

• копируем файлы на карту памяти

• карту памяти вставляем обратно в модуль Matipay. Включаем Matipay

• возможно понадобится один раз перезагружать Matipay - первый раз (после включения) устанавливается прошивка, второй раз - конфигурация''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Создаем устройство Mati.mp4','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
проверяем, что процесс идет - желтый кружочек означает, что обновление в процессе''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Ждем обновление.mp4','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
• проверяем, что прошивка и конфигурация встали - синие кружки с галочкой на «Статус прошивки» и «Статус параметров»

• проверяем «Качество сигнала» - не ниже 10

• делаем тестовую продажу продажу за наличные/по приложению/по банковской карте

  Видим их отображение -  синие кружки с галочкой на:

  • «Считывание продаж наличными»

  • «Считывание продаж с ключами» - это продажа по банковской карте

  • «Считывание продаж по приложению с телеметрии» и «Считывание продаж по приложению со смартфона» - должно совпадать''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Проверка работы и продажа.mp4','rb'), protect_content=True, reply_markup=Delete6)
    elif callback.data == '4.17':
        bot.send_video(callback.message.chat.id,open('./Прошивка карты памяти Matipay на Iphone.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '4.18':
        bot.send_message(callback.message.chat.id, '''
• «Телеметрия» - «Список устройств» - вбиваем номер ТА/ТП/модуля внутреннего

• нажимаем на номер модуля внутреннего

• переходим во вкладку «Electronic detections»

• во вкладке «Device state» смотри время последних продаж

  • наличными

  • ключами (банковский  терминал)

  • по приложению с телеметрии/со смартфонов

• карту памяти вставляем обратно в модуль Matipay. Включаем Matipay''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./проверка продаж Matipay.mp4','rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == '17.2':
        bot.send_document(callback.message.chat.id, open(r"./Установка аудит-кабеля в MEINRI для снятия статистики через Matipay.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '17.22':
        bot.send_document(callback.message.chat.id, open(r"./Установка аудит-кабеля в MEINRI для снятия статистики через Matipay(rus).pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 3.3.2 Безналичные системы - Банковский терминал - кнопки ответа
    elif callback.data == '5.1':
        bot.send_message(callback.message.chat.id, '''
• не ловит сеть – установить усиленную антенну, вставить сим-карту МТС/Мегафон, вывести комплектную антенну на улицу

• перезагружается ТА или уходит в ошибку «Монетоприемник» после каждой покупки по банк терминалу – неверно выставлено время удержания цены в настройках платежной системы. Время должно быть выставлено так, чтобы банк терминал и ТА переходили из режима продажи в режим ожидания одновременно

• не проходит покупка/не удалось купить продукт – не успели совершить покупку в отведенное время (время удержания цены), плохая связь с банком. Попытаться купить еще раз. Средства за предыдущую покупку должны вернуться автоматически

• не выставить время большое время удержания цены – перепрошить ТА на актуальную версию прошивки
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.2':
        bot.send_message(callback.message.chat.id, '''
См. инструкцию «Действия при замене или установке банковского терминала»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.3':
        bot.send_message(callback.message.chat.id, '''
Vendotek VL отличается от Vendotek V3/VN в следующем:

• он может работать только в паре с внутренним модулем MatiPay. Использует его как модем для получения/передачи информации

• показывает QR-код электронного чека после совершения покупки. Если он установлен в ТА, то пропадает необходимость в использовании отдельного дисплея для его отображения

• значительно дешевле Vendotek V3/VN

• не может использоваться в ТА одновременно с App, так как используют один и тот же разъем

• могут работать с монетоприемниками NRI и MEI (Vendotek V3 только с MEI)

• уровень сотового сигнала можно проверить только в личном кабинете на сайте MatiPay

• Vendotek VL – 2G, Vendotek V3 – 3G

Vendotek V3 и Vendotek VN функционально для нас ничем не отличаются между собой.
На текущий момент Vendotek VL больше не закупаем. Приоритет отдан Vendotek V3/VN как компромиссное решение между Vendotek Lite и Vendotek V3 как по стоимости, так и функциональности
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.4':
        bot.send_message(callback.message.chat.id, '''
Нажать и удерживать на экране два пальца >11 сек и набрать пин-код 739.

• Terminal Info – информация о терминале/версия прошивки

• Log-TMS – проверка соединения с сервером «Терминальных Технологий»

• Update TMS config – обновление конфигурации с сервера «Терминальных технологий»

• Update BANK config – обновление конфигурации от банка
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.5':
        bot.send_message(callback.message.chat.id, '''
• нажатие кнопки программирование на обратной стороне терминала

• набрать пин-код 351 путем касания экрана одним пальцем посередине в нижней части экрана терминала:

один, два, три — пауза — один, два, три, четыре, пять — пауза — один

• нажать и удерживать на экране два пальца >11 сек и набрать пин-код 351
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.6':
        bot.send_message(callback.message.chat.id, '''
Обновить терминал можно через сервисное меню по WiFi

1. при включении терминала (когда показывается версия прошивки) три раза «тапнуть» по экрану для попадания в сервисное меню

2. «FW update»  «Список устройств»

3. в «Mode» выбрать «WiFi»

4. заполнить данные «SSID» и «Password» (берем из телефона при создании точки доступа в нем)

5. вкл точку доступа на телефоне

6. подключить по WiFi банковский терминал к точке доступа телефона

7. нажать «Update»

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.7':
        bot.send_message(callback.message.chat.id, '''
Сбросить к заводским настройкам

1. при включении терминала (когда показывается версия прошивки) три раза «тапнуть» по экрану для попадания в сервисное меню

2. Settings

3. вводим пароль 9644278

4. Factory reset

5. после этого терминал должен быстро запускаться

6. далее прошиваем на последнюю прошивку
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.8':
        bot.send_message(callback.message.chat.id, '''
Vendotek Lite

• нет связи с банком. Попробовать обновить конфигурацию TMS и конфигурацию банка через меню терминала

• сим-карта может быть заблокирована

• сим-карта может быть неисправна

• глюк ПО. Помогает Factory reset

Vendotek V3

• сим-карта может быть заблокирована

• сим-карта может быть неисправна

• плохой уровень сигнала — внешнюю антенну поставить
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.9':
        bot.send_message(callback.message.chat.id, '''
Vendotek VL/VN/V3 может работать с монетоприемниками NRI и MEI
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.10':
        bot.send_message(callback.message.chat.id, '''
Поддерживается только монетоприменикм MEI, КМ KREA/KALEO. В настройках необходимо выставить следующий параметр:
Always idle - cashless 1
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.11':
        bot.send_message(callback.message.chat.id, '''
Выставить в настройках банковского терминала MDB Level – 2 (по умолчанию стоит AUTO):

• Vendotek V3 - зайти в меню программирования - Конфиг. VMC - Уровень (MDB) — 2

• Vendotek VN -  зайти в меню программирования - Система - Настройки автомата - MDB Feature level – 2

Можно выставить удаленно через ЛК ТТ следующие профили:

• для NRI + VN -  (parent)/mdb.cashless1/dc0/500/L1

• для NRI + V3 - (parent)/mdb.cashless1.dc0.lvl1.tcn
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.12':
        bot.send_message(callback.message.chat.id, '''
Включить следующую настройку в монетприемнике MEI:

• Безналичные системы - основное меню - pre-selection - da(вкл)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.13':
        bot.send_document(callback.message.chat.id, open(r"./Руководство по эксплуатации Vendotek V3.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.14':
        bot.send_document(callback.message.chat.id, open(r"./Руководство по эксплуатации Vendotek VN.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '5.15':
        bot.send_document(callback.message.chat.id, open(r"./Руководство по эксплуатации Vendotek VL.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 3.3.2 Безналичные системы - Банковский терминал - Ошибки_ЛК_ТТ - кнопки ответа
    elif callback.data == 'errorLK1':
        bot.send_document(callback.message.chat.id, open(r"./Ошибки_ЛК_ТТ/Tamper.jpg", 'rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
Терминалу не нравится батарейка (села), в ЛК отображается ошибка «Tamper (TPR)»,
но терминал продолжает работать до тех пор, пока не словит глюк и тогда начинает перезагружаться про кругу.
Снять для ремонта в офисе*

*раньше при TPR надо было сдавать в ТТ на замену батареи и переинициализации,
сейчас можем менять сами, терминал не падает в защиту
''', protect_content=True, reply_markup=Delete2)





# 3.3.3 Безналичные системы - АПП - кнопки вопроса
    elif callback.data == '6.1':
        bot.send_message(callback.message.chat.id, '''
• отсутствует соединение с интернетом

• в случае ошибки «проверить время» — необходимо в настройках смартфона проверить параметр «Использовать время сети» и «Использовать часовой пояс сети», они должны быть активными

• смартфон подключается, но не дает сделать покупку (что-то пошло не так) — необходимо в настройках смартфона проверить параметр «Использовать время сети» и «Использовать часовой пояс сети», они должны быть активными
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '6.2':
        bot.send_message(callback.message.chat.id, '''
• зеленый диод - в рабочем состоянии

• оранжевый диод - в режиме подключения к смартфону

• красный диод - в нерабочем состоянии
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '6.3':
        bot.send_message(callback.message.chat.id, '''
• о bluetooth

• по NFC
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '6.4':
        bot.send_message(callback.message.chat.id, '''
Нет, так как они подключаются к одному и тому же разъему на внешнем модуле Matipay
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '6.5':
        bot.send_message(callback.message.chat.id, '''
• App работает с NRI только на первом кэшлесс (NRI+MSK)

• App работает с MEI на втором кэшлесс
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '6.6':
        bot.send_message(callback.message.chat.id, '''
При прикладывании брелока к внешнему модулю считывателя NFC (App+NFC) Matipay по каналу GPRS связывается с сервером и передает ему информацию о брелоке (идентификационный номер).
После получения ответа от сервера становится возможным использовать брелок — пополнять его, покупать с него.
Если в момент прикладывания интернет отсутствует, то брелок использовать не получится, он не будет работать,
так как без ответа с сервера, Matipay не сможет его идентифицировать.
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '6.7':
        bot.send_message(callback.message.chat.id, '''
Плохая связь/отсутствие интернета в момент попытки использовать NFC-брелок

Как увидеть:
Через ЛК Matipay в устройстве во вкладке  «Alarms/Events» смотрим «GPRS network status».
Он должен быть равен всегда «1». Это говорит о том, что интернет есть.
Если периодически проскакивает «0» (то есть периодически отсутствует интернет), то необходимо поменять оператора связи и дополнительно установить антенну
''', protect_content=True, reply_markup=Exitt)





# 3.4 MDB - кнопки ответа
    elif callback.data == 'mdb.1':
        bot.send_message(callback.message.chat.id, '''
1. переключить на плате CPU дип-переключатели (1,2,3 и 4) в положение «On» для включения шины MDB

2. подключить параллельно платежную систему, включая Matipay, по проводу MDB (питание приходит по этому же проводу) в разъем MDB на плате CPU

3. подключить к ТА в разъем RS-232 провод от Matipay для передачи информации об ошибках ТА

4. выставить в настройках платежной системы ТА:

• ПС — MDB

• Immidiate change – off

• Позиция пункта - 0

• Multivend – on

• Cashless 2 Enable  - on (если на аппарате будет вторая безналичная система (приложение, к примеру))

Цены устанавливаются в ТА в  меню 2.1:

• стандарт - отображение стоимости на табло ТА

• ключ 1 - цена по банковскому терминалу

• key 1 - цена по приложению (данные строчки появятся только после включения Cashless 2 Enable)

5. настроить телеметрию:

Техн. 6.2.Х:

• communicat. protocol DDCMP ENHANCED

• передача данных TELEMETRY

• EVADTS TYPE ENHANCED

• serial baudrate 2400''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./MDB/Canto_maestro_MDB.mp4','rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == 'mdb.2':
        bot.send_message(callback.message.chat.id, '''
Полностью отключить питание сети:

• обесточить плату

• выключить ТА из розетки

• вытащить сервисный ключ из выключателя питания за лотком выдачи продуктов
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mdb.3':
                bot.send_message(callback.message.chat.id, '''

1. переключить на плате CPU дип-переключатели (1,2,3 и 4) в положение «On» для включения шины MDB

2. подключить параллельно платежную систему, включая Matipay, по проводу MDB (питание приходит по этому же проводу) в разъем MDB на плате CPU

3. подключить к ТА в разъем RS-232 провод от Matipay для передачи информации об ошибках ТА

4. выставить в настройках платежной системы ТА:

• тип монетника — mdb

• немедлен сдача — off

• позиция пункта — 0

• резервейш тайм — 35

• макс кредит ключа 500

Цены устанавливаются в ТА в соответствующем меню

5. настроить телеметрию:

Техн. 6.2.Х:

• communicat. protocol DDCMP ENHANCED

• передача данных TELEMETRY

• EVADTS TYPE ENHANCED

• serial baudrate 2400

''', protect_content=True)
                bot.send_video(callback.message.chat.id,open('./MDB/Настройки MDB для Concerto.mp4','rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == 'mdb.4':
        bot.send_message(callback.message.chat.id, '''
1. переключить на плате CPU дип-переключатели (1,2,3 и 4) в положение «On» для включения шины MDB

2. подключить параллельно платежную систему, включая Matipay, по проводу MDB (питание приходит по этому же проводу) в разъем MDB на плате CPU

3. подключить к ТА в разъем RS-232 провод от Matipay для передачи информации об ошибках ТА

4. выставить в настройках платежной системы ТА:

• тип монетника - mdb

• изменить немедленно - off

• десятичная точка — 0

• максимум кредита - 300

Цены устанавливаются в ТА в соответствующем меню

5. настроить телеметрию:

Техн. 6.2.Х:

• communicat. protocol DDCMP ENHANCED

• передача данных TELEMETRY

• EVADTS TYPE ENHANCED

• serial baudrate 2400

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == 'mdb.5':
        bot.send_message(callback.message.chat.id, '''
1. переключить на плате CPU дип-переключатели (1,2,3 и 4) в положение «On» для включения шины MDB

2. подключить параллельно платежную систему, включая Matipay, по проводу MDB (питание приходит по этому же проводу) в разъем MDB на плате CPU

3. подключить к ТА в разъем RS-232 провод от Matipay для передачи информации об ошибках ТА

4. выставить в настройках платежной системы ТА:

• ПС — MDB

• Immidiate change – off

• Позиция пункта - 0

• Reservetion T. - 35 (выставлять индивидуально после тестов оплаты по банковской карте)

• Торговый тип - Multivend

• Максимальный кредит - 300

• Cash sale - 00

• Cashless always IDLE - on

Цены устанавливаются в ТА в  меню 2.1:

• стандарт - отображение стоимости на табло ТА

5. настроить телеметрию:

Техн. 6.2.Х:

• communicat. protocol DDCMP ENHANCED

• передача данных TELEMETRY

• EVADTS TYPE ENHANCED

• serial baudrate 2400

6. В конфигурации Matipay установить Cashless - 1. Перезагрузить Matipay

''', protect_content=True)
        bot.send_video(callback.message.chat.id,open('./MDB/MDB Maestro+Vendotek_Lite.mp4','rb'), protect_content=True, reply_markup=Delete2)





# 4. Гидросистема - кнопки вопроса
    elif callback.data == '7.1':
        bot.send_message(callback.message.chat.id, '''
Недолив напитка (особенно с утра после большого простоя) происходит из-за байпаса 12-14 бар,
который на верхней помпе. он пропускает воду из бойлера, и она уходит через байпас на счетчик воды и в эйр брейк.
В бойлере образуется воздушная пробка, которая при приготовлении сначала выдавливается в стакан (воздух идет) и только потом вода
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.2':
        bot.send_message(callback.message.chat.id, '''
Неисправен:

• счетчик воды

• микровыключатель Айрбрейка
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.3':
        bot.send_message(callback.message.chat.id, '''
Помпа рассчитана на рабочее напряжение 24В
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.4':
        bot.send_message(callback.message.chat.id, '''
Снять трубку со входа счетчика воды и посмотреть, как льется вода самотеком из эйр-брейка
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.5':
        bot.send_message(callback.message.chat.id, '''
Пошевелить катушку клапана. Если не шевелится, значит ее расперло или от влаги с треснутого корпуса клапана, или от того, что сама по себе развалилась
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.6':
        bot.send_message(callback.message.chat.id, '''
Визуально осмотреть гидросистему и убедиться, что:

• шланги в канистрах не короткие и имеют вырез на концах, чтобы не прилипать к стенкам канистры при закачке воды

• при наличии 2х и более канистр шланги плотно сидят на тройниках и затянуты стяжками

• шланг на нижней помпе закреплен стяжкой

• айрбрейк чистый, без трещин и подтеков. Поплавок свободно ходит, микровыключатель айрбрейка надежно закреплен

• фильтр воды чистый, подходящие шланги надежно закреплены

• бойлер без подтеков

• счетчик воды внутри чистый, снаружи подходящие шланги надежно закреплены

• резьбовые соединения на внутренней помпе не подтекают

• клапан лавацца (при его наличии) не подтекает, все соединения с пластиковыми трубками сухие

• кофейный пресс при приготовлении кофе не протекает в местах соединения с шлангами
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.7':
        bot.send_message(callback.message.chat.id, '''
Сделать 3 раза промывку и замерить количество выдаваемой воды
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.8':
        bot.send_message(callback.message.chat.id, '''
• сделать промывку и убедиться в работе всех клапанов

• сделать зерновой/капсульный кофе, убедиться в работе клапана эспрессо

• визуально осмотреть бойлер на наличие протечек

• проверить ТЭН бойлера на «пробой» с помощью мультиметра - если исправен, то покажет 38-42 Ома, если неисправен, то зашкалит в килоомы

• проверить, что сопротивление термодатчика меняется при изменении температуры воды в бойлере

• проверить скорость нагрева бойлера
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.9':
        bot.send_message(callback.message.chat.id, '''
• помпа EP8

• погружной насос Bianchi

В общем случае нужна высокопроизводительная помпа, чтобы эйр-брейк успевал наполняться водой из канистры, и ТА не уходил в ошибку «Нет воды»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.10':
        bot.send_message(callback.message.chat.id, '''
Ограничивает давление:

• 12 бар на помпе, которая идет к бойлеру

• 2 бара - на помпе, которая качает воду из канистры

(используется в том числе для того, чтобы при пережатии шланга подачи воды от насоса к эйр-брейку, он не слетел с насоса и не было утечки воды. Вода будет качаться по кругу через bypass)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.11':
        bot.send_message(callback.message.chat.id, '''
Сброс давления, чтобы при раскрытии пресса не разлетался жмых
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.12':
        bot.send_message(callback.message.chat.id, '''
В Concerto LB дополнительно присутствует:

• клапан LB

• второй фильтр воды после счетчика воды перед бойлером эспрессо

• два бойлера – бойлер эспрессо и бойлер растворимых напитков

• два счетчика воды

• две верхних помпы
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.13':
        bot.send_message(callback.message.chat.id, '''
• на зерновом с помощью подстроечного резистора на задней плате

• на капсульном регулируется в соответствующем меню программирования ТА
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '7.14':
        bot.send_message(callback.message.chat.id, '''
EP8 - слабое давление, но большой обьем воды прокачивает. Только на подкачку воды (особенно KREA)

EX5 - большое давление (12-14бар), малый обьем воды. Может использоваться как на полке бойлера, так и на подкачке любого аппарата (ТА), КРОМЕ КМ KREA!!!

EP5 - большое давление (12-14бар), малый обьем воды. Отличается от EX5 только тем, что имеет пластиковый корпус. Может использоваться как на полке бойлера, так и на подкачке любого аппарата (ТА), КРОМЕ КМ KREA!!!

EX5 и EP5 НОВЫЕ СТАВИМ ТОЛЬКО НА ПОЛКУ БОЙЛЕРА. БУ вниз на подкачку. Потому что бу это бу, а на подкачке много давления не надо, в отличие от полки бойлера, где помпа должна продавить таблетку спрессованного кофе в прессе, нагрузка больше в разы.
''', protect_content=True, reply_markup=Exitt)





# 5. Кофемолка - кнопки вопроса
    elif callback.data == '8.1':
        bot.send_message(callback.message.chat.id, '''
• не подключен датчик холла на кофемолке

• неисправен датчик холла на кофемолке

• не правильно подключен разъем микровыключателя наличия пресса (их там два)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '8.2':
        bot.send_message(callback.message.chat.id, '''
• сделать несколько тестов выдачи кофе

• убедиться в отсутствии посторонних звуков при работе кофемолки
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '8.3':
        bot.send_message(callback.message.chat.id, '''
• первая доза выдается по сигналу микровыключателя

• вторая доза по количеству оборотов кофемолки
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '8.4':
        bot.send_message(callback.message.chat.id, '''
• проверить помол (слишком мелкий)

• проверить температуру (слишком высокая)

• проверить/заменить кофемолку (затупливаются ножи, кофе не молится, а перетирается в итоге)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '8.5':
        bot.send_message(callback.message.chat.id, '''
1. Проверить температуру воды на выходе из носика (xем больше робусты в составе, тем меньше температура.
И чем больше арабики, тем больше температура. К примеру: 82 — 83 Granbar; 83 — 85 Crema Ricco; 84 – 87 Aroma top)

2. Помол настраивается на СВЕЖЕМ кофе!

3. Дозатор и камера пресса должны быть выставлены соответственно типу ТА

4. Вращением ручки – регулятора степени помола  (по часовой – мельче помол, против часовой - грубее)
необходимо добиться выполнения следующих условий (вращать ручку регулятора можно ТОЛЬКО ПРИ РАБОТАЮЩЕЙ КОФЕМОЛКЕ!
После каждой подстройки результат виден только на 3-ем тестовом напитке):

• струя должна быть коническая, коричневатая

• время эспрессо пролива 10-12 сек

• на готовом кофе образуется плотная коричневая пенка

• таблетка после выброса из пресса чуть влажная, крепкая

• отсутствует запах и привкус жженой резины
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '8.6':
        bot.send_message(callback.message.chat.id, '''
Перетянут помол. Так как камера большого диаметра (43 или 46 мм) (в отличие от прессов с маленьким объемом камеры, диаметр 38 мм),
то таблетка получается тонкая и давления помпы хватит при любом помоле, чтобы прогнать через нее воду (на камере 38 мм ТА уйдет в ошибку «счетчик воды»).
Единственным показателем того, что помол перетянут будет как раз жидкая таблетка
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '8.7':
        bot.send_message(callback.message.chat.id, '''
• поставить кофемолку от Оперы, при этом придется снять обе родных кофемолки Калео

• в случае, если у клиента используется только один бункер кофе/кофемолка, переключить контакты на вторую неиспользуемую кофемолку и засыпать кофе в соответствующий бункер
''', protect_content=True)
        bot.send_photo(callback.message.chat.id, open('./Кофемолка от оперы на калео_1.jpg','rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open('./Кофемолка от оперы на калео_2.jpg','rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open('./Кофемолка от оперы на калео_3.jpg','rb'), protect_content=True, reply_markup=Delete4)





# 6. Кофе - кнопки вопроса
    elif callback.data == '9.1':
        bot.send_message(callback.message.chat.id, '''
• проверить помол (слишком мелкий)

• проверить температуру (слишком высокая)

• проверить/заменить кофемолку (затупливаются ножи, кофе не молится, а перетирается в итоге)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '9.2':
        bot.send_message(callback.message.chat.id, '''
Чем больше робусты в составе, тем меньше температура. И чем больше арабики, тем больше температура. К примеру:

• 82 — 83 Granbar

• 83 — 85 Crema Ricco

• 84 – 87 Aroma top
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '9.3':
        bot.send_message(callback.message.chat.id, '''
1. Проверить температуру воды на выходе из носика (xем больше робусты в составе, тем меньше температура. Чем больше арабики, тем больше температура

2. Помол настраивается на СВЕЖЕМ кофе!

3. Дозатор и камера пресса должны быть выставлены соответственно типу ТА и объему напитка

4. Вращением ручки – регулятора степени помола (по часовой – мельче помол, против часовой - грубее) необходимо добиться выполнения следующих условий (вращать ручку регулятора можно ТОЛЬКО ПРИ РАБОТАЮЩЕЙ КОФЕМОЛКЕ! После каждой подстройки результат виден только на 3-ем тестовом напитке):

• струя должна быть коническая, коричневатая

• время эспрессо пролива 10-12 сек (на 50мл)

• на готовом кофе образуется плотная коричневая пенка

• таблетка после выброса из пресса чуть влажная, крепкая

• отсутствует запах и привкус жженой резины
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '9.4':
        bot.send_message(callback.message.chat.id, '''
Перетянут помол.
Так как камера большого диаметра (43 или 46 мм) (в отличие от прессов с маленьким объемом камеры, диаметр 38 мм),
то таблетка получается тонкая и давления помпы хватит при любом помоле, чтобы прогнать через нее воду (на камере 38 мм ТА уйдет в ошибку «счетчик воды»).
Единственным показателем того, что помол перетянут будет как раз жидкая таблетка.
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '9.5':
        bot.send_message(callback.message.chat.id, '''
1. температура

2. помол

3. сточенные ножи кофемолки

4. доза кофе

5. дозатор, его заклинивание

6. дозировка воды

7. клапан эспрессо не держит

8. не достаточное давление воды

9. прокладки пресса не держат

10. засорилась сетка пресса

11. некачественный кофе

12. некачественная вода
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '9.6':
        bot.send_document(callback.message.chat.id, open(r"./Обзор блендов кофе Lavazza.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '9.7':
        bot.send_document(callback.message.chat.id, open(r"./Теоретический курс кофе.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 7. Кофе-группа - кнопки вопроса
    elif callback.data == '10.1':
        bot.send_message(callback.message.chat.id, '''
1. капсула из диспенсера капсул падает в пресс

2. пресс делает оборот до закрытия камеры с капсулой

3. включается верхняя помпа

4. открывается клапан Lavazza

5. под давлением воды, поступающей с клапана Lavazza, капсула кофе начинает прокалываться верхним поршнем

6. через определенное время после прокалывания капсулы открывается клапан эспрессо на бойлере

7. начинается процесс заварки кофе

8. после пролива необходимого количества кофе помпа выключается

9. закрывается клапан эспрессо на бойлере

10. сбрасывается давление на клапане Lavazza

11. верхний поршень пресса возвращается в исходное положение

12. пресс делает оборот до полного открытия камеры одновременно выбрасывая капсулу нижним штоком и выталкивателями капсул
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.2':
        bot.send_message(callback.message.chat.id, '''
Объемом заварочной камеры:

• ToGo 200мл 38мм (поршень в нижнем положении)

• ToGo 200мл 38мм (поршень в верхнем положении)

• ToGo 250мл 46мм (поршень в нижнем положении)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.3':
        bot.send_message(callback.message.chat.id, '''
   Сделать тест зернового/капсульного кофе

В зерновом прессе:

• проверить ход штока – должен ходить плавно без заеданий

• проверить сеточку в камере пресса на чистоту

• визуально осмотреть на наличие утечки кофе

• если молотый кофе из дозатора сыпется мимо камеры пресса, то его необходимо заменить

В капсульном прессе проверить:

• ход штока – должен ходить плавно без заеданий

• прокалыватели на целостность

• после теста убедиться в том, что верхний прокалыватель возвращается на свое место

• утечки при приготовлении кофе
    ''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.4':
        bot.send_message(callback.message.chat.id, '''
Перетянут помол. Так как камера большого диаметра (43 или 46 мм) (в отличие от прессов с маленьким объемом камеры, диаметр 38 мм),
то таблетка получается тонкая и давления помпы хватит при любом помоле, чтобы прогнать через нее воду (на камере 38 мм ТА уйдет в ошибку «счетчик воды»).
Единственным показателем того, что помол перетянут будет как раз жидкая таблетка
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.5':
        bot.send_message(callback.message.chat.id, '''
46 диаметр, поршень в нижнем положении
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.6':
        bot.send_message(callback.message.chat.id, '''
• заменить кофемолку

• заменить дозатор кофе

• заменить вентилятор (ТО вент группы провести)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.7':
        bot.send_message(callback.message.chat.id, '''
• проверить работу зернового пресса, возможно закис шток

• проверить моторедуктор пресса

• проверить крепление моторедуктора пресса к полке миксеров

• крупный помол, не дающий камере пресса полностью закрыться

• неисправен микровыключатель положения пресса

• отсутствует опорная втулка на винте крепления пресса к ТА, из-за чего он не ровно встает и верхний шток не попадает в камеру пресса

• большая доза выброса кофе из дозатора кофе
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.8':
        bot.send_message(callback.message.chat.id, '''
Механическая блокировка модуля.
Если, по какой-либо причине, двигатель не завершает вращение в определенное время, направление вращения изменяется на противоположное;
если эта попытка не приводит к успеху, выбор кофе-продуктов блокируется, в системе регистрируется сбой «Capsule block»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '10.9':
        bot.send_message(callback.message.chat.id, '''
• не уходит на место верхний прокалыватель

• плохое состояние прокалывателей

• отсутствие выталкивателей капсул на прессе

• закисший верхний шток

• закисший нижний шток

• бракованные капсулы

• неисправен дозатор капсул

• ТА не выставлен по уровню
''', protect_content=True, reply_markup=Exitt)





# 8. Ошибки ТА - кнопки вопроса
    elif callback.data == '11.1':
        bot.send_message(callback.message.chat.id, '''
• в истории ошибок в меню ТА

• на сайте Matipay в разделе Alarms/Events
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.2':
        bot.send_message(callback.message.chat.id, '''
Симптомы неисправности самого счетчика воды:

• постоянно льющаяся вода (неисправен датчик Холла, отсутствует контакт на разъеме счетчика воды (провод отвалился или закис) или неправильно подключен разъем счетчика воды)

• перелив напитков (датчик Холла исправен, но вращению крыльчатки, для корректного отсчёта импульсов, что-то мешает - частицы осадка из расширительного бачка или износ вершины иглы, на которой вращается крыльчатка)

Причины, по которым может возникать неисправность «Счётчик воды» при исправном счётчике сводятся к одному -вода не проходит через счётчик,
либо за определённое время не проходит определённый объём воды. То есть, нет движения воды через счетчик воды - нет отсчёта импульсов счётчиком, отсюда и ошибка.


Примеры:

• не открывшийся клапан эспрессо/растворимых при приготовлении напитка

• верхняя помпа не качает воду при приготовлении напитка

• износ перепускного клапана на тройнике By pass 12 bar

• сгоревшая катушка электромагнитного клапана эспрессо/растворимых

• слишком мелкий помол кофе, не дающий воде «пройти» через таблетку в прессе

• забитая сеточка камеры зернового пресса

В случае с КМ Калео:

• воздушная пробка,

• зарос накипью фитинг на входе в бойлер

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.3':
        bot.send_message(callback.message.chat.id, '''
ТА не успел нагреть воду в бойлере до значения, выставленного в настройках за 10 минут с момента включения ТА
или с момента последнего приготовления напитка. Причины:

• низкое напряжение сети (д.б. 230-240В)

• термопредохранитель сработал

• плата управления бойлером неисправна

• неисправен тэн

• температурный датчик неисправен

• низкая температура в помещении
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.4':
        bot.send_message(callback.message.chat.id, '''
• утечка воды из эйр-брейка в момент простоя ТА

• если после 7 приготовлений микровыключатель Айр-брейка не просигнализирует о том, что кончилась вода в нем (инфа от производителя)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.5':
        bot.send_message(callback.message.chat.id, '''
Проверить работу датчиков наличия стаканов, почистить, отрегулировать
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.6':
        bot.send_message(callback.message.chat.id, '''
• проверить работу зернового пресса, возможно закис шток

• проверить моторедуктор пресса

• проверить крепление моторедуктора пресса к полке миксеров

• крупный помол, не дающий камере пресса полностью закрыться

• неисправен микровыключатель положения пресса

• отсутствует опорная втулка на винте крепления пресса к ТА, из-за чего он не ровно встает и верхний шток не попадает в камеру пресса

• большая доза выброса кофе из дозатора кофе
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.7':
        bot.send_message(callback.message.chat.id, '''
Если величина входящего тока дозатора выходит за пределы величин, установленных по умолчанию, все опции выбора,
в приготовлении которых принимает участие этот дозатор, будут отключены.

К примеру, оператор при обслуживании ТА забыл опустить в бункере носик молока
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.8':
        bot.send_message(callback.message.chat.id, '''
Механическая блокировка модуля.

Если, по какой-либо причине, двигатель не завершает вращение в определенное время, направление вращения изменяется на противоположное;
если эта попытка не приводит к успеху, выбор кофе-продуктов блокируется, в системе регистрируется сбой «Capsule block»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.9':
        bot.send_message(callback.message.chat.id, '''
Утечка воды:

• в бойлере

• в By pass

• в треснувшем шланге от Bypass к бойлеру

• протекающий клапан эспрессо/растворимых

Движение воды (утечка) во время самодиагностики ТА на момент утечки.

Вкл насос, если вода не проходит через счетчик воды, то давление в бойлере есть и все нормально (в противном случае выдается ошибка инсталляция).

Дальше открывает клапан на полсекунды и видит, что счетчик воды работает – таким образом отсекается вариант поломки счетчика воды
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.10':
        bot.send_message(callback.message.chat.id, '''
Суппорт с носиками напитков не отработал полный цикл движения. Чаще всего застрявший стакан является причиной того, что носики не встали в положение для налива напитка.

Особенность этой ошибки в Concerto.
Симптомы - перезагрузка во время приготовления напитка. Проявляется только, когда ТА подключен к водопроводу.

Решение — подключить на канистру
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.11':
        bot.send_message(callback.message.chat.id, '''
• села батарейка энергозависимой памяти, в которой хранятся настройки на плате CPU

• снят джампер на плате CPU, рядом с батарейкой (вкл питание энергозависимой  памяти от батарейки)

• плата CPU неисправна
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.12':
        bot.send_message(callback.message.chat.id, '''
Появляется на Snakky Max Food - разомкнут микровыключатель открытия двери
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '11.13':
        bot.send_message(callback.message.chat.id, '''
• не отрегулирован/не работает датчик выдачи стакана, или неправильно отключен программно

• закрытая дверь ТА зажала окно выдачи стаканов из-за чего стало невозможным движение носиков
''', protect_content=True, reply_markup=Exitt)





# 9.1 Koro Prime - кнопки ответа
    elif callback.data == '12.1':
        bot.send_message(callback.message.chat.id, '''
В техническом меню зайти в пункт "Неисправности" – "Сброс ошибок"
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.2':
        bot.send_message(callback.message.chat.id, '''
1. От парового бойлера идет пар через клапан вверх капучинатора

2. Через ручной регулируемый клапан подается воздух

3. Одновременно подается молоко

4. Все это смешивается в капучинаторе и подается в стакан

Путем регулировки ручного клапана можно регулировать объём и плотность пены
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.3':
        bot.send_message(callback.message.chat.id, '''
Убедиться, что

• на конце шланга есть металлический дозатор (который опускается в емкость с молоком)

• в правильности установки емкости молока

• молочные трубки не перегибаются

• молочные трубки и капучинатор чистые

• регулятор подачи пены не закрыт полностью

• молочные трубки правильно подсоединены (согласно схеме на обратной стороне двери аппарата)

• молоко ультрапастеризованное и нужной жирности (2.5% - 4.5%)

• молочный насос исправен
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.4':
        bot.send_message(callback.message.chat.id, '''
как в ТА Necta Opera/Canto/Concerto
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.5':
        bot.send_message(callback.message.chat.id, '''
• контейнер отходов переполнен

  Его нужно очищать только при включенном аппарате и закрытой дверце

• быстро вытащили-вставили контейнер отходов, счетчик отходов не успел сброситься
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.6':
        bot.send_message(callback.message.chat.id, '''
нажать любую кнопку
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.7':
        bot.send_message(callback.message.chat.id, '''
• прошивка с usb-накопителя КМ

• копирование настроек с Google-диска («Документы выездных техников» - [ЗЕРНОВЫЕ КОФЕ-МАШИНКИ] - [ЗЕРНОВЫЕ КОФЕ-МАШИНКИ_КЛИЕНТЫ] - KORA PRIME FM) на usb-накопитель

• копирование настроек с usb-накопителя на КМ

• калибровка шнеков

• регулировка доз кофе/растворимых

• общая настройка КМ

Если при попытке прошиться с USB-флешки КМ перезагружается, то необходимо поменять USB-флешку.
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.8':
        bot.send_message(callback.message.chat.id, '''
Если в настройках напитков стоит доза кофе больше или равная 10 грамма, то машинка считает её как две дозы
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.9':
        bot.send_message(callback.message.chat.id, '''
Слить настройки с КМ и скопировать на гугл-диск в соответствующую папку

«Документы выездных техников» - [ЗЕРНОВЫЕ КОФЕ-МАШИНКИ] - [ЗЕРНОВЫЕ КОФЕ-МАШИНКИ_КЛИЕНТЫ] - KORA PRIME FM

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.10':
        bot.send_message(callback.message.chat.id, '''
Перетянут помол
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.11':
        bot.send_message(callback.message.chat.id, '''
46 диаметр, маленький объем камеры - верхний поршень должен быть опущен
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.12':
        bot.send_message(callback.message.chat.id, '''
Нет, ограничение по времени (около 50 сек)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.13':
        bot.send_message(callback.message.chat.id, '''
Поставить обратный клапан от аквариума
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.14':
        bot.send_message(callback.message.chat.id, '''
1.Включение

  В настройках КМ в пункте меню «Equipped cabinet» - «OFF»

2.Регулировка количества отходов

  В контейнер максимум помещается 25 таблеток. При необходимости изменить количество можно в «Параметры ТА» - «Макс кол-во отходов»

2.Отключение

  Только для КМ , стоящих на кофе-поинте или имеющих отверстие под сброс отходов в ведро под столом.

  В настройках КМ в пункте меню «Equipped cabinet» - «ON»

Неправильно выставленный параметр будет приводить к тому, что в КМ постоянно будет забиваться пресс отходами, а сообщение о переполненном контейнере не высвечивается

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.15':
        bot.send_message(callback.message.chat.id, '''
Диодный мост неисправен на плате управления (задняя плата), заменить плату в сборе
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.16':
        bot.send_message(callback.message.chat.id, '''
В КМ два кэшлесса.

• Cashless 1 - используется

• Cashless 2 - не испол, так как не попадает в статистику

На КМ может работать одновременно только одно устройство безналичной оплаты

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.17':
        bot.send_message(callback.message.chat.id, '''
На всех КМ вне зависимости от типа водоснабжения установить

• «Канистра» - «Установка тумбы»

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.18':
        bot.send_message(callback.message.chat.id, '''
• проверить и заменить при необходимости паровой бойлер

• заменить клапан пара

• проверить настройки скорости подачи  молока. Чем выше значение, тем медленнее льет

• проверить не забито ли верхнее отверстие подачи пара в капучинатор

''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.19':
        bot.send_message(callback.message.chat.id, '''
В настройках платежной системы «Reservetion time» должен быть >2 секунд
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.20':
        bot.send_message(callback.message.chat.id, '''
Отключены пункты операторского меню в настройках КМ
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.21':
        bot.send_message(callback.message.chat.id, '''
Кнопкой американо (вторая кнопка) набрать 6 нулей (000000)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.22':
        bot.send_document(callback.message.chat.id, open(r"./Настройка Kora Prime для HoReCa.pdf", 'rb'), protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Универсальная прош_настр KORA fm0.2 HoReCa.rar", 'rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == '12.23':
        bot.send_document(callback.message.chat.id, open(r"./Универсальная прош_настр KORA fm0.3 Vending.rar", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.24':
        bot.send_document(callback.message.chat.id, open(r"./Пользовательская инструкция по эксплуатации Kora Prime Fresh Milk.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.25':
        bot.send_document(callback.message.chat.id, open(r"./Инструкция по эксплуатации Kora Prime Fresh Milk.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '12.26':
        bot.send_message(callback.message.chat.id, '''
Для того, чтобы молоко не зависало в бункере, на зубчатое колесо необходимо прикрепить стяжки.
Пример №1''',protect_content=True)
        bot.send_video(callback.message.chat.id,open('./Kora_стяжки/Кора_стяжки_видео.mp4','rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''Пример №2''')
        bot.send_photo(callback.message.chat.id, open(r"./Kora_стяжки/Кора_стяжки1.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Kora_стяжки/Кора_стяжки2.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Kora_стяжки/Кора_стяжки3.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Kora_стяжки/Кора_стяжки4.jpg", 'rb'), protect_content=True, reply_markup=Delete7)
    elif callback.data == '12.27':
        bot.send_message(callback.message.chat.id, '''
Установлены заводские крепления пресса и моторедуктора''',protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Kora_press/koro_press1.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Kora_press/koro_press2.jpg", 'rb'), protect_content=True)
        bot.send_message(callback.message.chat.id, '''
Необходимо сделать следующее:
• переделать на месте - из пресса вытащить штырь, на моторедуктор пресса установить кривошип арт. 098763

• поставить переделанные пресс без штыря и моторедуктор (к примеру, от кикко Es6/LB/Max)''',protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Kora_press/koro_press3.jpg", 'rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open(r"./Kora_press/koro_press4.jpg", 'rb'), protect_content=True, reply_markup=Delete6)





# 9.2 Kaleo - кнопки вопроса
    elif callback.data == '13.1':
        bot.send_message(callback.message.chat.id, '''
• магнит отвалился

• контейнер не вставлен

• разъем на герконе
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.2':
        bot.send_message(callback.message.chat.id, '''
• давление парового бойлера изменить

• скорость подачи молока
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.3':
        bot.send_message(callback.message.chat.id, '''
• заменить кофемолку

• заменить дозатор кофе

• заменить вентилятор (ТО вент группы провести)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.4':
        bot.send_message(callback.message.chat.id, '''
Зарос накипью фитинг на входе в бойлер эспрессо
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.5':
        bot.send_message(callback.message.chat.id, '''
Установить обычный счетчик объема воды Некта.
    Важно!
На КМ, подключенной к водопроводу, данный счетчик не сможет работать, так как соединения не выдержат давления воды.
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.6':
        bot.send_message(callback.message.chat.id, '''
В КМ два кэшлесса. Использоваться могут оба
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.7':
        bot.send_message(callback.message.chat.id, '''
Неисправен датчик давления. Закоротить его
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.8':
        bot.send_message(callback.message.chat.id, '''
Включена функция «Активация продаж за наличные» ( Меню 6.1.4>6.1.4.3).
При активной функции каждый раз, когда покупатель  пробует купить напиток (тыкает в экран), Matipay думает, что совершена продажа и регистрирует ее как бесплатную
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.9':
        bot.send_message(callback.message.chat.id, '''
 9902
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.10':
        bot.send_message(callback.message.chat.id, '''
• воздушная пробка

• зарос накипью фитинг на входе в бойлер

• неисправен счетчик воды

• кончилась вода в канистре, и ТА засосал воздух, образовалась воздушная пробка

Отсоединить шланг на выходе из счетчика воды, включить машинку и ждать, чтобы вода полилась.
Подставить емкость для воды! Как только вода пошла, выключить км, вставить обратно шланг и включить обратно. Все должно заработать.

С ОСТОРОЖНОСТЬЮ!
Не помогло - можно снять заглушку с парового бойлера, вкл машинку и подождать, когда вода пойдет. Если км только вырубилась, может пойти пар/кипяток
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.11':
        bot.send_message(callback.message.chat.id, '''
• поставить кофемолку от Оперы, при этом придется снять обе родных кофемолки Калео

• в случае, если у клиента используется только один бункер кофе/кофемолка, переключить контакты на вторую неиспользуемую кофемолку и засыпать кофе в соответствующий бункер
''', protect_content=True)
        bot.send_photo(callback.message.chat.id, open('./Кофемолка от оперы на калео_1.jpg','rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open('./Кофемолка от оперы на калео_2.jpg','rb'), protect_content=True)
        bot.send_photo(callback.message.chat.id, open('./Кофемолка от оперы на калео_3.jpg','rb'), protect_content=True, reply_markup=Delete4)
    elif callback.data == '13.12':
        bot.send_message(callback.message.chat.id, '''https://drive.google.com/drive/folders/1KG22bskIe2nTGEnzwJk0vToUcTeYJeLv''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '13.13':
        bot.send_document(callback.message.chat.id, open(r"./Инструкция по эксплуатации Kalea.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 9.3 Krea - кнопки вопроса
    elif callback.data == '14.1':
        bot.send_message(callback.message.chat.id, '''
• магнит отвалился

• контейнер не вставлен

• разъем на герконе
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.2':
        bot.send_message(callback.message.chat.id, '''
• заменить кофемолку

• заменить дозатор кофе

• заменить вентилятор (ТО вент группы провести)
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.3':
        bot.send_message(callback.message.chat.id, '''
оторвать/отпаять конденсатор на плате управления
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.4':
        bot.send_message(callback.message.chat.id, '''
в КМ два кэшлесса. Использоваться могут оба
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.5':
        bot.send_message(callback.message.chat.id, '''
выключить функцию

• «Активация продаж за наличные» ( Меню 6.1.4>6.1.4.3)

При активной функции каждый раз, когда покупатель  пробует купить напиток (тыкает в экран), Мати думает, что совершена продажа и регистрирует ее как бесплатную
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.6':
        bot.send_message(callback.message.chat.id, '''
• слив

• шланг

• ножки 4шт (М6х40)

• крепеж для шланга

• ведро
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.7':
        bot.send_message(callback.message.chat.id, '''
выключить

• «Код бесплатной продажи»

Данная опция дает возможность бесплатно получить один или неограниченное количество напитков, в зависимости от введенного кода
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.8':
        bot.send_message(callback.message.chat.id, '''
9902
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.9':
        bot.send_message(callback.message.chat.id, '''
• помпа EP8

• погружной насос Bianchi 24V (дополнительно уст блок питания 220V — 24V)

В общем случае нужна высокопроизводительная помпа, чтобы эйр-брейк успевал наполняться водой из канистры, и ТА не уходил в ошибку «Нет воды»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.10':
        bot.send_message(callback.message.chat.id, '''
Когда Vendotek V3 начинает делать сверку с банком раз в сутки, то сразу отваливается вся платежка.

Решение - заменить Vendotek V3 на Vendotek VN
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.11':
        bot.send_document(callback.message.chat.id, open(r"./Инструкция по эксплуатации Krea Touch.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.12':
        bot.send_message(callback.message.chat.id, '''https://drive.google.com/drive/folders/1PRXP7o2odcECzaWl94MWUtdqojTldwWh''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.13':
        bot.send_document(callback.message.chat.id, open(r"./Настройки Krea Touch_ПС & EVA_DTS_HoReCa.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.14':
        bot.send_document(callback.message.chat.id, open(r"./Настройки Krea Touch_ПС & EVA_DTS_Vending.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.15':
        bot.send_document(callback.message.chat.id, open(r"./Включение LOG-файлов на КМ KREA.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '14.16':
        bot.send_message(callback.message.chat.id, '''
Коды работаю при условии, что активирована опция «Код бесплатной продажи»

• 9998 - один напиток

• 9999 - неограниченное количество напитков
''', protect_content=True, reply_markup=Exitt)





# 9.4 Bianchi Gaia - кнопки вопроса
    elif callback.data == '15.1':
        bot.send_message(callback.message.chat.id, '''
• на кнопочной версии - нажать кнопку «Service» на внутренней стороне двери и нажать и держать вторую кнопку слева направо (обычно «Американо»). Начнется сброс ошибок

• на версии с тач-дисплеем - нажать кнопку «Service» на внутренней стороне двери и нажать иконку сброса ошибок
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '15.2':
        bot.send_message(callback.message.chat.id, '''
 Регулируется в меню «Дозы»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '15.3':
        bot.send_message(callback.message.chat.id, '''
Контейнер отходов переполнен. Ошибка появляется после 60-80 напитков.  Сбрасывается путем длительного нажатия кнопки «Service»
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '15.4':
        bot.send_message(callback.message.chat.id, '''
Нажать кнопку «Service» на внутренней стороне двери и прочитать ошибки
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '15.5':
        bot.send_message(callback.message.chat.id, '''
• на тач-версии подключить программатор через разьем, в который подключен дисплей, через флешку залить настройки с вставками/ценниками.

• на кнопочной версии этот разьем пустой
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '15.6':
        bot.send_document(callback.message.chat.id, open(r"./Bianchi Gaia руководство пользователя.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '15.7':
        bot.send_document(callback.message.chat.id, open(r"./Bianchi Gaia руководство техническое.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == '15.8':
        bot.send_message(callback.message.chat.id, '''
Сервисный ключ Bianchi нужен для того, чтобы:

• выставить пресс в «нулевое» положение перед установкой в КМ

• отрегулировать моторедуктор пресса для того, чтобы он выставлял пресс в «нулевое» положение (при условии, что он до этого был отрегулирован физически на «ноль»)

''', protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Bianchi/Сервисный ключ.mp4", 'rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == '15.9':
        bot.send_message(callback.message.chat.id, '''
Выставляем пресс в «нулевое» положение с помощью сервисного ключа
''', protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Bianchi/Выставляем пресс в положение ноль.jpg", 'rb'), protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Bianchi/Выставляем пресс в положение ноль.mp4", 'rb'), protect_content=True, reply_markup=Delete3)
    elif callback.data == '15.10':
        bot.send_message(callback.message.chat.id, '''
Пресс может расскрываться при приготовлении по следующим причинам:

• слишком большое давление воды на выходе бойлера:
     • или помпа (выдает слишком большое давление)

     • bypass (пропускает больше, чем надо давление)

• неправильно отрегулирован моторедуктор пресса, отрегулировать

     • выставить пресс в «нулевое» положение с помощью сервисного ключа

     • установить пресс в КМ

     • открыть заднюю крышку КМ и полчуить доступ к моторедуктору пресса

     • ослабить крепление кулачка на моторедукторе пресса сервисным ключом/гаечным ключом

     • повернуть кулачок так, чтобы его край касался (но не нажимал) ролика микровыключателя

     • затянуть крепление кулачка

     • протестировать

     • в случае, если после тестирования/самодиагностики/оборота пресса, он оказывается закрыт,
    необходимо выставить кулачок в противоположном положении (чтобы он касался ролика микровыключателя другой стороной)''', protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Bianchi/Регулировка моторедуктора пресса.mp4", 'rb'), protect_content=True, reply_markup=Delete2)





# 9.5 Biepi MC1 - кнопки ответа
    elif callback.data == 'bi.1':
        bot.send_document(callback.message.chat.id, open(r"./Biepi/Брошюра.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'bi.2':
        bot.send_document(callback.message.chat.id, open(r"./Biepi/Инструкция.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'bi.3':
        bot.send_document(callback.message.chat.id, open(r"./Biepi/Сервис-мануал.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 10. Общение с клиентом - кнопки вопроса
    elif callback.data == '16.1':
        bot.send_message(callback.message.chat.id, '''
Угостить напитком, попросить клиента позвонить в офис. Деньги клиенту не возвращаем
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '16.2':
        bot.send_message(callback.message.chat.id, '''
При подтверждении технической неисправности в снеке, допускается возврат товара. К примеру, завис продукт или отщелкнулась спираль с привода спирали и продукт не выпал
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '16.3':
        bot.send_message(callback.message.chat.id, '''
Если ТА имеет внешние повреждения, то необходимо их зафиксировать по форме «Бланк фиксации повреждения аппарата» в присутствии ЛПР (лицо, принимающее решения на данной ТП) или другого контактного лица
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '16.4':
        bot.send_message(callback.message.chat.id, '''
Протестировать в присутствии клиента те напитки, которые, по его мнению, невкусные/некачественные.
Проверить дозировки напитков на соответствие стандартам фирмы. Предложить клиенту связаться с менеджером по работе с клиентами
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '16.5':
        bot.send_message(callback.message.chat.id, '''
Угощать клиента кофе разрешено
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '16.6':
        bot.send_message(callback.message.chat.id, '''
Разменивать деньги запрещено. Вежливо отказать, предложить стакан кофе
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '16.7':
        bot.send_message(callback.message.chat.id, '''
Выполняется только по соответствующей задаче в Bitrix от менеджера сопровождения в течение 4 рабочих дней.

Примечание: если перед внесением изменений планируется дегустация, то необходимо обязательное присутствие менеджера сопровождения и ЛПР
''', protect_content=True, reply_markup=Exitt)
    elif callback.data == '16.8':
        bot.send_message(callback.message.chat.id, '''
• обучение по обслуживанию и ремонту эксплуатируемого оборудования вы проходили

• имеете 2 группу допуска по ЭБ, присвоенную комиссией предприятия (нашей компанией)

• удостоверения с собой возить вы не обязаны

• так как автоматы являются собственностью нашей компании, то компания сама определяет порядок допуска персонала к обслуживанию и ремонту

• если клиента не устраивает этот ответ - предлагайте ему через менеджера сделать запрос и получить сканы соответствующих документов
''', protect_content=True, reply_markup=Exitt)





# 11. Инструкции - ответы
    elif callback.data == '17.3':
        bot.send_document(callback.message.chat.id, open(r"./Действия выездного сервисного инженера при подъезде ТА.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 12. Видео-инструкции - ответы
    elif callback.data == 'videoinstrokleyka':
        bot.send_document(callback.message.chat.id, open('./Оклейка ТА.mp4','rb'), protect_content=True, reply_markup=Exitt)

    elif callback.data == 'videocreatezv':
        bot.send_document(callback.message.chat.id, open('./Palm_video/Выбор заявки.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv3':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Создание заявки по типу Другое.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv4':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Создание заявок.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv5':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Комментарий к заявке.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv6':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Закрытие заявки как невыполненная.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv7':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Время работы ТП.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv8':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Ищем просроченное ТО.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv9':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Отмечаем правильно ТО.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv10':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Заводим заявку на загрузку ТА для оператора.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv11':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Отмечаем 2 работы на одной ТП.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv12':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Замена узла, участвующего в ТО.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv13':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Работы при изменении конфигурации СТА.mp4','rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'videocreatezv14':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Делаем предзаказ.mp4','rb'), protect_content=True, reply_markup=Exitt)

    elif callback.data == 'videocreatezv16':
        bot.send_video(callback.message.chat.id,open('./Palm_video/Замена платежной системы.mp4','rb'), protect_content=True, reply_markup=Exitt)





# 13. Инструкции по моделям ТА - кнопки вопроса
    elif callback.data == 'Fast900/1000':
        bot.send_document(callback.message.chat.id, open(r"./FAST_инструкция по эксплуатации.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# 14. Таблицы доз напитков по аппаратам - ответы
    elif callback.data == 'dozer1':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз для Canto X2 Double Cup, 300мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer2':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз для Canto X2 Double Cup, 250мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer3':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Canto Big Cup, 250мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer4':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Canto LB (переделка), 200мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer5':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Canto LB, 150мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer6':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Opera ToGo, 300мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer7':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Opera, 250мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer8':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Concerto LB, 200мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer9':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Concerto LB, 150мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer10':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Kikko Max ToGo, 300мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer11':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз для Kikko Max ToGo, 250мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer12':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Kikko Es6 ToGo, 200мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer13':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз Kikko Max & Kikko Es6, 150мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dozer14':
        bot.send_document(callback.message.chat.id, open(r"./Tablici_doz/Таблица доз КАЛЕА_КРЕА 250мл.pdf", 'rb'), protect_content=True, reply_markup=Exitt)





# Каталоги запчастей - ответы
    elif callback.data == 'Bianchi':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Bianchi.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'BiepiMC_1':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/BiepiMC_1.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Canto_Double_Cup':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Canto_Double_Cup.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Canto_LB':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Canto_LB.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'CantoLB_Big_Cup_250ml':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/CantoLB_Big_Cup_250ml.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Concerto_LB':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Concerto_LB.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'FAS1050':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/FAS1050.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Gaia':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Gaia.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Kalea':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Kalea.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Kikko_Es':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Kikko_Es.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Kikko_Max':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Kikko_Max.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Koro':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Koro.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'KORO_FM':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/KORO_FM.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Krea':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Krea.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Maestro_X2_Double_Cup_Double_Cup_BIG':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Maestro_X2_Double_Cup_Double_Cup_BIG.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Opera':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Opera.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Opera_ToGo':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Opera_ToGo.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Snakky_Jazz':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Snakky_Jazz.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Snakky_LX':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Snakky_LX.pdf", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'Snakky_Max':
        bot.send_document(callback.message.chat.id, open(r"./Catalog_zapch/Snakky_Max .pdf", 'rb'), protect_content=True, reply_markup=Exitt)




#Размещение допоборудования на ТА
    elif callback.data == 'dopMaestro/Canto':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Maestro_Canto.jpg", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dopOpera':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Opera.jpg", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dopConcerto':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Concerto.jpg", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dopKikkoMax':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Kikko Max.jpg", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dopKikkoEs6':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Kikko ES6.jpg", 'rb'), protect_content=True, reply_markup=Exitt)
    elif callback.data == 'dopSnakkyJazz':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Snakky Jazz_Vendotek.jpg", 'rb'), protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Snakky Jazz_MyVend.jpg", 'rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == 'dopSnakkyMax':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Snakky Max_Vendotek.jpg", 'rb'), protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Snakky Max_MatiPay.jpg", 'rb'), protect_content=True, reply_markup=Delete2)
    elif callback.data == 'dopSnakkyLX':
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Snakky LX_Vendotek.jpg", 'rb'), protect_content=True)
        bot.send_document(callback.message.chat.id, open(r"./Размещение допоборудования на ТА/Snakky LX_MyVend.jpg", 'rb'), protect_content=True, reply_markup=Delete2)


bot.polling(none_stop=True, timeout=123)
