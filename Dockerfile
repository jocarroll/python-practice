FROM python:3.7.0-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
