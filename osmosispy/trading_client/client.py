import time
from typing import Optional
from os import getenv
from binance.websocket.spot.websocket_client import SpotWebsocketClient
from binance.spot import Spot
from .types import TradingFee
from osmosispy import Coin


class TradingClient:
    """
    Binance powered trading client
    """

    ws_client: SpotWebsocketClient
    api_client: Spot

    def __init__(
        self,
        api_key: str,
        api_secret: str,
    ):
        self.api_client = Spot(
            api_key=api_key,
            api_secret=api_secret,
        )

        self.ws_client = SpotWebsocketClient()

    @classmethod
    def _get_env_api_key(cls) -> str:
        res = getenv("BINANCE_API_KEY")

        if not res:
            raise ValueError("BINANCE_API_KEY not set")

        return res

    @classmethod
    def _get_env_api_secret(cls) -> str:
        res = getenv("BINANCE_API_SECRET")

        if not res:
            raise ValueError("BINANCE_API_SECRET not set")

        return res

    @classmethod
    def from_env(cls) -> "TradingClient":
        """
        Provides a convenient way to create a `TradingClient` instance without having to pass
        the api key and secret manually.

        Make sure to set the `BINANCE_API_KEY` and `BINANCE_API_SECRET` environment variables.

        ```bash
        export BINANCE_API_KEY=your_api_key
        export BINANCE_API_SECRET=your_api_secret
        ```

        Returns:
            TradingClient: The `TradingClient` instance
        """
        return cls(
            api_key=cls._get_env_api_key(),
            api_secret=cls._get_env_api_secret(),
        )

    def get_trading_fee(self, symbol: str = "USDT") -> Optional[TradingFee]:
        """
        Get the current trading fee for OSMO + `symbol` pair

        Args:
            symbol (str, optional): The symbol to get the trading fee for. Defaults to "USDT".

        Returns:
            Optional[TradingFee]: The trading fee for the pair. None if the there is no trades or fee info for the pair.
        """
        res = self.api_client.trade_fee(symbol="OSMO"+symbol)
        try:
            fees = res[0]
            return TradingFee(
                maker_commision=float(fees["makerCommission"]),
                taker_commision=float(fees["takerCommission"]),
            )
        except (NameError, AttributeError, IndexError) as _:
            return None

    def get_price(self, price_in_symbol: str = "USDT") -> Coin:
        """
        Get the current price of OSMO in `price_in_symbol` (e.g. "OSMOUSDT" pair)

        Args:
            price_in_symbol (str, optional): The symbol to get the price in. Defaults to "USDT".

        Returns:
            Coin: The price of OSMO in `price_in_symbol`
        """
        res = self.api_client.ticker_price(symbol="OSMO" + price_in_symbol)

        return Coin(denom=price_in_symbol, amount=res["price"])

    def start_ws(self):
        """
        Start the websocket client

        Call this method before using any of the websocket methods
        """
        self.ws_client.start()

    def stop_ws(self):
        """
        Stop the websocket client

        Call this method when you are done using the websocket methods
        """
        self.ws_client.stop()
