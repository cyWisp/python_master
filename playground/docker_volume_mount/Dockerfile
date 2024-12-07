FROM python:3.12.5-slim-bullseye
ENV PYTHONBUFFERED=1

RUN mkdir /usr/src/app
RUN mkdir /usr/src/app/target

WORKDIR /usr/src/app

RUN /usr/local/bin/python3.12 -m pip install --upgrade pip
RUN rm -rf ~/.cache/pip

COPY . /usr/src/app

RUN /usr/local/bin/python3.12 -m pip install -r requirements.txt
CMD ["/usr/local/bin/python3.12", "/usr/src/app/main.py"]