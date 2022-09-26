FROM python:3.7.5-slim
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install flask
RUN pip install pytest
RUN pip install requests

ADD server.py /

EXPOSE 80
CMD ["python", "./server.py"]