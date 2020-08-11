from django.shortcuts import render
import os
import sys
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.test import Client
from django.http import HttpResponse
from django.db import connection
from fpdf import FPDF
from .models import Cat
from .models import Sub
from .models import Act
from .models import Users

from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def homepage(request):
	print("cat"+str(Cat.objects.all()))
	print("sub"+str(Sub.objects.all()))
	print("act"+str(Act.objects.all()))
	print("us"+str(Users.objects.all()))
	return render(request=request,template_name="main/home_demo.html")

@csrf_exempt
def homepage_choose(request):
    print(request.POST)
    #print(Cat.objects.all())
    #print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    #print(int(request.POST.get('id')))
    userid=int(request.POST.get('id'))
    #id=int(userid[1:len(userid)-1])
    us_choice=''
    #print("Active DB ",connection.settings_dict['NAME'])
    try:
        print("inside try of sequence_already_present")
        u=Users.objects.get(us_id=userid)
        us_choice=u.us_des
    except ObjectDoesNotExist:
        us_choice=''
    except Exception as e:
        print("exception : " + str(e))
        
    if us_choice!='':
        print("true")
        print(us_choice)
        #return render(request=request,template_name="main/home.html",context={"category":Cat.objects.all(),"subcategory":Sub.objects.all(),"activity":Act.objects.all()})
        return render(request,"main/home.html",{"users":[userid,us_choice]})


    else:
        print("false")
        '''
        response = HttpResponse('Your message here', status=401)
        response['Content-Length'] = len(response.content)
        return response'''
        return render(request,"main/home.html")
        #return render(request=request,template_name="main/home.html",context={"category":Cat.objects.all(),"subcategory":Sub.objects.all(),"activity":Act.objects.all()})


        
def check(request):
     return render(request=request,template_name="main/home.html",context={"category":Cat.objects.all(),"subcategory":Sub.objects.all(),"activity":Act.objects.all()})

    
    
    
def generate_output(request):

    cat=request.GET.get('Category')
    sub=request.GET.get('Sub_Category')
    act=request.GET.get('Activity')
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",'B',size=16)
    pdf.write(5,"Category\n\n")
    line=1
    pdf.set_font("Arial",size=12)
    waste=['"','[',']']
    cat = ''.join(i for i in cat if not i in waste)
    cat=cat.split(',')
    sub = ''.join(i for i in sub if not i in waste)
    sub=sub.split(',')
    act = ''.join(i for i in act if not i in waste)
    act=act.split(',')
    i=0
    for c in cat:
        if(i==len(cat)-1):
            pdf.write(3,c+"\n\n\n")
        else:
            if(i%4==0 and i!=0):
                pdf.write(3,c+"\n\n\n")
            else:
                pdf.write(3,c+"   ")
        i+=1
    pdf.set_font("Arial",'B',size=16)
    pdf.write(5,"Sub Category\n\n")
    pdf.set_font("Arial",size=12)
    i=0
    for s in sub:
        if(i==len(sub)-1):
            pdf.write(3,s+"\n\n\n")
        else:
            if(i%4==0 and i!=0):
                pdf.write(3,s+"\n\n\n")
            else:
                pdf.write(3,s+"   ")
        i+=1
    pdf.set_font("Arial",'B',size=16)
    pdf.write(5,"Activity\n\n")
    pdf.set_font("Arial",size=12)
    i=0
    for a in act:
        if(i==len(act)-1):
            pdf.write(3,a+"\n\n\n")
        else:
            if(i%4==0 and i!=0):
                pdf.write(3,a+"\n\n\n")
            else:
                pdf.write(3,a+"   ")
        i+=1
    pdf.output("Report.pdf")

def generate_new_output(request):

    cat=request.GET.get('Category')
    sub=request.GET.get('Sub_Category')
    act=request.GET.get('Activity')
    t=request.GET.get('Reason')
    print(t)
    print(type(t))
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",'B',size=16)
    pdf.write(5,"Category\n\n")
    line=1
    pdf.set_font("Arial",size=12)
    waste=['"','[',']']
    cat = ''.join(i for i in cat if not i in waste)
    cat=cat.split(',')
    sub = ''.join(i for i in sub if not i in waste)
    sub=sub.split(',')
    act = ''.join(i for i in act if not i in waste)
    act=act.split(',')
    t=''.join(i for i in t if not i in waste)
    i=0
    for c in cat:
        if(i==len(cat)-1):
            pdf.write(3,c+"\n\n\n")
        else:
            if(i%4==0 and i!=0):
                pdf.write(3,c+"\n\n\n")
            else:
                pdf.write(3,c+"   ")
        i+=1
    pdf.set_font("Arial",'B',size=16)
    pdf.write(5,"Sub Category\n\n")
    pdf.set_font("Arial",size=12)
    i=0
    for s in sub:
        if(i==len(sub)-1):
            pdf.write(3,s+"\n\n\n")
        else:
            if(i%4==0 and i!=0):
                pdf.write(3,s+"\n\n\n")
            else:
                pdf.write(3,s+"   ")
        i+=1
    pdf.set_font("Arial",'B',size=16)
    pdf.write(5,"Activity\n\n")
    pdf.set_font("Arial",size=12)
    i=0
    for a in act:
        if(i==len(act)-1):
            pdf.write(3,a+"\n\n\n")
        else:
            if(i%4==0 and i!=0):
                pdf.write(3,a+"\n\n\n")
            else:
                pdf.write(3,a+"   ")
        i+=1
    pdf.set_font("Arial",'B',size=16)
    pdf.write(5,"\n\n\nReason\n\n")
    pdf.set_font("Arial",size=12)
    pdf.write(3,t)
    pdf.output("Updated_Report.pdf")
