FROM python:3.10


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


#build python protoc files
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. stock.proto

#standard gprc port
EXPOSE 50051

CMD ["sleep","infinity"]