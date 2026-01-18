FROM python:3.9-slim
RUN pip install fastapi uvicorn
COPY . /app
WORKDIR /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]