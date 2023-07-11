# start by pulling the python image
FROM python:3.11-slim as python-base

ENV POETRY_VERSION=1.4.2\
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/app" \
    VENV_PATH="/app/.venv" 

# Prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

# install poetry
RUN pip3 install poetry

# switch working directory
WORKDIR $PYSETUP_PATH
COPY ./app /app
COPY ./pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev -vvv

CMD [ "python","server.py" ]
