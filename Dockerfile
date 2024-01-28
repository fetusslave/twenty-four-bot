FROM python:3.10-bullseye
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .
RUN echo "GUILD_ID: $GUILD_ID"
RUN echo "DISCORD_TOKEN: $DISCORD_TOKEN"
CMD ["python3", "main.py"]
