from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty

model = '../img/boy'

def onChange(text):
    global model
    model = text
    print('asldksa;flksa',text)
