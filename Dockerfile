FROM python:3.11-slim

# نصب پیش‌نیازها و هسته Xray
RUN apt-get update && apt-get install -y curl unzip systemctl
RUN bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PORT=8080
EXPOSE 8080
CMD ["python", "main.py"]
