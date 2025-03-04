import grpc
import stock_pb2
import stock_pb2_grpc
import time
import random
from concurrent import futures
from datetime import datetime
from grpc_reflection.v1alpha import reflection



class StockService(stock_pb2_grpc.StockServiceServicer):
    def GetStockDataStream(self, request,context):
        symbol = request.symbol
        #setting random starting price
        price = random.uniform(100,200) 

        while True:
            # randomly generating the data. in theory all 4 should be determined by the price and date time together, but this is a good starting point to get some data
            change = random.uniform(-1,1)
            price = price + change
            high = price + random.uniform(0,5)
            low =  price - random.uniform(0,5)
            close = (high + low) / 2

            stock_data = stock_pb2.StockData(
                symbol = symbol,
                datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                open=price,
                high = high,
                low = low,
                close = close,

            )

            yield stock_data
            time.sleep(.5)

def serve():
    print("StockStreamService is booting up...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5)) #not sure if I need any other params here yet since they're optional
    stock_pb2_grpc.add_StockServiceServicer_to_server(StockService(), server)

    service_names = (
    stock_pb2.DESCRIPTOR.services_by_name['StockService'].full_name,
    reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)


    server.add_insecure_port("0.0.0.0:50051")

    server.start()
    print("StockStreamService starting on port 50051")

    server.wait_for_termination()


if __name__=="__main__":
    print("howdy")
    serve()


