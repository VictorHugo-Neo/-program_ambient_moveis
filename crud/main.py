from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import json

class CrudApp(App):
    def build(self):
        self.data_file = "data.json"
        self.load_data()

        # Layout principal
        layout = BoxLayout(orientation="vertical")

        # Lista para exibir dados
        self.data_list = Label(text=self.get_data_as_string())
        layout.add_widget(self.data_list)

        # Campos de entrada
        self.input_name = TextInput(hint_text="Nome")
        self.input_age = TextInput(hint_text="Idade")
        layout.add_widget(self.input_name)
        layout.add_widget(self.input_age)

        # Botões de operação CRUD
        btn_add = Button(text="Adicionar", on_press=self.add_data)
        btn_update = Button(text="Atualizar", on_press=self.update_data)
        btn_delete = Button(text="Deletar", on_press=self.delete_data)
        layout.add_widget(btn_add)
        layout.add_widget(btn_update)
        layout.add_widget(btn_delete)

        return layout

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.data, file)

    def get_data_as_string(self):
        return "\n".join([f"{entry['name']} - {entry['age']} anos" for entry in self.data])

    def add_data(self, instance):
        name = self.input_name.text
        age = self.input_age.text

        if name and age:
            entry = {"name": name, "age": age}
            self.data.append(entry)
            self.save_data()
            self.data_list.text = self.get_data_as_string()

    def update_data(self, instance):
        name = self.input_name.text
        age = self.input_age.text

        if name and age:
            for entry in self.data:
                if entry["name"] == name:
                    entry["age"] = age
                    break
            self.save_data()
            self.data_list.text = self.get_data_as_string()

    def delete_data(self, instance):
        name = self.input_name.text

        if name:
            self.data = [entry for entry in self.data if entry["name"] != name]
            self.save_data()
            self.data_list.text = self.get_data_as_string()

if __name__ == "__main__":
    CrudApp().run()
