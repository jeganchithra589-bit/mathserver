# Ex.05 Design a Website for Server Side Processing
# Date:02/10/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
<!DOCTYPE html>
<html>
<head>
    <title>POWER CALCULATOR</title>
    <style>
        body {
            font-family: 'Gill Sans', sans-serif;
            text-align: center;
            margin-top: 50px
           
        }
        .container {
            max-width: 300px;
            margin: auto;
            padding: 30px;
            border: 10px solid=cyan;
            background-color:tan;
            border-radius:20px;
        }
        input, button {
            margin: 10px;
            padding: 5px;
        }
    </style>
</head>
<body style="background:linear-gradient(red,rgb(11, 0, 128),cyan);">
<body>
    <form method="POST">
        {% csrf_token %}
    <div class="container">
        <h2>POWER CALCULATOR </h2>
      Current (A):
        <input type="text" name="current" 
        placeholder="{{current}}"></input><br>
      Resistance (ohms):
        <input type="text" name="resistance" 
        placeholder="{{resistance}}"></input><br>
        <button type="submit">CALCULATOR</button><br>
      POWER:<input type="text" name="power" 
        value="{{power}}"></input>W</div>
        
    </div>
    </form>   
</body>   
</html>


url.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns =[
    path('admin/',admin.site.urls),
    path('',views.power,name="jegan")
]


views.py

from django.shortcuts import render


def power(request):
    context={}
    context['power']=""
    context['current']="0"
    context['resistance']="0"
    if request.method =="POST":
        print("POST method is used")
        current = request.POST.get('current','0')
        resistance= request.POST.get('resistance','0')
        print('request=',request)
        print('current=',current)
        print('Resistance=',resistance)
        power=(int(current)**2)*int(resistance)
        context['power']= power
        context['current']= current
        context['resistance']= resistance
        print('Power=',power)
    return render(request,'myapp/power.html',context)

```
    
# SERVER SIDE PROCESSING:
![alt text](<Screenshot (73).png>)
# HOMEPAGE:
![alt text](<Screenshot (75).png>)
# RESULT:
The program for performing server side processing is completed successfully.
