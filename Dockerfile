FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
COPY ml/registry ml/registry
ENV MODEL_PATH=ml/registry/model.pkl
EXPOSE 5000
CMD ["python", "app/main.py"]
