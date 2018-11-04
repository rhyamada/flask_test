FROM python
RUN mkdir -p /opt/python
WORKDIR /opt/python
RUN pip install flask flask-sqlalchemy flask-admin
CMD ["python","run.py"]