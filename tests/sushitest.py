#!/usr/bin/python3

import pytest
import brownie
from brownie import *

# Define global constants
accounts = brownie.accounts

pool = "0xb223EACc07D4043A14B22b6a3BF9920EF4d3Db67"


@pytest.fixture(scope="module")
def token(SushiToken):
    return SushiToken.deploy({'from': accounts[0], 'gas_price': 1000000000})

@pytest.fixture(scope="module")
def bar(Sushibar, token):
    return Sushibar.deploy(token.address, pool, {'from': accounts[0], 'gas_price': 1000000000})

def test_deployment(token, bar):
    assert token.address != brownie.ZERO_ADDRESS
    assert token.balanceOf(accounts[0]) == 1000*1e18
    assert bar.pool() == pool

def test_enter(token, bar):
    token.approve(bar.address, 10000*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.allowance(accounts[0], bar.address) == 10000*1e18
    bar.enter(100*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    assert bar.balanceOf(accounts[0]) == 100*1e18
    assert bar.deposits(0)[0] == accounts[0]
    assert bar.deposits(0)[2] == 100*1e18


def test_leaveAfter8Days(token, bar):
    chain.snapshot()
    token.approve(bar.address, 10000*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    bar.enter(100*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 900*1e18
    chain.sleep(86400*9)
    bar.leave(100*1e18, 0, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 1000*1e18 
    chain.revert()

def test_leaveIn2Days(token, bar):
    chain.snapshot()
    token.approve(bar.address, 10000*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    bar.enter(100*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 900*1e18
    chain.sleep(86400*2)
    bar.leave(100*1e18, 0, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 900*1e18 
    assert token.balanceOf(pool) == 100*1e18 
    chain.revert()

def test_leaveIn4Days(token, bar):
    chain.snapshot()
    token.approve(bar.address, 10000*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    bar.enter(100*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 900*1e18
    chain.sleep(86400*4)
    bar.leave(100*1e18, 0, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 925*1e18 
    assert token.balanceOf(pool) == 75*1e18 
    chain.revert()

def test_leaveIn6Days(token, bar):
    chain.snapshot()
    token.approve(bar.address, 10000*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    bar.enter(100*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 900*1e18
    chain.sleep(86400*6)
    bar.leave(100*1e18, 0, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 950*1e18 
    assert token.balanceOf(pool) == 50*1e18 
    chain.revert()

def test_leaveIn8Days(token, bar):
    chain.snapshot()
    token.approve(bar.address, 10000*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    bar.enter(100*1e18, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 900*1e18
    chain.sleep(86400*8)
    bar.leave(100*1e18, 0, {'from': accounts[0], 'gas_price': 1000000000})
    assert token.balanceOf(accounts[0]) == 975*1e18 
    assert token.balanceOf(pool) == 25*1e18 
    chain.revert()