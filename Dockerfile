FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY services .
# 暴露应用运行端口
EXPOSE 5000

# 启动应用
CMD ["python", "app.py"]
