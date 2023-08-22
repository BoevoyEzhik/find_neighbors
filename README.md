<h1>Техническое задание</h1>
Напишите REST-сервис для поиска соседей. Основная функция - сервис должен позволить запросить K ближайших соседей пользователя N в радиусе M километров.

У каждого пользователя есть:
<ul>
<li>ID (int64);</li>
<li>имя (строка до 128 символов);</li>
<li>координаты (числа с плавающей точкой - 2D, на плоскости, сфере или геоиде - на выбор).</li>
</ul>  
Помимо поиска сервис должен позволять создавать пользователей с указанными ID, именами и координатами обеспечивая уникальность ID.<br></br>

<h1>Описание проекта</h1>
Решение было написано для координатной плоскости. Также в проекте представлен работоспособный докерфайл.<br></br>

Проект представлен как тестовый стенд возможностей программиста.

<h1>Решение</h1>
Находим соседей через гипотенузу от каждого пользователя в указанном радиусе.  