FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app/ /code/app

HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD curl -f http://localhost:9696/healthcheck || exit 1

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "9696"]