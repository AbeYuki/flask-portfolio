FROM python:3.10
WORKDIR /usr/src/
COPY ./portfolio/ ./portfolio
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn", "portfolio.app:create_app()"]
CMD ["--workers", "2", "--bind", "0.0.0.0:80", "--max-requests", "100", "--log-level", "info", "--capture-output"]
