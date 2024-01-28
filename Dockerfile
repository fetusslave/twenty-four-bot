FROM python:3.10-bullseye
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]
