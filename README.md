# Osmosis python SDK

<!-- Python-based client for interacting with the Osmosis AMM. -->

Python SDK for interacting with the Osmosis AMM.

<!-- Badges -->

[![Project Status: WIP -- Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://img.shields.io/badge/repo%20status-WIP-yellow.svg)](https://www.repostatus.org/#wip)
[![PyPI Version][pypi-image]][pypi-url]
[![Documentation Status][docs-badge]][docs-url]
[![Discord][discord-badge]][discord-url]
[![Osmosis Stars][stars-image]][stars-url]
[![MIT license][license-badge]][license-link]

<!-- Badges links -->

[docs-badge]: https://img.shields.io/badge/docs-passing-green.svg
[docs-url]: https://docs.osmosis.zone/
[discord-badge]: https://dcbadge.vercel.app/api/server/osmosis?style=flat
[discord-url]: https://discord.gg/osmosis
[stars-image]: https://img.shields.io/github/stars/osmosis-labs?style=social
[stars-url]: https://github.com/osmosis-labs
[pypi-image]: https://img.shields.io/pypi/v/osmosispy
[pypi-url]: https://pypi.org/project/osmosispy/
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://github.com/sbneo2022/osmosispy/blob/master/LICENSE

The `osmosispy` and `osmosis_proto` package allows you to interact with the Osmosis AMM using Python.

#### README Contents

- [Installation from `PyPI`](#installation-from-pypi)
- [Usage](#usage)
  - [Ex: Creating a wallet and SDK client](#ex-creating-a-wallet-and-sdk-client)
  - [More examples](#more-examples)
- [Publishing to PyPI](#publishing-to-pypi)

## Installation from `PyPI`

```bash
python -m pip install --upgrade pip

pip install osmosispy  # requires Python 3.11.2+
```

## Usage

### Ex: Creating a wallet and SDK client

**example.py**

```python
#!/usr/bin/env python3

import osmosispy

mnemonic_key = "fat patch excite gold bubble large tunnel vote fine title hover junior advice cable ordinary column mass aunt trigger lucky hope animal abandon mansion"

# authorize in the mainnet
network = osmosispy.Network.mainnet()

trader = osmosispy.Sdk.authorize(key=mnemonic_key).with_network(network)

# print the address
print(trader.address)
```

```console
$ python3 example.py
osmo1jggt8pcj2d8m9n62luytf8sdncj5uxfs3su2my
```

### More examples

For more examples see the [examples directory](/examples).

- [connection and base methods](/examples/connect.ipynb)
- [trading client](/examples/trading_client.ipynb)

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
   git tag -asm "v1.2.3" v1.2.3
   git push --tags
   ```

4. The tag will trigger a [GitHub Action Workflow](https://github.com/sbneo2022/osmosispy/actions/workflows/publish.yml).
