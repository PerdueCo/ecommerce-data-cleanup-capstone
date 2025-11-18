FROM python:3.11-slim
WORKDIR /app
COPY ./src/cleaner.py ./cleaner.py
COPY ./data ./data
RUN pip install pandas
CMD ["python", "cleaner.py"]
