import sys

try:
    if sys.version_info >= (3, 8):
        from importlib_metadata import version

        __version__ = version(__package__ or __name__)
    else:
        import pkg_resources

        __version__ = pkg_resources.get_distribution(
            __package__ or __name__).version
except BaseException:
    pass

import google.protobuf.message

ProtobufMessage = google.protobuf.message.Message

import osmosispy.exceptions  # noqa
import osmosispy.pytypes  # noqa
from osmosispy.grpc_client import GrpcClient  # noqa
from osmosispy.pytypes import (  # noqa
    Coin,
    Direction,
    Network,
    NetworkType,
    PoolAsset,
    Side,
    TxConfig,
    TxType,
)
from osmosispy.trading_client import TradingClient  # noqa
from osmosispy.sdk import Sdk  # noqa
from osmosispy.tx import Transaction  # noqa
from osmosispy.wallet import Address, PrivateKey, PublicKey  # noqa
