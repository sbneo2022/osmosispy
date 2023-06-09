"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import osmosis.downtime_detector.v1beta1.query_pb2

class QueryStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    RecoveredSinceDowntimeOfLength: grpc.UnaryUnaryMultiCallable[
        osmosis.downtime_detector.v1beta1.query_pb2.RecoveredSinceDowntimeOfLengthRequest,
        osmosis.downtime_detector.v1beta1.query_pb2.RecoveredSinceDowntimeOfLengthResponse,
    ]

class QueryServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def RecoveredSinceDowntimeOfLength(
        self,
        request: osmosis.downtime_detector.v1beta1.query_pb2.RecoveredSinceDowntimeOfLengthRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.downtime_detector.v1beta1.query_pb2.RecoveredSinceDowntimeOfLengthResponse: ...

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
