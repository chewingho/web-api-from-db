FROM python:3.7.4
LABEL maintainer kateho
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python book.py