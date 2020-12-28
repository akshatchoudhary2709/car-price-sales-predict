from flask import Flask,render_template, request,jsonify
import pickle


app=Flask("car_price_prediction")
model=pickle.load(open('car_price_prediction.pkl','rb'))
@app.route('/result',methods=['GET'])
def ping():
    return render_template('price.html')

@app.route('/predict',methods=['POST'])
def result():
    if request.method=='POST':
        Vehicle_type=request.form['Vehicle_type']
        if (Vehicle_type == 'Passenger'):
            Vehicle_type = 0
        else:
            Vehicle_type = 1

        Engine_size = float(request.form['Engine_size'])
        Horsepower =float(request.form['Horsepower'])
        Wheelbase = float(request.form['Wheelbase'])
        Width = float(request.form['Width'])
        Length = float(request.form['Length'])
        Curb_weight = float(request.form['Curb_weight'])
        Fuel_capacity = float(request.form['Fuel_capacity'])
        Fuel_efficiency = float(request.form['Fuel_efficiency'])
        Power_perf_factor = float(request.form['Power_perf_factor'])

        prediction=model.predict([[Vehicle_type,Engine_size,Horsepower,Wheelbase,Width,Length,Curb_weight,Fuel_capacity,Fuel_efficiency,Power_perf_factor]])


        prediction = round(prediction[0], 2)

        return render_template('price.html', prediction_text="The chances of placement is {} ".format(prediction))


if __name__=='__main__':
    app.run(debug=True)
