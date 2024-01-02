FROM python:3.11-slim

RUN mkdir -p /kitchen/kitchen

WORKDIR /kitchen

RUN pip install -U pip
COPY requirements.txt /kitchen/
RUN pip install -r requirements.txt

COPY api /kitchen//kitchen/api/
COPY oas.yaml /kitchen/oas.yaml
COPY . /kitchen/

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000", "--reload"]

