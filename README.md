# Osmosis python SDK

<!-- Python-based client for interacting with the Osmosis AMM. -->

Python SDK for interacting with the Osmosis AMM.

<!-- TODO add badges -->
<!-- Badges -->

[![MIT license][license-badge]][license-link]

<!-- Badges links -->

[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://github.com/sbneo2022/osmosispy/blob/master/LICENSE

The `osmosispy` and `osmosis_proto` package allows you to interact with the Osmosis AMM using Python.

#### README Contents

- [Python SDK Tutorial](#python-sdk-tutorial)
- [Installation from `PyPI`](#installation-from-pypi)
- [Usage](#usage)
  - [Ex: Creating a wallet and SDK client](#ex-creating-a-wallet-and-sdk-client)
- [Publishing to PyPI](#publishing-to-pypi)
- [Documentation Website](#documentation-website)

## Installation from `PyPI`

```bash
python -m pip install --upgrade pip

pip install osmosispy  # requires Python 3.11.2+
```

## Usage

### Ex: Creating a wallet and SDK client

```python
import osmosispy

mnemonic = "lorem ipsum dolor sit amet ..."

network = osmosispy.network.Network.localnet()
sdk = osmosispy.Sdk.authorize(mnemonic)
  .with_network(network)
```

The `Sdk` class creates an interface to sign and send transactions or execute queries.

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

## Documentation Website

Documentation can be found [here](https://example.com) (**NOT IMPLEMENTED YET**)
