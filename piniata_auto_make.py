import os
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware, geth_poa_middleware
from getabi import getabi



def mint_on_contract(w3, ipfs_hash, to_account, contract_address, token_id, gas_price='45', private_key=os.environ.get("PRIVATE_KEY")):
    abi_dict = getabi()

    contract = w3.eth.contract(address=contract_address, abi=getabi())
    tx = contract.functions._safeMint(
        to_account,
        token_id,
        "ipfs://" + ipfs_hash,
    ).build_transaction({
        'from': to_account,
        'nonce': w3.eth.get_transaction_count(to_account),
        'gas': 200000,
        'gasPrice': w3.to_wei(gas_price, 'gwei')
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt


if __name__ == "__main__":
    ipfs_hash = "QmXLQfn7ozmVfHvgZ7wTHeNeB9BAtmvMQCXesVatfioQfC"
    to_account = '0x9Bb1211E790013227703BbBAb11cd8A08e62b6dc'
    contract_address = "0xf3C5d6ea982836b431478198E54A682D04891e49"
    token_id = 1000
    w3 = Web3(Web3.HTTPProvider('https://rpc-amoy.polygon.technology/'))
    print(mint_on_contract(w3, ipfs_hash, to_account, contract_address, token_id))
