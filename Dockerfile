FROM python:3.13.7-bookworm

WORKDIR /lolei-app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -ms /bin/bash dockeruser
RUN chown -R dockeruser:dockeruser /lolei-app
USER dockeruser

ENTRYPOINT ["uwsgi", "--ini"]
CMD ["/lolei-app/uwsgi.dev.ini"]
