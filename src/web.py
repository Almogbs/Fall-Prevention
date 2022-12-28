from fall_prevention_modes import CollectMode, PredMode
from fall_prevention_patient import Patient
from fall_prevention_server import Server
from flask import Flask, render_template, request
from turbo_flask import Turbo
from enum import Enum, auto
import threading
import time

app = Flask(__name__, template_folder='fall_prevention_web/html', static_folder='fall_prevention_web')
turbo = Turbo(app)

NUM_CLIENTS = 1
PORT = 13380
IP = "192.168.0.100"
ADDR = (IP, PORT)

pred = PredMode()
server = Server(addr=ADDR, num_clients=NUM_CLIENTS, operator=pred)
patient1 = Patient.readPatientsJson("fall_prevention_web/assets/json/patient.json")[0]

class Position(Enum):
    BACK_LAYING = 0
    LEFT_LAYING = auto()
    RIGHT_LAYING = auto()
    LEFT_ALARM = auto()
    RIGHT_ALARM = auto()
    
Positions = ["Back Laying", "Left Side Laying", "Right Side Laying",
             "Left Side Alarm!", "Right Side Alarm!"]

AlarmPositions = [Position.LEFT_ALARM.value, Position.RIGHT_ALARM.value]

PositionsFiles = ["back", "left", "right", "left_alarm", "right_alarm"]


def update_datetime():
    with app.app_context():
        while True:
            time.sleep(1)
            turbo.push(turbo.replace(render_template('datetime.html'), 'load_datetime'))

@app.context_processor
def get_datetime():
    curr_date = f"{time.strftime(f'%d/%m/%Y', time.gmtime())}"
    curr_time = f"{time.strftime(f'%H:%M:%S', time.gmtime())}"
    return {'curr_time': curr_time, 'curr_date': curr_date}

def posToStr(pos):
    if not isPosValid(pos):
        return

    return Positions[pos]

def posToFile(pos):
    if not isPosValid(pos):
        return
    
    return PositionsFiles[pos]

def isPosAlarm(pos):
    return pos in AlarmPositions

def isPosValid(pos):
    return pos <= Position.RIGHT_ALARM.value and pos >= Position.BACK_LAYING.value

def update_position():
    with app.app_context():
        while True:
            time.sleep(5)
            turbo.push(turbo.replace(render_template('position.html'), 'load_position'))

@app.context_processor
def get_position():
    pos = pred.last_pred
    position = posToStr(pos)
    position_image = posToFile(pos)
    position_alarm = ""
    if isPosAlarm(pos):
        position_alarm = "alarm"

    return {'position': position, 'position_image': position_image, 'alarm':position_alarm}

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_datetime).start()
    threading.Thread(target=update_position).start()

@app.route('/edit_patient')
def edit_patient():
    new_vals = {k:v for k,v in request.args.items()}
    try:
        patient1.update(new_vals)
    except Exception as e:
        print(e)

    return render_template('edit_patient.html', patient=patient1)

@app.route('/patient')
def patient():
    return render_template('patient.html', patient=patient1)

@app.route('/')
def home():
    return render_template('home.html')
 
def startServer():
    server.start()

if __name__ == '__main__':
    threading.Thread(target=startServer).start()
    app.run(host='0.0.0.0', port=56000)