FROM python:3.8
ADD main.py /
ADD requirements.txt /
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 80
CMD ["python", "main.py"]
