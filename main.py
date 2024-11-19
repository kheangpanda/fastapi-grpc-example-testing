
from fastapi import FastAPI
from typing import Union
import uvicorn

import grpc
import calculator_pb2
import calculator_pb2_grpc

app = FastAPI()

@app.get("/")
def read_root():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(num1=20, num2=3))
    print(f"Result: {response.result}")
    return {"Result": {response.result}}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}