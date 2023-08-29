FROM python:latest

WORKDIR /github/workspace

COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "postswitch.py"]