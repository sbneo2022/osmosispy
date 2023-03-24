"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import osmosis.twap.v1beta1.query_pb2

class QueryStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Params: grpc.UnaryUnaryMultiCallable[
        osmosis.twap.v1beta1.query_pb2.ParamsRequest,
        osmosis.twap.v1beta1.query_pb2.ParamsResponse,
    ]
    ArithmeticTwap: grpc.UnaryUnaryMultiCallable[
        osmosis.twap.v1beta1.query_pb2.ArithmeticTwapRequest,
        osmosis.twap.v1beta1.query_pb2.ArithmeticTwapResponse,
    ]
    ArithmeticTwapToNow: grpc.UnaryUnaryMultiCallable[
        osmosis.twap.v1beta1.query_pb2.ArithmeticTwapToNowRequest,
        osmosis.twap.v1beta1.query_pb2.ArithmeticTwapToNowResponse,
    ]
    GeometricTwap: grpc.UnaryUnaryMultiCallable[
        osmosis.twap.v1beta1.query_pb2.GeometricTwapRequest,
        osmosis.twap.v1beta1.query_pb2.GeometricTwapResponse,
    ]
    GeometricTwapToNow: grpc.UnaryUnaryMultiCallable[
        osmosis.twap.v1beta1.query_pb2.GeometricTwapToNowRequest,
        osmosis.twap.v1beta1.query_pb2.GeometricTwapToNowResponse,
    ]

class QueryServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Params(
        self,
        request: osmosis.twap.v1beta1.query_pb2.ParamsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.twap.v1beta1.query_pb2.ParamsResponse: ...
    @abc.abstractmethod
    def ArithmeticTwap(
        self,
        request: osmosis.twap.v1beta1.query_pb2.ArithmeticTwapRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.twap.v1beta1.query_pb2.ArithmeticTwapResponse: ...
    @abc.abstractmethod
    def ArithmeticTwapToNow(
        self,
        request: osmosis.twap.v1beta1.query_pb2.ArithmeticTwapToNowRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.twap.v1beta1.query_pb2.ArithmeticTwapToNowResponse: ...
    @abc.abstractmethod
    def GeometricTwap(
        self,
        request: osmosis.twap.v1beta1.query_pb2.GeometricTwapRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.twap.v1beta1.query_pb2.GeometricTwapResponse: ...
    @abc.abstractmethod
    def GeometricTwapToNow(
        self,
        request: osmosis.twap.v1beta1.query_pb2.GeometricTwapToNowRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.twap.v1beta1.query_pb2.GeometricTwapToNowResponse: ...

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...