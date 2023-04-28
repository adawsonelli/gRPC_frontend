# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import cosine_pb2
import cosine_pb2_grpc


def run():
    print("let's calculate cosine on a server")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cosine_pb2_grpc.CosineStub(channel)
        amplitude = 1; freq = 1 ; phase = .5
        response = stub.GetCos(cosine_pb2.CosRequest(amplitude=amplitude,freq=freq,phase=phase))
        print("cos client received: " + str(response.data))

def CosSend(amplitude,freq,phase,addr="localhost"):
    """
    use a gRPC server to send a remote cosine computation request
    inputs:
        amplitude,freq,phase - wave parameters
        addr - IP address and port of the remote server
    """
    with grpc.insecure_channel(addr + ':50051') as channel:
        stub = cosine_pb2_grpc.CosineStub(channel)
        response = stub.GetCos(cosine_pb2.CosRequest(amplitude=amplitude,freq=freq,phase=phase))
        data = [ele for ele in response.data]
        return data




if __name__ == '__main__':
    logging.basicConfig()
    run()