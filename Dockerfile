FROM python:3.10-alpine3.15

RUN echo 'installing bash and nano in alpine'
RUN apk add --no-cache bash nano

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python3", "-m" , "flask", "run", "--port=80", "--host=0.0.0.0"]