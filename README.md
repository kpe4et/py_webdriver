# py_webdriver
Финальный проект от Stepik по Python  Webdriver

#Я привык называть корзину CART, а не BASKET =) Хотя в названиях тестов оставил BASKET, для удобства ревьюера. 
Но файлы, методы и локаторы у меня CART, прошу понять и простить))

Попытка осмыслить и перенести "на бумагу" структуру.
В base_page храним класс, описывающий общие методы работы со страницами
В main_page и login_page содержатся классы, отнаследованные от базового, с описыванием частных методов работы с отдельными страницами
В locators.py мы описываем константы-локаторы элементов страниц
В test_main_page хранятся тесты, использующие классы страниц и их локаторы
Возможно в одном классе создать объект(экземпляр) другой страницы. Передав в нее объект браузера в текущем состоянии
