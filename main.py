#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

def submit_form(name, surname, email, date, address):
    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name} {surname}, {email}, {date}, {address}\n")

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        date = request.form.get('date')
        address = request.form.get('address')

        submit_form(name, surname, email, date, address)

        text= f"Пользователь {name} {surname} сделал заказ на {date} с почтой для связи {email} с доставкой в {address}"
        print(text)

        return render_template('form_result.html',
                               name=name,
                               surname=surname,
                               email=email,
                               address=address,
                               date=date)

    return render_template('form.html')



#Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

#Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

#Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
app.run(debug=True)

