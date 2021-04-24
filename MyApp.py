import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        #main grid
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2


        self.inside.add_widget(Label(text="First Name: "))
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Phone Number: "))
        self.phoneNumber = TextInput(multiline=False)
        self.inside.add_widget(self.phoneNumber)


        self.add_widget(self.inside)
        #Button
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

#function to add functionality to the button. Which will be adding the user
#input to a dictionary
    def pressed(self, instance):
        #self.contactInfo = {}
        firstName = self.firstName.text
        last = self.lastName.text
        phone = self.phoneNumber.text
        fullName = (self.firstName.text +" "+ self.lastName.text)
        self.contactInfo = {fullName : phone}
        cInfo = json.dumps(self.contactInfo)
        with open('Contact Info.json','w') as f:
            f.write(cInfo)
            f.close()
        #need to find a way to append to new list


        #To clear the text once submit button is pressed
        self.firstName.text = ""
        self.lastName.text = ""
        self.phoneNumber.text = ""

        print("\n--- Contact List ---")
        print(self.contactInfo)
        return self.contactInfo
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':

    MyApp().run()