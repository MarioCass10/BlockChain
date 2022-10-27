from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'Kz9PPTCxqkvMXtf51t3u88ueGGU7UGZbfNXHHeuZ2d9vd9fWGkTD')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'L3sB23pe1Gmq3RULvHGsQbeVRz1mignarYmdabFFaB2nVPtm1Zt7')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'KysibXCzvR8Yy2t31sVFP3KvqjqdBzAyFJdeeyTQKh79dSueHdEx')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        OP_2, cust1_public_key, cust2_public_key,cust3_public_key, my_public_key, OP_4, OP_EQUALVERIFY# fill this in!
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00103403 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'ce51d2ca0a5d1d22e81aa9f6c569dc5ae755dc548528492472d3a278b53d7e20')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
