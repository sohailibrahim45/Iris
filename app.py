from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        input1 = float(request.form.get("input1"))
        input2 = float(request.form.get("input2"))
        input3 = float(request.form.get("input3"))
        input4 = float(request.form.get("input4"))
        print(input1,input2,input3,input4)
        p=[input1,input2,input3,input4]
        p=[np.array(p)]
        result=model.predict(p)
        print(result)

    return render_template("index.html",result = "The flower species is {}".format(result))
if __name__=="main":
    app.run(debug=True)