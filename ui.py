from textual.app import App
from textual.widgets import Button, Label, Input, Header
from textual.containers import Vertical, Horizontal
from batchMint import mint_directory, getIPFSclient
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware, geth_poa_middleware

class MyApp(App):
    CSS_PATH = "list_view.tcss"

    def compose(self):
        yield Header()
        self.address_input_field = Input(name="address", id="address")
        self.private_key_input_field = Input(name="private_key", id="private_key")

        self.a1h =  Horizontal(
            Label("Podaj address"),
            self.address_input_field,
            Button("Wprowadź", name="submit_address", id="submit_address"),
            classes="entry",
        )
        yield self.a1h


        self.pkh = Horizontal(
            Label("Podaj klucz prywatny"),
            self.private_key_input_field,
            Button("Wprowadź", name="submit_private_key", id="submit_private_key"),
            classes="entry",
        )
        yield self.pkh

        self.folder_name_input_field = Input(name="folder_name", id="folder_name")

        self.fnh = Horizontal(
            Label("Podaj nazwę folderu"),
            self.folder_name_input_field,
            Button("Wprowadź", name="submit_folder_name", id="submit_folder_name"),
            classes="entry",
        )
        yield self.fnh

        self.collection_name_input_field = Input(name="col_name", id="col_name")

        self.cnh =  Horizontal(
            Label("Podaj nazwę kolekcji"),
            self.collection_name_input_field,
            Button("Wprowadź", name="submit_col_name", id="submit_col_name"),
            classes="entry",
        )
        yield self.cnh

        self.col_desc_input_field = Input(name="col_desc", id="col_desc")

        self.cdh = Horizontal(
            Label("Podaj opis kolekcji"),
            self.col_desc_input_field,
            Button("Wprowadź", name="submit_col_desc", id='submit_col_desc'),
            classes="entry",
        )
        yield self.cdh
        self.cadress_input_field = Input(name="caddress", id="caddress")
        self.cadh = Horizontal(
            Label("Podaj adres kontraktu"),
            self.cadress_input_field,
            Button("Wprowadź", name="submit_caddress", id="submit_caddress"),
            classes="entry",
        )
        yield self.cadh

        


        self.label = Label("Wprowadź adres portfela")
        self.label2 = Label("Wprowadź klucz prywatny")
        self.label3 = Label("Wprowadź nazwę folderu")
        self.label4 = Label("Wprowadź nazwę kolekcji")
        self.label5 = Label("Wprowadź opis kolekcji")
        self.label6 = Label("Wprowadź adres kontraktu")
        yield self.label
        yield self.label2
        yield self.label3
        yield self.label4
        yield self.label5
        yield self.label6

        self.confirm_button = Button("Potwierdź", name="confirm", id="confirm")
        yield self.confirm_button

    def on_mount(self):
        self.title = "Mintowanie wielu NFT naraz"
        self.sum = 0
        self.confirm_button.visible = False
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit_address":
            self.address = self.address_input_field.value
            self.label.update(f"Adres portfela: {self.address}")
            self.address_input_field.disabled = True
            self.a1h.remove()
            self.sum += 1
        if event.button.id == "submit_private_key":
            self.private_key = self.private_key_input_field.value
            self.private_key_input_field.disabled = True
            self.label2.update(f"Klucz prywatny: {self.private_key}")
            self.pkh.remove()
            self.sum += 1
        if event.button.id == "submit_folder_name":
            self.folder_name = self.folder_name_input_field.value
            self.folder_name_input_field.disabled = True
            self.label3.update(f"Folder: {self.folder_name}")
            self.fnh.remove()
            self.sum += 1
        if event.button.id == "submit_col_name":
            self.col_name = self.collection_name_input_field.value
            self.collection_name_input_field.disabled = True
            self.label4.update(f"Nazwa kolekcji: {self.col_name}")
            self.cnh.remove()
            self.sum += 1
        if event.button.id == 'submit_col_desc':
            self.col_desc = self.col_desc_input_field.value
            self.col_desc_input_field.disabled = True
            self.label5.update(f"Opis kolekcji: {self.col_desc}")
            self.cdh.remove()
            self.sum += 1
        if event.button.id == "submit_caddress":
            self.caddress = self.cadress_input_field.value
            self.cadress_input_field.disabled = True
            self.label6.update(f"Adres kontraktu: {self.caddress}")
            self.cadh.remove()
            self.sum += 1
        
        if event.button.id == 'confirm':
            self.label.remove()
            self.label2.remove()
            self.label3.remove()
            self.label4.remove()
            self.label5.remove()
            self.confirm_button.remove()
            self.title = "Mintowanie NFT"
            ipfs_client = getIPFSclient("api_keys")
            w3 = Web3(Web3.HTTPProvider('https://rpc-amoy.polygon.technology/'))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            mint_directory(self.folder_name, ipfs_client, self.col_name, self.col_desc, self.caddress, w3, self.address)

            

        
        if self.sum == 6:
            self.confirm_button.visible = True
MyApp().run()
