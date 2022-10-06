FROM python:3.9.7-slim

WORKDIR /empowerchain

COPY . .
RUN pip3 install -r requirements.txt
#RUN pip install --upgrade pip; \
    #pip install -r requirements.txt
ENTRYPOINT ["python3","discord1.py"]
