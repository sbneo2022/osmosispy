"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import osmosis.lockup.tx_pb2

class MsgStub:
    """Msg defines the Msg service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    LockTokens: grpc.UnaryUnaryMultiCallable[
        osmosis.lockup.tx_pb2.MsgLockTokens,
        osmosis.lockup.tx_pb2.MsgLockTokensResponse,
    ]
    """LockTokens lock tokens"""
    BeginUnlockingAll: grpc.UnaryUnaryMultiCallable[
        osmosis.lockup.tx_pb2.MsgBeginUnlockingAll,
        osmosis.lockup.tx_pb2.MsgBeginUnlockingAllResponse,
    ]
    """BeginUnlockingAll begin unlocking all tokens"""
    BeginUnlocking: grpc.UnaryUnaryMultiCallable[
        osmosis.lockup.tx_pb2.MsgBeginUnlocking,
        osmosis.lockup.tx_pb2.MsgBeginUnlockingResponse,
    ]
    """MsgBeginUnlocking begins unlocking tokens by lock ID"""
    ExtendLockup: grpc.UnaryUnaryMultiCallable[
        osmosis.lockup.tx_pb2.MsgExtendLockup,
        osmosis.lockup.tx_pb2.MsgExtendLockupResponse,
    ]
    """MsgEditLockup edits the existing lockups by lock ID"""
    ForceUnlock: grpc.UnaryUnaryMultiCallable[
        osmosis.lockup.tx_pb2.MsgForceUnlock,
        osmosis.lockup.tx_pb2.MsgForceUnlockResponse,
    ]

class MsgServicer(metaclass=abc.ABCMeta):
    """Msg defines the Msg service."""

    @abc.abstractmethod
    def LockTokens(
        self,
        request: osmosis.lockup.tx_pb2.MsgLockTokens,
        context: grpc.ServicerContext,
    ) -> osmosis.lockup.tx_pb2.MsgLockTokensResponse:
        """LockTokens lock tokens"""
    @abc.abstractmethod
    def BeginUnlockingAll(
        self,
        request: osmosis.lockup.tx_pb2.MsgBeginUnlockingAll,
        context: grpc.ServicerContext,
    ) -> osmosis.lockup.tx_pb2.MsgBeginUnlockingAllResponse:
        """BeginUnlockingAll begin unlocking all tokens"""
    @abc.abstractmethod
    def BeginUnlocking(
        self,
        request: osmosis.lockup.tx_pb2.MsgBeginUnlocking,
        context: grpc.ServicerContext,
    ) -> osmosis.lockup.tx_pb2.MsgBeginUnlockingResponse:
        """MsgBeginUnlocking begins unlocking tokens by lock ID"""
    @abc.abstractmethod
    def ExtendLockup(
        self,
        request: osmosis.lockup.tx_pb2.MsgExtendLockup,
        context: grpc.ServicerContext,
    ) -> osmosis.lockup.tx_pb2.MsgExtendLockupResponse:
        """MsgEditLockup edits the existing lockups by lock ID"""
    @abc.abstractmethod
    def ForceUnlock(
        self,
        request: osmosis.lockup.tx_pb2.MsgForceUnlock,
        context: grpc.ServicerContext,
    ) -> osmosis.lockup.tx_pb2.MsgForceUnlockResponse: ...

def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
