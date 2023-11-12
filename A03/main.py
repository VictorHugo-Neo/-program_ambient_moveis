#Importando as classes da biblioteca Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

#Definindo a classe principal da aplicação
class MyApp(App):
    def build(self): 

        #criação da layout da aplicação
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Nome
        nome_label = Label(text='Nome:')
        nome_input = TextInput(multiline=False)
        layout.add_widget(nome_label)
        layout.add_widget(nome_input)

        # Sexo
        sexo_label = Label(text='Sexo:')
        feminino_checkbox = CheckBox(group='sexo', active=True)
        masculino_checkbox = CheckBox(group='sexo', active=False)
        layout.add_widget(sexo_label)
        layout.add_widget(feminino_checkbox)
        layout.add_widget(Label(text='Feminino'))
        layout.add_widget(masculino_checkbox)
        layout.add_widget(Label(text='Masculino'))

        # Botão
        button = Button(text='Enviar', on_press=self.validate_and_submit)
        layout.add_widget(button)

        return layout
    #método para realizar a validação dos dados quando o botão é precionado
    def validate_and_submit(self, instance):
        nome_input = self.root.children[0].children[1]
        sexo = 'Feminino' if self.root.children[2].children[1].active else 'Masculino'

        # Realizando validação do formulário
        if nome_input.text == "":
            print("Preenchimento obrigatório")
        else:
            print(f"Nome: {nome_input.text}, Sexo: {sexo}")
#verificando se o script está sendo executado diretamente
if __name__ == '__main__':
    #inciando a aplicação chamando o método
    MyApp().run()