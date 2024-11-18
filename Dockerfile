FROM python:3.8-slim
WORKDIR /app
COPY app.py /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8820
CMD ["python", "app.py"]