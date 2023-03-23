"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import osmosis.gamm.v1beta1.tx_pb2

class MsgStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    JoinPool: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgJoinPool,
        osmosis.gamm.v1beta1.tx_pb2.MsgJoinPoolResponse,
    ]
    ExitPool: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgExitPool,
        osmosis.gamm.v1beta1.tx_pb2.MsgExitPoolResponse,
    ]
    SwapExactAmountIn: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountIn,
        osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountInResponse,
    ]
    SwapExactAmountOut: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountOut,
        osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountOutResponse,
    ]
    JoinSwapExternAmountIn: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapExternAmountIn,
        osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapExternAmountInResponse,
    ]
    JoinSwapShareAmountOut: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapShareAmountOut,
        osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapShareAmountOutResponse,
    ]
    ExitSwapExternAmountOut: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapExternAmountOut,
        osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapExternAmountOutResponse,
    ]
    ExitSwapShareAmountIn: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapShareAmountIn,
        osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapShareAmountInResponse,
    ]

class MsgServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def JoinPool(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgJoinPool,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgJoinPoolResponse: ...
    @abc.abstractmethod
    def ExitPool(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgExitPool,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgExitPoolResponse: ...
    @abc.abstractmethod
    def SwapExactAmountIn(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountIn,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountInResponse: ...
    @abc.abstractmethod
    def SwapExactAmountOut(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountOut,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgSwapExactAmountOutResponse: ...
    @abc.abstractmethod
    def JoinSwapExternAmountIn(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapExternAmountIn,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapExternAmountInResponse: ...
    @abc.abstractmethod
    def JoinSwapShareAmountOut(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapShareAmountOut,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgJoinSwapShareAmountOutResponse: ...
    @abc.abstractmethod
    def ExitSwapExternAmountOut(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapExternAmountOut,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapExternAmountOutResponse: ...
    @abc.abstractmethod
    def ExitSwapShareAmountIn(
        self,
        request: osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapShareAmountIn,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.tx_pb2.MsgExitSwapShareAmountInResponse: ...

def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...