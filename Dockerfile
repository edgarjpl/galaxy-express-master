# App build #######################################################################################
FROM python:3.9 as production

RUN pip install --no-cache-dir pip==20.2.3 && \
    python -m venv /usr/local/lib/venv && \
    /usr/local/lib/venv/bin/pip install --no-cache-dir setuptools==47.1.0 wheel==0.36.2
ENV PATH /usr/local/lib/venv/bin:$PATH

WORKDIR /src

COPY ./requirements.txt /src/
RUN pip install -r requirements.txt

COPY . /src
RUN python setup.py develop && python setup.py build

ARG BASEPLATE_CONFIG_PATH
ENV BASEPLATE_CONFIG_PATH $BASEPLATE_CONFIG_PATH

EXPOSE 9090

CMD ["scripts/container-run.sh"]

# Dev build #######################################################################################
FROM production as development

RUN pip install -r requirements-dev.txt
