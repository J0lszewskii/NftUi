#Work in progress here, the textural ui in ui.py is finished and is subject of the review for the arcade
import streamlit as st

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


