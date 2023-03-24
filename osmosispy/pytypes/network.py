"""
The network class allows the user to defines the network the sdk interface should connect to.

There are some default values set for devnet, testnet, mainet and localnet, but the user cna also define its own
network by setting the values of the Network data class.

"""
import dataclasses
import enum
import os
from typing import Dict, List, Optional


@dataclasses.dataclass
class Network:
    lcd_endpoint: str
    grpc_endpoint: str
    tendermint_rpc_endpoint: str
    chain_id: str
    websocket_endpoint: str
    env: str = "custom"
    fee_denom: str = "uosmo"

    @property
    def is_insecure(self) -> bool:
        return not ("https" in self.tendermint_rpc_endpoint)

    @classmethod
    def testnet(cls, chain_num: int = 4) -> "Network":
        """
        Testnet is a network open to invited validators. It is more stable than
        devnet and provides a faucet to get some funds

        Args:
          chain_num (int): Testnet number

        Returns:
            Network: The updated Network object.
        """
        return cls(
            lcd_endpoint=f'https://lcd.testnet-{chain_num}.osmosis.zone ',
            grpc_endpoint=f'tcp://grpc.testnet-{chain_num}.osmosis.zone :443',
            tendermint_rpc_endpoint=f'https://rpc.testnet-{chain_num}.osmosis.zone ',
            websocket_endpoint=f'wss://rpc.testnet-{chain_num}.osmosis.zone /websocket',
            chain_id=f'osmo-test-{chain_num}',
            fee_denom='uosmo',
            env='testnet',
        )

    @classmethod
    def mainnet(cls) -> "Network":
        """
        **NOT IMPLEMENTED YET**
        """
        raise NotImplementedError

    @classmethod
    def localnet(cls) -> "Network":
        """
        Localnet is the network you would expect to connect to if you run `make localnet` from the osmosis repository.
        It allows you to update locally the golang codebase to checkout the behavior of the chain with different changes
        applied.

        Returns:
            Network: The updated Network object.
        """
        return cls(
            lcd_endpoint='http://localhost:1317',
            grpc_endpoint='localhost:9090',
            tendermint_rpc_endpoint='http://localhost:26657',
            websocket_endpoint='ws://localhost:26657/websocket',
            chain_id='osmo-local-0',
            fee_denom='uosmo',
            env='local',
        )

    def string(self) -> str:
        """
        Returns the current environment the network was initialized with. Will return `custom` if a custom network
        was created

        Returns:
            str: The name of the current environment.
        """
        return self.env


class NetworkType(enum.Enum):
    """Enum class for the available network types. E.g. 'testnet' and 'devnet'."""

    DEVNET = "devnet"
    TESTNET = "testnet"
    LOCALNET = "localnet"
