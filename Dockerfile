FROM python:3
WORKDIR /muscle
COPY . .
RUN chmod +x app/execute.sh
