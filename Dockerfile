FROM python:3.10
WORKDIR /usr/src/
COPY . ./
RUN wget https://github.com/jgthms/bulma/releases/download/0.9.4/bulma-0.9.4.zip porfolio/static/\
    && unzip portfolio/static/bulma-0.9.4.zip \
    && rm portfolio/static/bulma-0.9.4.zip \
    && pip install --upgrade pip \
    && pip install -r requirements.txt