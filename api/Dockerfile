FROM python:3.11

WORKDIR /opt/api
COPY ./requirements.txt /opt/api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/api/requirements.txt

COPY . /opt/api

EXPOSE 8000
CMD ["python", "-m", "run"]