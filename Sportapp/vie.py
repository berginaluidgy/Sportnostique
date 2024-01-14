from http.client import responses
from django.http import JsonResponse
import requests
from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import User,Account
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from datetime import date
# import pgrwpy
from .serializers import UserSerializer
import datetime
from django.utils import timezone

import jwt
from rest_framework.views import APIView
directionhome='./page/Home.html'
directionuser='./page/Users.html'
directionpayment='./page/payment.html'
directionadm='./page/adminpage.html'


@login_required
def  getpronos(request):
    from. import newfile
    print()
    print(request.POST)
    struse=request.POST
    sorted=str(struse).split("<querydict:{'{'name':")
    newsorted=sorted[1].split("}':['']}")
    interfixture=int(newsorted[0])
    print(int(newsorted[0]))
    return JsonResponse(newfile.pronossafe(interfixture))
    # return Response(newfile.pronossafe())
    
def getpronosmultiple(request): 
    from. import newfile
    print()
    print(request.POST)
    struse=request.POST
    sorted=struse.split("<querydict:{'{'name':")
    newsorted=sorted[1].split("}':['']}")
    interfixture=int(newsorted[0])
    print(int(newsorted[0]))
    tabrecorm=[1,1,1,1]
    recaptab=[]
    for fixpronos in tabrecorm:
       fixtureandpronos= newfile.pronossafe(fixpronos)
       recaptab.append(fixtureandpronos)
    print(recaptab)  
    return JsonResponse(recaptab) 
        
    
    

class RegisterApi(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save
        print(serializer.save())
        return Response(serializer.data)
                       
class loginApi(APIView):
    def post(self,request):
        name=request.data['name']
        password=request.data['password']     
        user=User.objects.filter(name=name).first()
        if user is None:
            raise AuthenticationFailed("Nom d'utilisateur non trouvé")
        if not user.check_password(password):
            raise AuthenticationFailed("Mot de passe incorrect")
        
        
        playload={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
                             
        token=jwt.encode(playload,'secret',algorithm='HS256').decode('utf-8')
        response=Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token
        }
        return Response


def home(request):
    name=request.POST.get('nom')
    prenom=request.POST.get('prenom')
    numero=request.POST.get('phone')
    password=request.POST.get('Mot de passe')
    boost=request.POST.get('choose')
    
    print(name,boost,password,numero)
    if boost=='signup':
        endpoint='http://localhost:8000/signup'
        response=requests.post(endpoint,json={
   
        "name":name,
        "prenom":prenom,
        "password":password,

        })

        print(response.status_code)
        print(response.json())
        if response.status_code==200:
            user=User.objects.filter(name=name).first()
            account=Account.objects.create(nom=name,prenom=prenom,tel=numero,affiliate=0,argentGagner=0,codeAff=0,identifiant=0)
           
            
            return render(request,directionpayment)
    if boost=='login':
        user=User.objects.filter(name=name).first()
        checkingUser=user.check_password(password)
        print(user.check_password(password))
        if checkingUser==True:
            Accountfilter=Account.objects.filter(nom=name).first()
            print(Accountfilter.nom)
            if Accountfilter.actifaccount==True: 
                context={
                'argent':Accountfilter.argentGagner,
                'nom':Accountfilter.nom,
                
                }
                
                return render(request,directionuser,context) 
            else:
                return render(request,directionpayment) 
    
     
    return render(request,directionhome)
@login_required
def Userpage(request):
   

    return render(request,directionuser)    
    
def payment(request):
   

    return render(request,directionpayment)              



@api_view(['get'])
def paymentmoncash(request):
    # montant=request.POST.get('')
    def payment(cash):
        pass
        
        # PG_USER_ID='eda2d807-bb47-4e71-a752-be4591b31b07'
        # PG_SECRET_KEY='sk_17734e0df0b2483355e6045b5f4d3fe8'

        # client = pgrwpy.Client(auth=(PG_USER_ID, PG_SECRET_KEY),
        #                         production_mode=False)

        # print(client.get_version())
        # etape1=moncashify.API('c7832bf1969f82708a4eb6a668ffa8e2','oHrr4tbnB1PH0uz6VQNUvY3d4OUOKOcnAydYMWn7zeysMxkVIpevkmw2dz6rDQib')
        # etape2=etape1.payment('Paris Sportif',cash)
        # etape3=etape2.redirect_url
        # return etape3

    # print(payment(129))
    return Response(payment(12))



def adm(request):
    alluser=User.objects.all()
    nbruser=len(alluser)
    Accountfilter=Account.objects.all()
    sumargent=[]
    print(str(date.today()))
    print(str(alluser[5].date_joined).find(str(date.today())))
    for arg in Accountfilter:
        if arg.actifaccount==True:
            sumargent.append(1)
        else:
            sumargent.append(0)  
    nbragent=sum(sumargent)    
    
    datejoined=User.objects.all()
    datetab=[] 
    
    for dateuser in datejoined:
       
      strdate=str(dateuser.date_joined).find(str(date.today()))
      if strdate!=-1: 
        datetab.append(1) 
      else:
        datetab.append(0)     
        print(str(strdate)+'ok')
    context={
        'numberuser':nbruser,
        'numberargent':nbragent*60,
        'nbrusertoday':sum(datetab)
        
    }
    
    return render(request,directionadm,context)


