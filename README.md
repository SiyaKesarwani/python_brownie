# sushibarcontract-extendedfeature

```
Fork SushiSwap’s SushiBar contract and implement following featuresStaking:
Time lock after staking:
2 days - 0% can be unstaked
2-4 days - 25% can be unstaked
4-6 days - 50% can be unstaked
6-8 days - 75% can be unstaked
After 8 days - 100% can be unstaked.This will work like a high tax though.
0-2 days - locked
2-4 days - 75% tax
4-6 days - 50% tax
6-8 days - 25% tax
After 8 days, 0% tax.
The tokens received on tax will go back into rewards pool.
```

For [Vyper](https://github.com/vyperlang/vyper), check out [`vyper-token-mix`](https://github.com/brownie-mix/vyper-token-mix).

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. Download the mix.

    ```bash
    brownie bake token
    ```

## Basic Use

This project contains two main contracts : 1st is SushiToken and the other is Sushibar.

SushiToken is used to deploy our own ERC20 Sushi token.
Sushibar is using the Sushibar contract but with some extended features mentioned above.

To interact with a deployed contract in a local environment, start by opening the console:

```bash
brownie console
```

## Testing

To run the tests:

```bash
brownie test
```

The unit tests included in this mix are very generic and should work with any ERC20 compliant smart contract. 

## Resources

To get started with Brownie:

* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).
