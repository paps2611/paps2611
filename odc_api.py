from flask import Flask, request
from ODC_localfiles import run_detector

app = Flask(__name__)


@app.route('/Object_detect',methods = ['POST', 'GET'])
def Object_detect():
    if request.method=='GET' :
        input_img_path = request.args.get("input_img_path")
        # print(input_img_path,"-------------")
        run_detector(input_img_path)
        return "Object detected successfully! >3"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug = True)