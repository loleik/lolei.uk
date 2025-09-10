FROM python:3.13.7-bookworm

WORKDIR /lolei-skeleton

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]
