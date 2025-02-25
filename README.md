# WasteSorting

Этот бот будет сортировать мусор

## Автор
Айбын Нугманов

## Способности

- Определяет, изображены и куда выкидывать мусор если есть.
- Показовает куда мусор выкидывать.


## Как это работает

Этот бот использует обученную модель для классификации изображений. После того как пользователь отправляет изображение, бот выполняет следующие шаги:

1. Загружает изображение.
2. Применяет модель для предсказания, является ли на мусор и куда его выкидывать .
3. Возвращает результат классификации с уверенностью.
4. Пишет куда выкидывать мусор

## Демонстрация работы
![Alt Text](https://i.postimg.cc/0NXv875w/2025-02-25-215751.png)
![Alt Text](https://i.postimg.cc/MGCsbGdL/2025-02-25-220259.png)

## Требования

- Python 3.x
- Библиотеки:
  - `telebot` — для работы с Telegram API.
  - `keras` и `tensorflow` — для работы с моделью машинного обучения.
  - `pillow` — для обработки изображений.
  - `numpy` — для работы с массивами данных.
