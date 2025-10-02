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
