from http.client import responses
from django.http import JsonResponse
import requests
import random 
from django.contrib.auth import authenticate, login

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import User,Account
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from datetime import date
# import pgrwpy
from .serializers import UserSerializer,accSerializer
import datetime
from django.utils import timezone
from rest_framework import generics
import jwt
from rest_framework.views import APIView
import time
directionhome='./page/Home.html'
directionuser='./page/Users.html'
directionpayment='./page/payment.html'
directionadm='./page/adminpage.html'


# @login_required
@api_view(['get'])
def  getpronos(request,id,idleague):
    from. import newfile
    print(request)
    print(id)
    print(idleague)
    print(newfile.pronossafe(id,idleague))
    
    return JsonResponse(newfile.pronossafe(id,idleague))
    # return Response(newfile.pronossafe())
@api_view(['get'])    
def getpronosmultiple(request): 
    from. import newfile
    tabrecoverry=[138,140,141,142,139,135,136,39,40,61,62,63,78,94,95,144,145,307,309,310]
    def base(endpoint):
    
        url ="https://v3.football.api-sports.io/"+endpoint
        headers={
        'x-rapidapi-key': '2f554e59b05daef4304c2752e4fff0a8',
        'x-rapidapi-host': 'v3.football.api-sports.io'}
        response = requests.request("GET", url, headers=headers)
        resjson=response.json()
        
        return resjson['response']
    
    for lg in tabrecoverry:
        
        leaguetabrecov=base(' https://v3.football.api-sports.io/leagues?country='+str(lg)+'&season=2023&type=league')
        randomnbr1=random.randint(1,len(leaguetabrecov))
        randomnbr2=random.randint(1,len(leaguetabrecov))
        randomnbr3=random.randint(1,len(leaguetabrecov))
        randomnbr4=random.randint(1,len(leaguetabrecov))
        tabinit=[randomnbr1,randomnbr2,randomnbr3,randomnbr4]
        
        
        print()
    print(request.POST)
    
    return JsonResponse() 
        
def  admin_get_Unique_user(request,name):
    unique=Account.objects.all()
    context={}
    for account in unique:
        if account.nom==name:
            context['name']=account.nom
            context['prenom']=account.prenom
            context['date']=account.date
            context['isactif']=account.actifaccount
        
    return JsonResponse(context,safe=False,status=200)     
    

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
    base_uri=request.build_absolute_uri()
    name=request.POST.get('nom')
    prenom=request.POST.get('prenom')
    numero=request.POST.get('phone')
    password=request.POST.get('Mot de passe')
    boost=request.POST.get('choose')
    
    print(name,boost,password,numero)
    if boost=='signup':
        print('signup')
        endpoint=base_uri+'signup'
        print(endpoint)
        print('gooooo')
        Usercreate=User.objects.create(name=name,prenom=prenom, password=password)
        user=User.objects.filter(name=name).first()
        account=Account.objects.create(nom=name,prenom=prenom,tel=numero,affiliate=0,argentGagner=0,codeAff=0,identifiant=0)
        return render(request,directionpayment)   
    #    response=requests.post(endpoint,json={
   #
     #   "name":name,
       # "prenom":prenom,
        #"password":password,

        #})

      #  print(response.status_code)
        #print(response.json())
       # if response.status_code==200:
            
            
            
    if boost=='login':
        print('loginreper')
        user=User.objects.filter(name=name).first()
        #checkingUser=user.check_password(password)
        checkingUser=authenticate(request, username=name, password=password)
        print('etape 2',checkingUser)
        if checkingUser==True:
            print('login2')
            Accountfilter=Account.objects.filter(nom=name).first()
            print(Accountfilter.nom)
            if Accountfilter.actifaccount==True: 
                context={
                'argent':Accountfilter.argentGagner,
                'nom':Accountfilter.nom,
                
                }
                print('éaooojdj')
                
                return render(request,directionuser,context) 
            else:
                return render(request,directionpayment) 
        else:
            return HttpResponse("ou antre yon non oubyen yon motdpas ki pa korek")
    
     
    return render(request,directionhome)
@login_required
def Userpage(request):
   

    return render(request,directionuser)    
    
def payment(request):
    print(request.build_absolute_uri())
    print(request.get_full_path())
    print(request.path)
   

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
        'numberargent':nbragent*500,
        'nbrusertoday':sum(datetab)
        
    }
    
    return render(request,directionadm,context)


@api_view(['get'])
def updatechecking(request,data):
    pre_base_uri=request.build_absolute_uri()
    pageurl=request.path
    base_uri=pre_base_uri.replace(pageurl,'')
    print(pre_base_uri,pageurl,base_uri)
    datas=data
    getdata=Account.objects.all()
    aktiv=getdata
    dts=''
    for dt in getdata:
       if dt.nom==data: 
           if dt.actifaccount==False:
                # endpointe='http://localhost:8000/updating/'+str(dt.pk)
                endpointe=base_uri+'/updating/'+str(dt.pk)
                responsesearch=requests.put(endpointe,json={
                    'nom':dt.nom,
                    'prenom':dt.prenom,
                    'tel':dt.tel,
                    'affiliate':dt.affiliate,
                    'argentGagner':dt.argentGagner,
                    'codeAff':dt.codeAff,
                    'identifiant':dt.identifiant,
                    
                    'actifaccount':True
                })
            
                print(responsesearch.json)
           else:
                endpointe=base_uri+'/updating/'+str(dt.pk)
                responsesearch=requests.put(endpointe,json={
                    'nom':dt.nom,
                    'prenom':dt.prenom,
                    'tel':dt.tel,
                    'affiliate':dt.affiliate,
                    'argentGagner':dt.argentGagner,
                    'codeAff':dt.codeAff,
                    'identifiant':dt.identifiant,
                    'actifaccount':False,
                })
            
    from django.core.serializers import serialize
    import json
    
    serialized_data = serialize("json", getdata)
    serialized_data = json.loads(serialized_data)
    serialized_data 
    return JsonResponse(serialized_data,safe=False,status=200)

class updating(generics.UpdateAPIView):
    queryset=Account.objects.all()
    serializer_class=accSerializer
    lookup_field='pk'

