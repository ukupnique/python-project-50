### Учебный проект GenDiff. Используется для сравнения файлов и вывода отличий в них


### Установка


Для установки и запуска проекта вам потребуется Python версии 3.10 и выше, а также инструмент для управления зависимостями Poetry.
- Склонируйте репозиторий с проектом на ваше локальное устройство:

```

git clone git@github.com:ukupnique/python-project-50.git
```
- Перейдите в директорию проекта:

```
cd python-project-50
```
- Установите необходимые зависимости с помощью Poetry:

```
poetry install
```

### Поддерживаемые форматы файлов


Проект поддерживает следующие форматы файлов для поиска отличий:
- YAML (.yaml, .yml)

- JSON (.json)

***

### Как найти различия между двумя файлами


- Поместите два файла, которые вы хотите сравнить, в папку tests/fixtures.

- Выполните команду для поиска различий:

```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```
- Замените file1.json и file2.json на названия ваших файлов.

***

### Форматы вывода


Для выбора формата вывода различий укажите флаг -f с названием форматтера. Возможные варианты:
- stylish (по умолчанию)

- plain

- json

### Примеры команд для разных форматов вывода:


- Вывод в стиле stylish:

```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```
- Вывод в формате plain:

```
poetry run gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
```
- Вывод в формате json:

```
poetry run gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
```

***

### Hexlet tests and linter status:
[![Actions Status](https://github.com/ukupnique/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ukupnique/python-project-50/actions)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a160070a2e498302387c/test_coverage)](https://codeclimate.com/github/ukupnique/python-project-50/test_coverage)

