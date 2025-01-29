# Используем базовый образ Python
FROM python:3.11

# Устанавливаем зависимости
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --upgrade pip

# Копируем файлы проекта
COPY . /app

# Переходим в директорию с проектом
WORKDIR /app

# Устанавливаем необходимые пакеты из файла requirements.txt
RUN pip install -r requirements.txt

# Выполняем main.ipynb
CMD ["python", "main.ipynb"]
