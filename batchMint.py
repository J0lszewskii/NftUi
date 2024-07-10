from ipfs import upload_to_ipfs
from getabi import getabi
from mint_on_contract import mint_on_contract
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware, geth_poa_middleware
from pinata import Pinata
import os
import json

def getIPFSclient(path_to_folder):
    # get all files in the folder
    files = os.listdir(path_to_folder)
    file = files[-1]
    # get the file
    with open(f"{path_to_folder}/{file}", "r") as f:
        data = f.read()
    #split the data by new line
    data = data.split("\n")
    api_key = data[0].split(" ")[-1]
    api_secret = data[1].split(" ")[-1]
    secret_access_token = data[2].split(" ")[-1]

    return Pinata(api_key, api_secret, secret_access_token)

def upload_to_ipfs(client, file):
    response = client.pin_file(file)
    if response['status'] == "success":
        return response['data']['IpfsHash']
    else:
        print(response)
        return None

def get_metadata(ipfs_hash, token_id, collection_name, collection_description):
    return {
        "name": collection_name+" #"+str(token_id),
        "description": collection_description,
        "image": f"ipfs://{ipfs_hash}"
    }

def mint(file, ipfs_client, collection_name, collection_description, contract_address, w3, to_address):
    token_id = int(file.split(".")[0])
    image_hash = upload_to_ipfs(ipfs_client, "images/"+file)
    metadata = get_metadata(image_hash, token_id, collection_name, collection_description)
    with open("metadata.json", "w") as f:
        json.dump(metadata, f)

    metadata_hash = upload_to_ipfs(ipfs_client, "metadata.json")
    abi = getabi()
    return mint_on_contract(w3, metadata_hash, to_address, contract_address, token_id)


def mint_directory(directory, ipfs_client, collection_name, collection_description, contract_address, w3, to_address):
    files = os.listdir(directory)
    for file in files:
        reciept = mint(file, ipfs_client, collection_name, collection_description, contract_address, w3, to_address)
        print(f"minted {file}")
        reciepts = []
        reciepts.append(reciept)
    return reciepts



if __name__ == "__main__":
    ipfs_client = getIPFSclient("api_keys")
    w3 = Web3(Web3.HTTPProvider('https://rpc-amoy.polygon.technology/'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    mint_directory("images", ipfs_client, "Test Collection", "This is a test collection", "0xf3C5d6ea982836b431478198E54A682D04891e49", w3, "0x9Bb1211E790013227703BbBAb11cd8A08e62b6dc")
