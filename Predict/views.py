from django.shortcuts import render
import pandas as pd
import pickle
import numpy as np
from django.http import HttpResponse


data = pd.read_csv('Cleaned_data_final.csv')
pipe = pickle.load(open("LinearRegressionModelFinal.pkl",'rb'))


def predict(request): 
    locations = sorted(data['location'].unique())
    if request.method == 'POST':
        location = str(request.POST['location'])
        print(request.POST['location'])
        bhk = request.POST['bhk']
        bath = request.POST['bath']
        balcony = request.POST['balcony']
        sqft = request.POST['total_sqft']
        
        input = pd.DataFrame([[location,sqft,bath,balcony,bhk]],columns = ['location','total_sqft','bath','balcony','bhk'])
        predicted_price = pipe.predict(input)[0]*100000
        predicted_price = np.round(predicted_price,2)
        
        context = {
            'locations' : locations ,
        'predicted_price' : predicted_price,
        }
        return render(request, 'predict.html', context)
    
    context = {
        'locations' : locations ,
        # 'predicted_price' : predicted_price,
    }
    return render(request, 'predict.html', context)

    

# def predict_price():
    
    # location = request.form.get('location')
    # bhk = request.form.get('bhk')
    # bath = request.form.get('bath')
    # balcony = request.form.get('balcony')
    # sqft = request.form.get('total_sqft')
    
#     # print(<h1>locations</h1>)
    
#     input = pd.DataFrame([[location,sqft,bath,balcony,bhk]],columns = ['location','total_sqft','bath','balcony','bhk'])
#     predicted_price = pipe.predict(input)*100000
    
    
#     # return render(request, 'predict.html', context)
#     return (predicted_price)


