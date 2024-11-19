import grpc
import clients_pb2
import clients_pb2_grpc

def run(firstName, lastName, gender):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = clients_pb2_grpc.ClientsStub(channel)
        response = stub.Add(clients_pb2.AddRequest(firstName=firstName, lastName=lastName, gender=gender))
    print(f"Result: {response.fullname}")

if __name__ == '__main__':
    # Get user Input 
    firstName = input("Please input firstName: ")
    lastName = input("Please input lastName: ")
    gender = input("Please input gender: ")
    run(firstName, lastName,gender)