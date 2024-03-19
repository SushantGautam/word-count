FROM python:3.10
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

#  build:
# run: docker run --rm -it word-count /bin/bash
# reproduce: python code/count.py  --path data --output figures