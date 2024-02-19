FROM python:3.11.4
RUN apt -y update -y && apt -y upgrade && apt -y install wget
WORKDIR /
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "app:app" ]
