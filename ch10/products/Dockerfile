FROM python:3.11-slim

RUN mkdir -p /products/products

WORKDIR /products

RUN pip install -U pip
COPY requirements.txt /products/
RUN pip install -r requirements.txt

COPY web /products/products/web/
COPY web/products.graphql /products/web/
COPY . /products/

EXPOSE 8000

CMD ["uvicorn", "server:server", "--host", "0.0.0.0", "--port", "8001", "--reload"]