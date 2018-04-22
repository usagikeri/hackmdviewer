FROM python:3.6

LABEL maintainer="usagikeri <a.k.a.usagikeri@gmail.com>"
LABEL env="dev"

RUN pip install flask   \
        mysqlclient     \
        sqlalchemy      \
        ipython

VOLUME ../src/:/home/

CMD ["python","/home/app.py"]
