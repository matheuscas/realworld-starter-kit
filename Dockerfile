FROM python:3.6.1

WORKDIR /app

ADD ./src /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]





