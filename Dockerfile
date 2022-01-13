FROM python:3-alpine
WORKDIR /tmp
COPY requirements.txt ./
RUN pip3 install -r requirements.txt && rm requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3","./login.py"]