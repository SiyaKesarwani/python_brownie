#!/usr/bin/python3

import brownie
from brownie import SushiToken, Sushibar


accounts = brownie.accounts
pool = "0xb223EACc07D4043A14B22b6a3BF9920EF4d3Db67"


def main():
    token = SushiToken.deploy({'from': accounts[0], 'gas_price': 1000000000})
    sushibar = Sushibar.deploy(token.address, pool, {'from': accounts[0], 'gas_price': 1000000000})

