FROM python:3.6-alpine3.7
WORKDIR /app
COPY ./ /app
RUN python -V
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r ./requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "-m", "waitress",  "--port", "5000", "--call", "api:create_app" ]