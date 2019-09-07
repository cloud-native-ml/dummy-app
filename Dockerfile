FROM python:3.7

RUN pip install tornado
COPY ./src /src

ENTRYPOINT ["python", "/src/main.py"]