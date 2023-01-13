FROM python:3.10.5


ENV PYTHONUNBUFFERED 1

WORKDIR /Photo_Album
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000