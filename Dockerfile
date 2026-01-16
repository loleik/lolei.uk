FROM python:3.13-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /lolei-app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -ms /bin/bash dockeruser
RUN chown -R dockeruser:dockeruser /lolei-app
USER dockeruser

ENTRYPOINT ["uwsgi", "--ini"]
CMD ["/lolei-app/uwsgi.dev.ini"]
