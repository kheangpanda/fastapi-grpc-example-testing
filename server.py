import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
import clients_pb2
import clients_pb2_grpc



class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)
    
class ClientsServicer(clients_pb2_grpc.ClientsServicer):
    def Add(self, request, context):
        print("request --- ",request)
        result = request.firstName + request.lastName

        return clients_pb2.AddResponse(fullname=result)
def serve():
    print("Working")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    clients_pb2_grpc.add_ClientsServicer_to_server(ClientsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    serve()