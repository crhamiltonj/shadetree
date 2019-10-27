FROM python:slim
LABEL maintainer="crhamiltonj@gmail.com"
EXPOSE 5000/tcp
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
VOLUME ["/app"]
ENV FLASK_APP=wsgi
ENV FLASK_ENV=development

