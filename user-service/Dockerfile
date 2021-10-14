FROM python:3.9

WORKDIR /home/user-service

ENV FLASK_APP flasky.py
ENV FLASK_CONFIG production

COPY .env .env
COPY app app
COPY migrations migrations
COPY flasky.py config.py requirements.txt ./

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

EXPOSE 5000

CMD [ "venv/bin/python", "-m", "flask", "run", "--host", "0.0.0.0" ]