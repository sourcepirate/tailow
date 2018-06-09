FROM python:3.5-alpine
WORKDIR /src
RUN apk update
COPY . /src

ENTRYPOINT [ "python", "setup.py", "test" ]