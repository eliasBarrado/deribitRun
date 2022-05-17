FROM python:3.8
COPY . /project
WORKDIR /project
ENV GOOGLE_APPLICATION_CREDENTIALS="key.json"
RUN pip install -r requirements.txt
#CMD ["python","main.py"]
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app