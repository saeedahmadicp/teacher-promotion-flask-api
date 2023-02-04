from flask import Flask, render_template, request, redirect, url_for, abort
from flask_app import app
from flask_app.forms import InputForm
from load_process_prediction import label_encoder, process_and_predict

#defining the home route
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
    form = InputForm()
    if request.method == 'POST':
         if form.validate_on_submit():
            firstName = form.firstName.data
            lastName = form.lastName.data
            age = form.age.data
            experience = form.experience.data
            grade = form.grade.data
            lastPromotion = form.last_promotion.data
            promo1 = form.promo1.data
            promo2 = form.promo2.data
            promo3 = form.promo3.data
            data = [age, experience, grade, lastPromotion, label_encoder(promo1), label_encoder(promo2), label_encoder(promo3)]
            prediction = process_and_predict(data)
            #redirecting the user to the  page    
            return render_template('result.html', firstName=firstName, lastName=lastName, prediction=prediction)  
    else:
        return render_template('index.html', form=form)

#defing the result route
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':               #use args if using get method
        pass

    else:
        return redirect('/')