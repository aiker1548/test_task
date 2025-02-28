# FastAPI Web Service

Этот проект представляет собой веб-сервис на FastAPI, который выводит сообщение с динамическими параметрами, переданными через GET-запрос. Текст "Recruto" и сообщение "Давай дружить" подставляются из параметров запроса.

## Стек технологий:
- **Python 3.11**
- **FastAPI** — для создания веб-сервиса.
- **Uvicorn** — ASGI сервер для запуска FastAPI.
- **Docker** — для контейнеризации приложения.

## Установка и запуск

### 1. Клонирование репозитория

Клонируйте репозиторий на свою машину:

```bash
git clone https://github.com/your-username/fastapi-web-service.git
cd fastapi-web-service
2. Установка зависимостей
Установите все зависимости с помощью pip:

bash
Copy
Edit
pip install -r requirements.txt
3. Запуск приложения с помощью Docker
Чтобы запустить приложение в Docker, выполните следующие шаги:

Построить образ Docker:

bash
Copy
Edit
docker build -t fastapi-web-service .
Запустить контейнер с монтированием папки для логов:

bash
Copy
Edit
docker run -d -p 8000:8000 -v /path/to/local/logs:/app/logs --name fastapi-service fastapi-web-service
Замените /path/to/local/logs на путь на хост-машине, где хотите хранить логи. Теперь логи будут писаться как в контейнер, так и на хост.

4. Запрос к сервису
Для того чтобы получить ответ от сервиса, отправьте GET-запрос с параметрами name и message:

bash
Copy
Edit
http://localhost:8000/?name=Recruto&message=Давай%20дружить
Ответ будет:

nginx
Copy
Edit
Hello Recruto! Давай дружить!
5. Логи
Логи сервиса записываются в файл logs/app.log внутри контейнера. Если вы хотите сохранить их на хост-машине, используйте volume, как показано в примере запуска Docker. Логи будут также выводиться в консоль.
