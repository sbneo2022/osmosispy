from typing import Callable, Optional
from os import getenv
from binance.websocket.spot.websocket_client import SpotWebsocketClient
from binance.spot import Spot

from .trade_data import TradeData
from .types import TradingFee
from .client import ITradingClient
from osmosispy import Coin


class BinanceClient(ITradingClient):
    """
    Binance trading client
    """

    ws_client: SpotWebsocketClient
    api_client: Spot
    last_id = 0

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
    def from_env(cls) -> "BinanceClient":
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
        except (NameError, AttributeError, IndexError):
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

    def listen_trades(self, cb: Callable[[TradeData], None], symbol: str = "USDT"):
        self.ws_client.start()

        id = self.last_id
        self.last_id += 1

        def callback(data):
            # check if the event is an aggTrade
            try:
                if data["e"] != "aggTrade":
                    return
            except KeyError as e:
                return

            # call the actual callback
            cb(TradeData(
                price=Coin(denom=symbol, amount=data["p"]),
                quantity=Coin(denom="OSMO", amount=data["q"]),
            ))

        self.ws_client.agg_trade(
            id=id,
            symbol="OSMO" + symbol,
            callback=callback,
        )

    def stop_ws(self) -> None:
        self.ws_client.stop()
