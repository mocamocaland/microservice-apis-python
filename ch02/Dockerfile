FROM python:3.11-slim

RUN mkdir -p /orders/orders

WORKDIR /orders

RUN pip install -U pip
COPY requirements.txt /orders/
RUN pip install -r requirements.txt

COPY orders/api /orders/orders/api/
COPY oas.yaml /orders/oas.yaml
COPY . /orders/

EXPOSE 8000

CMD ["uvicorn", "orders.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

