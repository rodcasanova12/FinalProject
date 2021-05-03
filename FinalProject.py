#Name: Rodrigo Casa Nova
# Import modules
from tkinter import *
import webbrowser
import json

class userInterface():
    def __init__(self):
        # Create object
        self.root = Tk()

        # Adjust size
        self.root.geometry("754x327")

        # Add image file
        self.bg = PhotoImage(file="helpandguide.png")

        # Create Canvas
        self.canvas1 = Canvas(self.root, width=400,
                         height=400)

        self.canvas1.pack(fill="both", expand=True)

        # Display image
        self.canvas1.create_image(0, 0, image=self.bg,
                             anchor="nw")
        # Save contact list in json format
        def getJSON(filePathAndName):
            with open(filePathAndName, 'r') as fp:
                return json.load(fp)

        myObj = getJSON('Contact Info.json');

        # Functions to give each button what to do
        def openWhatIsDepression():
            webbrowser.open('https://www.nimh.nih.gov/health/topics/depression/index.shtml')
        def openCrisis():
            webbrowser.open('https://www.nami.org/Your-Journey/Living-with-a-Mental-Health-Condition/What-to-Do-In-a-Crisis')
        def openHowToStop():
            webbrowser.open('https://www.medicalnewstoday.com/articles/325513#changes-in-sleep-habits')
        def openAddContactList():
            import MyApp
            MyApp.MyApp().run()
        def openContactList():
            print(myObj)





        # Create Buttons
        self.button1 = Button(self.root, text="What is Depression?", command=openWhatIsDepression)
        self.button3 = Button(self.root, text="How to Spot Some With Issues", command=openHowToStop)
        self.button2 = Button(self.root, text="Crisis", command=openCrisis)
        self.button4 = Button(self.root, text="Add Contact", command=openAddContactList)
        self.button5 = Button(self.root, text="Contact List", command=openContactList)



        # Display Buttons
        self.button1_canvas = self.canvas1.create_window(100, 10,
                                               anchor="nw",
                                               window=self.button1)

        self. button2_canvas = self.canvas1.create_window(100, 40,
                                               anchor="nw",
                                               window=self.button2)

        self.button3_canvas = self.canvas1.create_window(100, 70, anchor="nw",
                                               window=self.button3)

        self.button4_canvas = self.canvas1.create_window(100, 100, anchor="nw",
                                               window=self.button4)

        self.button5_canvas = self.canvas1.create_window(100, 130, anchor="nw",
                                                         window=self.button5)

        # Execute tkinter
        self.root.mainloop()


def main():
    #To call the UI
    userInterface()

if __name__ == '__main__':
    main()
