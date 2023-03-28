import time
from typing import Optional
from os import getenv
from binance.websocket.spot.websocket_client import SpotWebsocketClient


class TradingClient:
    """
    Binance powered trading client
    """

    binance: SpotWebsocketClient

    def __init__(
        self,
    ):

        self.binance = SpotWebsocketClient()

    @classmethod
    def from_env(cls) -> "TradingClient":
        return cls()

    @classmethod
    def get_env_api_key(cls) -> str:
        res = getenv("BINANCE_API_KEY")

        if not res:
            raise ValueError("BINANCE_API_KEY not set")

        return res

    @classmethod
    def get_env_api_secret(cls) -> str:
        res = getenv("BINANCE_API_SECRET")

        if not res:
            raise ValueError("BINANCE_API_SECRET not set")

        return res
