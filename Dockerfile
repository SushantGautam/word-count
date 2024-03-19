FROM python:3.10
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt
