
# using python 2.7
FROM arnulfosolis/python:latest

ENV PATH="/app/bin:${PATH}"

ENV PYTHONPATH="/app/src"

COPY . /app

WORKDIR /app

RUN pip install --ignored-installed -r requirements.txt

WORKDIR /app/src

EXPOSE 5000

ENTRYPOINT [""]

CMD ["gunicorn", "-c", "/app/conf/app/conf.py", "init:application"]

