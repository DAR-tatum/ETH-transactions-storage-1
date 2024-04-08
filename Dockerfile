FROM python:3.8-slim

WORKDIR /ETH-transactions-storage
COPY . .

RUN pip install --no-cache-dir -vvv -r requirements.txt

RUN python3.8 ethtest.py
RUN python3.8 pgtest.py


CMD [ "python3.8", "./ethsync.py" ]