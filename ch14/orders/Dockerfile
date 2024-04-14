FROM python:3.11-slim

RUN mkdir -p /orders/orders

WORKDIR /orders

RUN pip install -U pip
COPY requirements.txt /orders/
RUN pip install -r requirements.txt

COPY orders_service /orders/orders/orders_service/
COPY repository /orders/orders/repository/
COPY web /orders/orders/web/
COPY oas.yaml /orders/
COPY public_key.pem /orders/public_key.pem
COPY private_key.pem /orders/private_key.pem
COPY . /orders/

EXPOSE 8000

ENV AUTH_ON=True
CMD ["uvicorn", "web.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
