from django.shortcuts import render
import numpy as np

import pickle

model= pickle.load(open('./model.pkl', 'rb'))

vectorizer= pickle.load(open('./vectorizer.pkl', 'rb'))
def home(request):
    if request.method=="POST":
        
        password=request.POST['password']
        arr=np.array([password])
        
        matrix=vectorizer.transform(arr)
        length_pass=len(password)
        length_normalized_lowercase=len([char for char in password if char.islower()])/len(password)
    
        new_matrix=np.append(matrix.toarray(),(length_pass,length_normalized_lowercase)).reshape(1,101)
        result=model.predict(new_matrix)
        if result==0:
            result='Weak Password'
        elif result==1:
            result='Normal Password'
        else:
            result='Strong Password'
            
        return render(request,"index.html",{'result':result})
    
    return render(request,"index.html")

