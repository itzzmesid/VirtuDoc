from django.shortcuts import render
import joblib
import numpy as np
 

def home(request):
    return render(request,'backend/index.html')
 
def heart(request):
    return render(request,'backend/heart.html')
 
def kidney(request):
    return render(request,'backend/kidney.html')
 
def diabetes(request):
    return render(request,'backend/diabetes.html')

def liver(request):
    return render(request,'backend/liver.html')


def ValuePredictor(to_predict_list,size,model_name):
    mdname = str(model_name)
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        trained_model = joblib.load(rf'/home/sid/VirtuDoc/{mdname}_model.pkl')
        result = trained_model.predict(to_predict)
    return result[0]
  

def kdpredictor(request):
    mname = "kidney"
    klis = []
    klis = [request.POST.get(i, False) for i in ('Year', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc')]
 
    if(len(klis)==7):
            result = ValuePredictor(klis,7,mname)
 
    if(int(result)==1):
        return render(request,'backend/risk.html')
    else:
        return render(request,'backend/norisk.html')
 
 
def hdpredictor(request):
    mname = "heart"
    hlis = []
    hlis = [request.POST.get(i, False) for i in ('cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang')]    
    if(len(hlis)==7):
        result = ValuePredictor(hlis,7,mname)
    
    if(int(result)==1):
        return render(request,'backend/risk.html')
    else:
        return render(request,'backend/norisk.html')


def lpredictor(request):
    mname = "liver"
    llis = []
    llis = [request.POST.get(i, False) for i in ('Total Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio')]
 
    if(len(llis)==7):
            result = ValuePredictor(llis,7,mname)
 
    if(int(result)==1):
        return render(request,'backend/risk.html')
    else:
        return render(request,'backend/norisk.html')
 
 
 
def DiabetesValuePredictor(to_predict_list,size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==6):
        trained_model = joblib.load(r'/home/sid/VirtuDoc/diabetes_model.pkl')
        result = trained_model.predict(to_predict)
    return result[0]
 
 
def dbpredictor(request):
    dblis = []
    dblis.append(request.POST['Pregnancies'])
    dblis.append(request.POST['Present_Price'])
    dblis.append(request.POST['BloodPressure'])
    dblis.append(request.POST['BMI']) 
    dblis.append(request.POST['DiabetesPedigreeFunction'])
    dblis.append(request.POST['Age'])   
    if(len(dblis)==6):
        result = DiabetesValuePredictor(dblis,6)
    
    if(int(result)==1):
        return render(request,'backend/risk.html')
    else:
        return render(request,'backend/norisk.html')
