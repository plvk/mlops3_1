Цель задания

Вам необходимо настроить CI/CD-пайплайн для автоматизации сборки проекта, линтинга кода, публикации пакета и документации на GitLab Pages. Также нужно провести разведочный анализ данных (EDA) на предложенном датасете Credit Default и представить результаты в виде отчета.

Датасет содержит информацию о клиентах с указанием их дохода, возраста, суммы кредита и отношения кредита к доходу, а также бинарный таргет Default, указывающий на факт дефолта по кредиту (1 — дефолт, 0 — нет).

Основные признаки:

Income — годовой доход клиента.
Age — возраст клиента.
Loan — сумма кредита, который был предоставлен клиенту.
Loan to Income — отношение суммы кредита к доходу клиента.
Default — бинарный таргет, указывающий, попал ли клиент в дефолт (1 = дефолт, 0 = нет).

Шаги задания

Часть 1: Настройка CI/CD пайплайна

1. Сборка Docker-образа с DinD (Docker-in-Docker):
   
-Настройте CI/CD пайплайн для сборки Docker-образа вашего проекта.

-Опубликуйте собранный образ в GitLab Docker Registry.

2. Линтеринг и форматирование кода:
   
-Добавьте этапы линтинга и форматирования кода с использованием Flake8 и Black в ваш CI/CD пайплайн.

-Убедитесь, что код проверяется на соответствие стандартам и автоматически форматируется.

3. Сборка и публикация Python-пакета:
   
-Добавьте этап сборки вашего проекта в виде Python-пакета.

-Опубликуйте собранный пакет в GitLab PyPI Registry.

4. Сборка документации:
   
-Используйте Quarto или Jupyter для генерации документации в формате HTML.

-Настройте CI/CD пайплайн для публикации сгенерированной документации на GitLab Pages.

5. Секреты и переменные:
   
-Используйте masked variables для хранения credentials, таких как токены доступа и пароли, необходимых для публикации в GitLab Registry.

Часть 2: Разведочный анализ данных (EDA)

Используя датасет Credit Default.csv, проведите следующие шаги:

1. Предварительный обзор данных:
   
-Загрузите данные и отобразите несколько первых строк таблицы, чтобы понять структуру данных и типы признаков (например, Income, Loan, Age и бинарный таргет Default).

2. Анализ пропущенных значений:
   
-Постройте таблицы и графики, показывающие объем пропущенных значений в данных.

-Используйте pie chart или bar chart для визуализации процентного соотношения пропущенных значений по столбцам.

3. Построение диаграмм попарного распределения признаков:
   
-Постройте диаграммы попарного распределения признаков, таких как доход (Income), возраст (Age), сумма кредита (Loan) и таргет Default, с использованием библиотеки seaborn или plotly.

4. Корреляционный анализ:
   
-Рассчитайте матрицу корреляций для числовых признаков (например, Income, Loan, Loan to Income) и визуализируйте ее с помощью heatmap.

5. Анализ баланса классов:
   
-Проанализируйте баланс классов (дефолт/не дефолт) и визуализируйте распределение классов с помощью bar chart.

6. Заключение и выводы:
   
-Зафиксируйте ваши наблюдения и выводы по результатам исследования.

-Опишите любые аномалии или интересные моменты, которые вы заметили в данных (например, влияние возраста или дохода на вероятность дефолта). Это можно сделать в jupyter notebook либо в файле README.MD
