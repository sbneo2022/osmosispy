from typing import Callable, Optional
from .client import ITradingClient
from .trade_data import TradeData
from .types import TradingFee
from osmosispy import Coin


class OsmosisTradingClient(ITradingClient):
    def get_trading_fee(self, symbol: str = "OSMOUSDT") -> Optional[TradingFee]:
        raise NotImplementedError

    def get_price(self, symbol: str = "OSMOUSDT") -> Coin:
        raise NotImplementedError

    def listen_trades(self, cb: Callable[[TradeData], None], symbol: str = "OSMOUSDT"):
        raise NotImplementedError

    def stop_listeners(self) -> None:
        raise NotImplementedError
