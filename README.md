django_my_project

Создание интернет-магазина. 

Шаг 1. (Сделано)

Критерии выполнения заданий

    Всё итоговое решение залили в github.com и сдали в виде ссылки на репозиторий.
    Создали отдельное приложение.
    Реализовали два контроллера.
    Адреса описали не внутри главного URL-файла, а вынесли в пространства имен.
    Добавили папку с шаблонами, в которой лежат два шаблона.

Задание 1
Для начала работы над задачей выполните первые шаги:

    Настройте виртуальное окружение.
    Создайте новый Django-проект.

Задание 2
После успешного создания проекта сделайте первую настройку. Для этого:

    Создайте первое приложение с названием
    catalog .
    Внесите начальные настройки проекта.
    Сделайте настройку урлов (URL-файлов) для нового приложения.

Задание 3
Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.

    Для создания шаблонов лучше использовать UIkit Bootstrap. Это удобный набор элементов, которые уже стилизованы и готовы к использованию. UIkit Bootstrap помогает избежать самостоятельной верстки макетов.

    Если возникнут проблемы при создании собственного интерфейса, возьмите за основу данный шаблон: https://github.com/oscarbotru/.

Задание 4
В приложении в контроллере реализуйте два контроллера:

    Контроллер, который отвечает за отображение домашней страницы.
    Контроллер, который отвечает за отображение контактной информации.

* Дополнительное задание
Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.

    Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.

Шаг 2 (сделано)

Критерии выполнения заданий

    Результат выполнения проекта залейте на GitHub и сдайте в виде ссылки на репозиторий.
    Результаты работы по первому пункту в задании 6 прикрепите в виде скриншотов терминала.

Задание 1
Подключите СУБД PostgreSQL для работы в проекте, для этого:

    Создайте базу данных в ручном режиме.
    Внесите изменения в настройки подключения.

Задание 2
В приложении каталога создайте модели:

        Product,
        Category.

    Опишите для них начальные настройки.
    К начальным настройкам модели относятся метод  __str__ и class Meta с описанием свойств модели.

Задание 3
Для каждой модели опишите следующие поля:

    Product
        Наименование
        Описание
        Изображение (превью)
        Категория
        Цена за покупку
        Дата создания (записи в БД)
        Дата последнего изменения (записи в БД)
    Category
        Наименование
        Описание

    Свяжите продукт и категорию, используя связь между таблицами «Один ко многим».

    У одной категории может быть много продуктов, но у одного продукта может быть только одна категория.
    Воспользуйтесь специальным полем модели — ForeignKey().
    Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей. 
    Их общепринятые названия — created_at и updated_at соответственно.
    Примечание
    Для поля с изображением необходимо добавить соответствующие настройки (MEDIA URL, MEDIA ROOT, настроить URL для отображения медиаданных) в проект, 
    а также установить библиотеку для работы с изображениями Pillow

Задание 4
Перенесите отображение моделей в базу данных с помощью инструмента миграций, для этого:

    создайте миграции для новых моделей;
    примените миграции;
    внесите изменения в модель продукта, добавьте поле «Дата производства продукта» (manufactured_at), 
    примените обновление структуры с помощью миграций;
    откатите миграцию до состояния, когда поле «Дата производства продукта» (manufactured_at) 
    для модели продукта еще не существовало, и удалите лишнюю миграцию.
    Важно сохранять всю историю миграций проекта для сохранения целостности базы данных проекта.
    Не забудьте добавить все выполненные миграции в коммит, а затем отправить в удаленный репозиторий на GitHub.

Задание 5
Для моделей категории и продукта настройте отображение в административной панели. 
Для категорий выведите id и наименование в список отображения, а для продуктов 
выведите в список id, название, цену и категорию.

    При этом интерфейс вывода продуктов настройте так, 
    чтобы можно было результат отображения фильтровать по категории, 
    а также осуществлять поиск по названию и полю описания.

Задание 6
Через инструмент shell заполните список категорий, а также выберите список категорий, 
применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.

        Установите библиотеку ipython для комфортной работы с инструментом shell

Сформируйте фикстуры для заполнения базы данных.

    Фикстуры создайте командой. Для управления кодировкой используйте опцию -Xutf8
    для команды. Такой параметр уместно будет использовать на операционной системе Windows.

    В общем случае команда для создания фикстур будет выглядеть следующим образом:    
    python -Xutf8 manage.py dumpdata имя_приложения > имя_папки_с_фикстурами/имя_приложения_data.json

    Напишите кастомную команду, которая умеет заполнять данные в базу данных, 
    при этом предварительно ее зачищать от старых данных. 

    Примечание
    Последний пункт можно реализовать в связке с инструментом работы с фикстурами, можно описать вставку данных отдельными запросами.

Дополнительное задание

        В контроллер отображения главной страницы добавить выборку последних пяти товаров и вывод их в консоль.
        Создать модель для хранения контактных данных и попробовать вывести данные, заполненные через админку, на страницу с контактами.

Примечание: дополнительные задания, помеченные звездочкой, желательны, но не обязательны к выполнению.
