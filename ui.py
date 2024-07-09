from textual.app import App
from textual.widgets import Button, Label, Input, Header
from textual.containers import Vertical, Horizontal


class MyApp(App):
    CSS_PATH = "list_view.tcss"

    def compose(self):
        yield Header()
        self.address_input_field = Input(name="address", id="address")
        self.private_key_input_field = Input(name="private_key", id="private_key")
        yield Horizontal(
            Label("Podaj address"),
            self.address_input_field,
            Button("Wprowadź", name="submit_address", id="submit_address"),
            classes="entry"
        )
        yield Horizontal(
            Label("Podaj klucz prywatny"),
            self.private_key_input_field,
            Button("Wprowadź", name="submit_private_key", id="submit_private_key"),
            classes="entry"
        )

        self.folder_name_input_field = Input(name="folder_name", id="folder_name")



        yield Horizontal(
            Label("Podaj nazwę folderu"),
            self.folder_name_input_field,
            Button("Wprowadź", name="submit_folder_name", id="submit_folder_name"),
            classes="entry"
        )


        self.collection_name_input_field = Input(name="col_name", id="col_name")

        yield Horizontal(
            Label("Podaj nazwę kolekcji"),
            self.collection_name_input_field,
            Button("Wprowadź", name="submit_col_name", id="submit_col_name"),
            classes='entry'

        )

        self.label = Label("Wprowadź adres kontraktu")
        self.label2 = Label("Wprowadź klucz prywatny")
        self.label3 = Label("Wprowadź nazwę folderu")
        self.label4 = Label("Wprowadź nazwę kolekcji")
        yield self.label
        yield self.label2
        yield self.label3
        yield self.label4

    def on_mount(self):
        self.title = "Mintowanie wielu NFT naraz"
    

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "submit_address":
            self.address = self.address_input_field.value
            self.label.update(f"Adres kontraktu: {self.address}")
            self.address_input_field.disabled = True
        if event.button.id == "submit_private_key":
            self.private_key = self.private_key_input_field.value
            self.private_key_input_field.disabled = True
            self.label2.update(f"Klucz prywatny: {self.private_key}")
        if event.button.id == "submit_folder_name":
            self.folder_name = self.folder_name_input_field.value
            self.folder_name_input_field.disabled = True
            self.label3 = Label(f"Folder: {self.folder_name}")
        if event.button.id == 'submit_col_name':
            self.col_name = self.collection_name_input_field.value
            self.collection_name_input_field.disabled = True
            self.label4.update(f"Nazwa kolekcji: {self.col_name}")


        

MyApp().run()
