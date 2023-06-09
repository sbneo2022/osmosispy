"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import osmosis.gamm.pool_models.stableswap.tx_pb2

class MsgStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateStableswapPool: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.pool_models.stableswap.tx_pb2.MsgCreateStableswapPool,
        osmosis.gamm.pool_models.stableswap.tx_pb2.MsgCreateStableswapPoolResponse,
    ]
    StableSwapAdjustScalingFactors: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.pool_models.stableswap.tx_pb2.MsgStableSwapAdjustScalingFactors,
        osmosis.gamm.pool_models.stableswap.tx_pb2.MsgStableSwapAdjustScalingFactorsResponse,
    ]

class MsgServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateStableswapPool(
        self,
        request: osmosis.gamm.pool_models.stableswap.tx_pb2.MsgCreateStableswapPool,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.pool_models.stableswap.tx_pb2.MsgCreateStableswapPoolResponse: ...
    @abc.abstractmethod
    def StableSwapAdjustScalingFactors(
        self,
        request: osmosis.gamm.pool_models.stableswap.tx_pb2.MsgStableSwapAdjustScalingFactors,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.pool_models.stableswap.tx_pb2.MsgStableSwapAdjustScalingFactorsResponse: ...

def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
