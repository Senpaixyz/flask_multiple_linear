from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    submission_successful = False
    if request.method == 'POST':
        name = request.form['name']
        sex = int(request.form['sex'])
        children = int(request.form['children'])
        age = int(request.form['age'])
        region = int(request.form['region'])
        bmi=float(request.form['bmi'])
        bmi_group = int(request.form['bmi_group_value'])
        smoker = int(request.form['isSmoker'])



        prediction=model.predict([[sex,children,age,region,bmi,bmi_group,smoker]])
        output=round(prediction[0],2)

        return render_template('index.html',
                prediction_text=("Hello! " + name + " the predicted insurance charges will be " + str(output)),
                submission_successful = True
                )
    else:
        return render_template('index.html',
                submission_successful=False)

if __name__=="__main__":
    app.run(debug=True)


