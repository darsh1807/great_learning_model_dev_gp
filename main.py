from flask import Flask, request, Response
from  joblib import load, dump
import pandas as pd

app = Flask(__name__)

def create_df(df):
    temp_dict = {'sepal.length':[df[0]], 'sepal.width':[df[1]], 'petal.length':[df[2]], 'petal.width':[df[3]]}
    df_temp = pd.DataFrame(temp_dict)
    return df_temp

@app.route("/", methods=['POST','GET'])
def test():
    my_model = load("decision_tree_model_iris.joblib")
    data = request.json
    df_temp = create_df(data)
    model_prediction = my_model.predict(df_temp)
    label = load("label_encoder.joblib")
    model_result = label.inverse_transform(model_prediction)
    return Response(str(model_result))



if __name__ == '__main__':
    app.run(debug=True)