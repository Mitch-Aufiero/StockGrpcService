import grpc
import stock_pb2
import stock_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = stock_pb2_grpc.StockServiceStub(channel)
    
    request = stock_pb2.StockRequest(symbol="AAPL")
    response_iterator = stub.GetStockDataStream(request)

    for response in response_iterator:
        print(f"Symbol: {response.symbol}, Open: {response.open}, High: {response.high}, Low: {response.low}, Close: {response.close}")

if __name__ == "__main__":
    run()
