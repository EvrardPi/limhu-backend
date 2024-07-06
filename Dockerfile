FROM python:3.12

WORKDIR /usr/src/app

COPY requirements/* ./

RUN if [ "$ENV" != "prod" ]; \
    then pip3 install pytest && \
    pip install -r ./dev.txt \
    ; else pip install -r ./base.txt \
    ; fi

COPY . .

RUN chmod +x ./start.sh

CMD [ "./start.sh" ]
