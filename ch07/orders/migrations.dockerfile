FROM python:3.11-slim

RUN mkdir -p /orders/orders

WORKDIR /orders

RUN pip install -U pip
COPY orders/requirements.txt /orders/
RUN pip install -r requirements.txt

#RUN pipenv install --dev --system --deploy

COPY orders/repository /orders/orders/repository/
COPY ../migrations /orders/migrations
COPY ../alembic.ini /orders/alembic.ini

ENV PYTHONPATH=/orders


CMD ["alembic", "revision", "--autogenerate", "-m", "'Initial migration'"]
CMD ["alembic", "upgrade", "heads"]
