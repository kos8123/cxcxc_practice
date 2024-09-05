FROM python:3.11
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3306
CMD ["python3", "main.py"]
