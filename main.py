from flask import Flask, request, render_template

# raspberry pi


def set_power(power):
    print(power)


def set_light(light):
    print(light)


def set_horn(horn):
    print(horn)
#todo play sound when charged

def handle_request(request):
    set_power(request['power'])
    set_light(request['light'])
    set_horn(request['horn'])


# server
app = Flask(__name__, template_folder='template')


@app.route('/', methods=['POST', 'GET'])
def handler():
    if request.method == 'POST':
        handle_request(request.form)
        return "ok"

    else:
        user = request.args.get('nm')
        return render_template('index.html')


if __name__ == "__main__":
    app.run("192.168.178.26", 8080, debug=True)

