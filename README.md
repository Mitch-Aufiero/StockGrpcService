# StockGrpcService

This application is a learning sandbox for learning gRPC. I will using a stock data as a use case. Since we don't have a have the means to hook into live intraday data(and the purpose is to learn about gRPC and not 3rd party services), we will be generating it randomly. In addition to the randomly generated data we will be visualizing it with React (our gRPC client). Since browsers do not natively support gRPC, we are using [Envoy](https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy) as a bridge from our React client to the gRPC service.

# Proj Structure
The project is broken down into 2 sections: 
`Stock StreamService` which is used to generate and send stock data.
`Frontend` which is used to consume and visualize the data.
```bash
EnvoyProxy/
│
├── envoy.yaml               # config file specifying our mapping for the envoy proxy
├── Dockerfile               # docker file for the envoy service
|
StockStreamService/
│
├── server.py                # entry point for our server.
├── stock.proto              # Our protocol buffer agreement file
├── requirements.txt         # python project package dependencies
├── Dockerfile               # docker file for the backend service
│
Frontend/                     # front end structure
│  
```





