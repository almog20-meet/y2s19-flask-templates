from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template ("index.html" , foods = ["Pasta" , "Pizza" , "Hamburger" , "Sushi"])
    ham = "https://www.google.co.il/url?sa=i&source=images&cd=&ved=2ahUKEwi3gcqlt9rjAhXFaFAKHWLzC-MQjRx6BAgBEAU&url=https%3A%2F%2Fwww.epicurious.com%2Frecipes%2Ffood%2Fviews%2Fthe-ultimate-hamburger-232191&psig=AOvVaw2SMOEl6QPSV5l1LqSwJfvs&ust=1564500096544029"
if __name__ == '__main__':
   app.run(debug = True)
