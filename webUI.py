#Work in progress here, the textural ui in ui.py is finished and is subject of the review for the arcade
import streamlit as st
from batchMint import mint_directory, getIPFSclient
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware, geth_poa_middleware

st.title("Mintowanie wielu NFT naraz webUI")

st.write("Podaj adres portfela")
wallet_address = st.text_input("Adres portfela")
st.write("Podaj klucz prywatny")
private_key = st.text_input("Klucz prywatny")
st.write("Podaj nazwę folderu")
folder_name = st.text_input("Nazwa folderu")
st.write("Podaj nazwę kolekcji")
collection_name = st.text_input("Nazwa kolekcji")
st.write("Podaj opis kolekcji")
collection_description = st.text_input("Opis kolekcji")
st.write("Podaj adres kontraktu")
contract_address = st.text_input("Adres kontraktu")

confirm = st.button("Potwierdź")

ipfs_client = getIPFSclient("api_keys")
w3 = Web3(Web3.HTTPProvider('https://rpc-amoy.polygon.technology/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
x = mint_directory(folder_name, ipfs_client, collection_name, collection_description, contract_address, w3, wallet_address)
if x != []:
    st.write("Mintowanie zakończone")
    st.toast("Mintowanie zakończone")
    st.write(x)