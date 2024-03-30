FROM python:3.10
ARG guild_id
ARG discord_token
ENV GUILD_ID=$guild_id
ENV DISCORD_TOKEN=$discord_token
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]
