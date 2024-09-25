FROM python:3.9-alpine

WORKDIR /api_code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "api_app.py"]