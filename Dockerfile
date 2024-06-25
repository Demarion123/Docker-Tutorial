FROM python
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python","app.py"]