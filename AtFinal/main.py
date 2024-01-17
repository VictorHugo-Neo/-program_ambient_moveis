import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
import sqlite3
from datetime import date

Builder.load_file("gui.kv")

class GratitudeScreen(Screen):
    def __init__(self, **kwargs):
        super(GratitudeScreen, self).__init__(**kwargs)
        self.conexao = sqlite3.connect("gratitude.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tb_gratidoes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                data DATE,
                                gratidao_texto TEXT
                              )""")
        self.conexao.commit()

    def inserir_gratidao(self, texto):
        data_atual = date.today().strftime("%Y-%m-%d")
        try:
            self.cursor.execute("INSERT INTO tb_gratidoes (data, gratidao_texto) VALUES (?, ?)", (data_atual, texto))
            self.conexao.commit()
            self.ids.lbl_resposta.text = "Registro de Gratidão Adicionado com Sucesso!"
        except sqlite3.Error as error:
            self.ids.lbl_resposta.text = "Erro ao adicionar gratidão."

    def visualizar_gratidoes(self):
        gratidoes = self.obter_gratidoes()
        gratitude_list_screen = self.manager.get_screen("gratitude_list_screen")
        gratitude_list_screen.atualizar_lista(gratidoes)
        self.manager.current = "gratitude_list_screen"

    def obter_gratidoes(self):
        try:
            self.cursor.execute("SELECT * FROM tb_gratidoes")
            gratidoes = self.cursor.fetchall()
            return gratidoes
        except sqlite3.Error as error:
            print("Erro ao buscar gratidões.", error)
            return []

    def deletar_gratidao(self, gratidao_id):
        try:
            self.cursor.execute("DELETE FROM tb_gratidoes WHERE id=?", (gratidao_id,))
            self.conexao.commit()
            self.visualizar_gratidoes()  # Atualiza a lista após a exclusão
        except sqlite3.Error as error:
            print("Erro ao deletar gratidão.", error)

class GratitudeListScreen(Screen):
    lista_gratidoes = ObjectProperty(None)

    def atualizar_lista(self, gratidoes):
        self.lista_gratidoes.clear_widgets()
        for gratidao in gratidoes:
            box_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=30)
            label = Label(text=f"Data: {gratidao[1]}, Gratidão: {gratidao[2]}", font_size="16sp", size_hint_x=0.8)
            btn_deletar = Button(text="Deletar", size_hint_x=0.2, on_release=lambda x, gratidao_id=gratidao[0]: self.deletar_gratidao(gratidao_id))
            box_layout.add_widget(label)
            box_layout.add_widget(btn_deletar)
            self.lista_gratidoes.add_widget(box_layout)

    def deletar_gratidao(self, gratidao_id):
        app = App.get_running_app()
        app.root.get_screen("gratitude_screen").deletar_gratidao(gratidao_id)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        gratitude_screen = GratitudeScreen(name="gratitude_screen")
        gratitude_list_screen = GratitudeListScreen(name="gratitude_list_screen")

        sm.add_widget(gratitude_screen)
        sm.add_widget(gratitude_list_screen)

        return sm

if __name__ == "__main__":
    MainApp().run()
