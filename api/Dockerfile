FROM python:3.9 as requirements-stage

WORKDIR /temp

RUN pip install poetry

COPY ./pyproject.toml /poetry.lock* /temp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9

COPY --from=requirements-stage /temp/requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./api /api

WORKDIR /api

CMD ["sh", "start.sh"]