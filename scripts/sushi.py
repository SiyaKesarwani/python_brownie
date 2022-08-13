#!/usr/bin/python3

from brownie import SushiToken, Sushibar, accounts


def main():
    return SushiToken.deploy({'from': accounts[0], 'gas_limit': 100000000})


