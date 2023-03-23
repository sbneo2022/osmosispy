# Osmosis python SDK

<!-- Python-based client for interacting with the Osmosis AMM. -->

Python SDK for interacting with the Osmosis AMM.

<!-- TODO add badges -->
<!-- Badges -->

[![MIT license][license-badge]][license-link]

<!-- Badges links -->

[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://github.com/chadury2021/osmosis-pysdk/blob/master/LICENSE

The `osmosis` package allows you to index, query, and send transactions on Cosmos chain using Python. It provides access to market data for analysis, visualization, indicator development, algorithmic trading, strategy backtesting, bot programming, and related software engineering.

The package is intended to be used by coders, developers, technically-skilled traders and data-scientists for building trading algorithms.

#### README Contents

- [Python SDK Tutorial](#python-sdk-tutorial)
- [Installation from `PyPI`](#installation-from-pypi)
- [Usage](#usage)
  - [Ex: Creating a wallet and SDK client](#ex-creating-a-wallet-and-sdk-client)
  - [Ex: Querying chain state](#ex-querying-chain-state)
  - [Ex: Submitting transactions](#ex-submitting-transactions)
- [Documentation Website](#documentation-website)

## Installation from `PyPI`

<!-- TODO: register on PyPI -->

**NOT IMPLEMENTED YET**

```bash
pip install osmosispy  # requires Python 3.10+
```

You may need to update `pip` to get this to run:

```bash
python -m pip install --upgrade pip
```

## Usage

### Ex: Creating a wallet and SDK client

**NOT IMPLEMENTED YET**

```python
from osmosispy import wallet

# Save the mnemonic for later
mnemonic, private_key = wallet.PrivateKey.generate()
```

After, creating an account, you can create an `Sdk` instance.

```python
import osmosispy

network = osmosispy.network.Network.testnet(2)
sdk = osmosispy.Sdk.authorize(mnemonic)
  .with_network(network)
```

The `Sdk` class creates an interface to sign and send transactions or execute
queries. It is associated with:

- A transaction signer (wallet), which is configured from existing mnemonic to recover a `PrivateKey`.
- A `Network`, which specifies the RPC, LCD, and gRPC endpoints for connecting to Cosmos chain.
- An optional `TxConfig` for changing gas parameters.

### Ex: Querying chain state

**NOT IMPLEMENTED YET**

```python
# Querying the token balances of the account
sdk.query.get_bank_balances(sdk.address)

# Querying from the vpool module
query_resp = sdk.query.vpool.all_pools()
print(query_resp)
# Queries from other modules can be accessed from "sdk.query.module"
```

### Ex: Submitting transactions

**NOT IMPLEMENTED YET**

```python
from osmosispy import OpenPositionMsg

tx_resp = sdk.tx.execute_msgs(
    OpenPositionMsg(
        sender=sdk.address,
        pair="ubtc:unusd",
        is_long=True,
        quote_asset_amount=10,
        leverage=10,
        base_asset_amount_limit=0,
    )
)
```

You can broadcast any available transaction by messages that inherits `Message` to the `sdk.tx.execute_msgs` function.

## Publishing to PyPI

The publish workflow looks like this:

1. Code-gen the new types from the chain. If there are changes, these should be committed.

   ```sh
   poetry run make proto-gen
   ```

2. Increment the package version. For example, use `poetry version preminor` to do a pre-release for a minor version.

   ```sh
   poetry version [update-keyword]
   ```

3. Create a tag and push it the remote origin.

   ```sh
   git tag -asm "v15.0.0" v15.0.0
   git push --tags
   ```

4. The tag should trigger a [GitHub Action Workflow](https://github.com/chadury2021/osmosis-pysdk/actions/workflows/publish-to-pypi.yml). **NOT IMPLEMENTED YET**

## Documentation Website

Documentation can be found [here](https://example.com) (**NOT IMPLEMENTED YET**)
