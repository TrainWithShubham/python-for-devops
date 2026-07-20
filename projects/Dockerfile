# Take patila

FROM python:3.14


#Add ingredients

WORKDIR  /app

COPY . .

#Mix / process the items

RUN  pip install -r requirements.txt

EXPOSE 8000

#Gas on

CMD ["python", "main.py"]
