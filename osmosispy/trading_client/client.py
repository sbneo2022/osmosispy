from typing import Callable, Optional
from osmosispy.trading_client.trade_data import TradeData
from .types import TradingFee
from osmosispy import Coin


class ITradingClient:
    """
    Interface for trading clients
    """

    def get_trading_fee(self, symbol: str = "USDT") -> Optional[TradingFee]:
        """
        Get the current trading fee for OSMO + `symbol` pair

        Args:
            symbol (str, optional): The symbol to get the trading fee for. Defaults to "USDT".

        Returns:
            Optional[TradingFee]: The trading fee for the pair. None if the there is no trades or fee info for the pair.
        """
        raise NotImplementedError

    def get_price(self, price_in_symbol: str = "USDT") -> Coin:
        """
        Get the current price of OSMO in `price_in_symbol` (e.g. "OSMOUSDT" pair)

        Args:
            price_in_symbol (str, optional): The symbol to get the price in. Defaults to "USDT".

        Returns:
            Coin: The price of OSMO in `price_in_symbol`
        """
        raise NotImplementedError

    def listen_trades(self, cb: Callable[[TradeData], None], symbol: str = "USDT"):
        """
        Listen to the price of OSMO in `price_in_symbol` (e.g. "OSMOUSDT" pair)

        Args:
            price_in_symbol (str, optional): The symbol to get the price in. Defaults to "USDT".

        Example:
        ```
        # Listen to trades for 60 seconds
        def cb(trade_data: TradeData):
            print(trade_data)

        cancel = client.start_ws(cb)

        sleep(60)

        cancel()
        """
        raise NotImplementedError

    def stop_ws(self) -> None:
        """
        Stops all listeners
        """
        raise NotImplementedError
