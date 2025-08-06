import json
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from GG_App.models import *
from GG_App.training import *


def logincc(request):
    auth.logout(request)
    return render(request,'login_index.html')




def logout(request):
    auth.logout(request)
    return render(request,'login_index.html')


def login_code(request):
    print(request.POST,"===========================")
    uname = request.POST['uname']
    pswrd = request.POST['password']

    try:
        ob = login_table.objects.get(username=uname, password=pswrd)
        print(ob,"++++++++++++++++++++++++++++++")
        if ob.type == "admin":

            ob1 = auth.authenticate(username="hazna", password="hazna")
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("WELCOME TO ADMIN HOME");window.location='/admin_home'</script>''')
        elif ob.type == "dietitian":
            ob1 = auth.authenticate(username="hazna", password="hazna")
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("WELCOME TO DIETITIAN HOME");window.location='/dietitian_home'</script>''')
        elif ob.type == "doctor":
            ob1 = auth.authenticate(username="hazna", password="hazna")
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("WELCOME TO DOCTOR HOME");window.location='/doc_home'</script>''')
        else:
            return HttpResponse('''<script>alert("INVALID");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("INVALID");window.location='/'</script>''')


@login_required(login_url='/')
def man_dietitian(request):
    ob=dietitian_table.objects.all()
    return render(request,'admin/Man_Dietitian.html',{"val":ob})

@login_required(login_url='/')
def dietitian_search(request):
    name=request.POST['textfield']
    ob = dietitian_table.objects.filter(name__istartswith=name)
    return render(request,'admin/Man_Dietitian.html',{'val':ob})

@login_required(login_url='/')
def add_dietitian(request):
    return render(request, 'admin/AddDietitian.html')

@login_required(login_url='/')
def add_new_dietitian(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield8']
    qualifications=request.POST['textfield2']
    image=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(image.name,image)
    Email=request.POST['textfield4']
    DOB=request.POST['textfield5']
    Gender=request.POST['radiobutton']
    username=request.POST['textfield6']
    password=request.POST['textfield7']

    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type='dietitian'
    ob.save()

    ob1=dietitian_table()
    ob1.firstname=fname
    ob1.lastname=lname
    ob1.qualification=qualifications
    ob1.photo=fsave
    ob1.email=Email
    ob1.dob=DOB
    ob1.gender=Gender
    ob1.LOGIN=ob
    ob1.save()
    return HttpResponse('''<script>alert("Dietitian Added");window.location='man_dietitian'</script>''')



@login_required(login_url='/')
def delete_dietitian(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Dietitian Deleted");window.location='/man_dietitian'</script>''')

@login_required(login_url='/')
def edit_dietitian(request,id):
    ob=dietitian_table.objects.get(id=id)
    request.session['did']=id
    return render(request, 'admin/editDietitian.html',{'val':ob})

@login_required(login_url='/')
def edited_diet(request):
    if 'file' in request.FILES:
        fname = request.POST['textfield']
        lname = request.POST['textfield8']
        qualifications = request.POST['textfield2']
        image = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(image.name, image)
        Email = request.POST['textfield4']
        DOB = request.POST['textfield5']
        Gender = request.POST['radiobutton']

        ob1 = dietitian_table.objects.get(id=request.session['did'])
        ob1.firstname = fname
        ob1.lastname = lname
        ob1.qualification = qualifications
        ob1.photo = fsave
        ob1.email = Email
        ob1.dob = DOB
        ob1.gender = Gender
        ob1.save()
        return HttpResponse('''<script>alert("Dietitian Edited");window.location='man_dietitian'</script>''')
    else:
        fname = request.POST['textfield']
        lname = request.POST['textfield8']
        qualifications = request.POST['textfield2']
        Email = request.POST['textfield4']
        DOB = request.POST['textfield5']
        Gender = request.POST['radiobutton']

        ob1 = dietitian_table.objects.get(id=request.session['did'])
        ob1.firstname = fname
        ob1.lastname = lname
        ob1.qualification = qualifications
        ob1.email = Email
        ob1.dob = DOB
        ob1.gender = Gender
        ob1.save()
        return HttpResponse('''<script>alert("Dietitian Edited");window.location='man_dietitian'</script>''')

# def del_dititian(request):

@login_required(login_url='/')
def man_doc(request):
    ob=doctor_table.objects.all()
    return render(request,'admin/Man_Doctor.html',{"val":ob})
@login_required(login_url='/')
def doc_search(request):
    firstname=request.POST['textfield']
    ob = doctor_table.objects.filter(name__istartswith=firstname)
    return render(request,'admin/Man_Doctor.html',{'val':ob})


@login_required(login_url='/')
def add_doc(request):
    return render(request,'admin/AddDoc.html')


@login_required(login_url='/')
def add_new_doc(request):
    fname = request.POST['textfield']
    lname = request.POST['textfield8']
    qualifications=request.POST['textfield2']
    image=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(image.name,image)
    Email=request.POST['textfield4']
    DOB=request.POST['textfield5']
    Gender=request.POST['radiobutton']
    username=request.POST['textfield6']
    password=request.POST['textfield7']

    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type='doctor'
    ob.save()

    ob1=doctor_table()
    ob1.firstname = fname
    ob1.lastname = lname
    ob1.qualification=qualifications
    ob1.photo=fsave
    ob1.email=Email
    ob1.dob=DOB
    ob1.gender=Gender
    ob1.LOGIN=ob
    ob1.save()
    return HttpResponse('''<script>alert("Doctor Added");window.location='man_doc'</script>''')



@login_required(login_url='/')
def delete_doctor(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Doctor Deleted");window.location='/man_doc'</script>''')

@login_required(login_url='/')
def edit_doc(request,id):
    ob=doctor_table.objects.get(id=id)
    request.session['did']=id
    return render(request, 'admin/editDoc.html',{'val':ob})

@login_required(login_url='/')
def edited_doc(request):
    if 'file' in request.FILES:
        fname = request.POST['textfield']
        lname = request.POST['textfield8']
        qualifications = request.POST['textfield2']
        image = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(image.name, image)
        Email = request.POST['textfield4']
        DOB = request.POST['textfield5']
        Gender = request.POST['radiobutton']

        ob1 = doctor_table.objects.get(id=request.session['did'])
        ob1.firstname = fname
        ob1.lastname = lname
        ob1.qualification = qualifications
        ob1.photo = fsave
        ob1.email = Email
        ob1.dob = DOB
        ob1.gender = Gender
        ob1.save()
        return HttpResponse('''<script>alert("Doctor Edited");window.location='man_doc'</script>''')
    else:
        fname = request.POST['textfield']
        lname = request.POST['textfield8']
        qualifications = request.POST['textfield2']
        Email = request.POST['textfield4']
        DOB = request.POST['textfield5']
        Gender = request.POST['radiobutton']

        ob1 = doctor_table.objects.get(id=request.session['did'])
        ob1.firstname = fname
        ob1.lastname = lname
        ob1.qualification = qualifications
        ob1.email = Email
        ob1.dob = DOB
        ob1.gender = Gender
        ob1.save()
        return HttpResponse('''<script>alert("Doctor Edited");window.location='man_doc'</script>''')

@login_required(login_url='/')
def admin_home(request):
    return render(request,'index.html')

@login_required(login_url='/')
def doc_rating(request):
    return render(request,'admin/DrRating.html')

@login_required(login_url='/')
def Rating_review(request):
    return render(request,'admin/Review_rating.html')
@login_required(login_url='/')
def Rating_review_search(request):
    type=request.POST['select']
    if type=='App':
        ob=rating_table.objects.all()
        return render(request, 'admin/Review_rating.html',{'val':ob,'type':type})
    else:
        ob1=doctor_rating_table.objects.all()

        return render(request,'admin/Review_rating.html',{'val1':ob1,'type':type})

@login_required(login_url='/')
def man_dietplan(request):
    ob = dietplan_table.objects.filter(dietition__LOGIN__id=request.session['lid'])
    return render(request,'Dietitian/Man_Dietplan.html',{"val":ob})
@login_required(login_url='/')
def add_dietplan(request):
    return render(request,'Dietitian/AddDietplan.html')
 # def man_tip(request):
 #    return render(request,'Dietitian/Man_tip.html')

@login_required(login_url='/')
def add_tip(request):
    return render(request,'Dietitian/AddTip.html')

@login_required(login_url='/')
def add_tipcode(request):
    tip = request.POST['textarea']
    ob=tip_table()
    ob.tips=tip
    ob.DIETITION=dietitian_table.objects.get(LOGIN__id=request.session['lid'])
    ob.date=datetime.today()
    ob.time=datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Tip Added Successfully");window.location='man_tip'</script>''')

@login_required(login_url='/')
def dietitian_home(request):
    return render(request,'Dietitian/dietitian_index.html')

@login_required(login_url='/')
def man_schedule(request):
    ob=schedule_table.objects.filter(DOC_ID__LOGIN=request.session['lid'])
    return render(request,'Doctor/Man_Schedule.html',{'val':ob})

@login_required(login_url='/')
def add_schedule(request):
    return render(request,'Doctor/Add_shedule.html')

@login_required(login_url='/')
def schedule_code(request):
    Date=request.POST['textfield']
    FromTime=request.POST['textfield2']
    ToTime=request.POST['textfield3']
    ob = schedule_table()
    ob.date=Date
    ob.from_time=FromTime
    ob.to_time=ToTime
    ob.DOC_ID=doctor_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Schedule Added Successfully");window.location='man_schedule'</script>''')

@login_required(login_url='/')

def edit_schedule(request,id):
    ob = schedule_table.objects.get(id=id)
    request.session['sid'] = id
    return render(request, 'Doctor/edit_schedule.html', {'dt':str(ob.date),'ft':str(ob.from_time),'tt':str(ob.to_time)})

@login_required(login_url='/')
def update_schedule(request):
    Date = request.POST['textfield']
    FromTime = request.POST['textfield2']
    ToTime = request.POST['textfield3']
    ob = schedule_table.objects.get(id=request.session['sid'])
    ob.date = Date
    ob.from_time = FromTime
    ob.to_time = ToTime
    ob.DOC_ID = doctor_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Schedule Edited Successfully");window.location='man_schedule'</script>''')

@login_required(login_url='/')
def delete_schedule(request,id):
    ob=schedule_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Schedule Deleted");window.location='/man_schedule'</script>''')

@login_required(login_url='/')
def schedule_search(request):
    dt=request.POST['textfield']
    ob = schedule_table.objects.filter(date=dt)
    return render(request,'Doctor/Man_Schedule.html',{'val':ob})

@login_required(login_url='/')
def dietplan(request):
    return render(request, 'Dietitian/AddDietplan.html')
@login_required(login_url='/')

def man_tip(request):
    ob=tip_table.objects.filter(DIETITION__LOGIN__id=request.session['lid'])
    return render(request,'Dietitian/Man_tip.html',{'val':ob})

@login_required(login_url='/')
def edit_dietplan(request,id):
    ob=dietplan_table.objects.get(id=id)
    request.session['tiid']=id
    return render(request, 'Dietitian/edit_dietplan.html',{'val':ob})

@login_required(login_url='/')
def edit_dietplancode(request):
    BMI = request.POST['textfield']
    age = request.POST['textfield2']
    gender=request.POST['textfield3']
    dietplan = request.POST['textarea']
    ob = dietplan_table.objects.get(id=request.session['tiid'])
    ob.BMI=BMI
    ob.age = age
    ob.gender=gender
    ob.dietplan= dietplan
    ob.dietition=dietitian_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Dietplan Edited Successfully");window.location='man_dietplan'</script>''')



@login_required(login_url='/')
def add_dietplan(request):
    return render(request,'Dietitian/AddDietplan.html')
@login_required(login_url='/')
def add_dietplancode(request):
    BMI = request.POST['textfield']
    age = request.POST['textfield2']
    gender=request.POST['textfield3']
    dietplan = request.POST['textarea']
    ob = dietplan_table()
    ob.BMI=BMI
    ob.age = age
    ob.gender=gender
    ob.dietplan= dietplan
    ob.dietition=dietitian_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Dietplan Added Successfully");window.location='man_dietplan'</script>''')

@login_required(login_url='/')
def delete_dietplan(request,id):
    ob=dietplan_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Dietplan Deleted");window.location='/man_dietplan'</script>''')

@login_required(login_url='/')
def edit_tip(request,id):
    ob=tip_table.objects.get(id=id)
    request.session['tiid']=id
    return render(request, 'Dietitian/Edittip.html',{'val':ob})

@login_required(login_url='/')
def edit_tipcode(request):
    tip = request.POST['textarea']
    ob=tip_table.objects.get(id=request.session['tiid'])
    ob.tips=tip
    ob.date=datetime.today()
    ob.time=datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Tip Edited Successfully");window.location='man_tip'</script>''')

@login_required(login_url='/')
def delete_tip(request,id):
    ob=tip_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Tip Deleted");window.location='/man_tip'</script>''')
@login_required(login_url='/')
def searchdate(request):
    dt=request.POST['textfield']
    ob = tip_table.objects.filter(date=dt)
    return render(request,'Dietitian/Man_tip.html',{'val':ob})

@login_required(login_url='/')
def man_doubt(request):
    ob = doubt_table.objects.filter(DOC_ID__LOGIN__id=request.session['lid'])
    return render(request,'Doctor/Doubt_clearence.html',{'val':ob})

@login_required(login_url='/')
def doubt_search(request):
    dt=request.POST['textfield']
    ob = doubt_table.objects.filter(date=dt)
    return render(request,'Doctor/Doubt_clearence.html',{'val':ob})


@login_required(login_url='/')
def doc_home(request):
    return render(request,'Doctor/doctor_index.html')

@login_required(login_url='/')
def doubt(request):
    return render(request,'Doctor/Doubt_clearence.html')

@login_required(login_url='/')
def reply(request,id):
    ob=doubt_table.objects.get(id=id)
    request.session['rid']=ob.id
    return render(request,'Doctor/Reply.html')
@login_required(login_url='/')
def send_reply(request):
    a=request.POST['textarea']
    ob=doubt_table.objects.get(id=request.session['rid'])
    ob.reply=a
    ob.date=datetime.now()
    ob.DOC_ID=doctor_table.objects.get(LOGIN__id= request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Reply Added Successfully");window.location='man_doubt'</script>''')






#___________________________________CHAT____________________________



def chatwithuser(request):
    ob = user_table.objects.all()
    return render(request,"Dietitian/fur_chat.html",{'val':ob})




def chatview(request):
    ob = user_table.objects.all()
    d=[]
    for i in ob:
        r={"name":i.first_name,'photo':str(i.photo.url),'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chat_table()
    ob.FROM_ID=login_table.objects.get(id=request.session['lid'])
    ob.TO_ID=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.now().strftime("%Y-%m-%d")
    ob.time=datetime.now()
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=chat_table.objects.filter(FROM_ID__id=id,TO_ID__id=request.session['lid'])
    ob2=chat_table.objects.filter(FROM_ID__id=request.session['lid'],TO_ID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROM_ID.id,"msg":i.message,'time':i.time,"date":i.date,"chat_id":i.id})

    obu=user_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.first_name,"photo":str(obu.photo.url),"user_lid":obu.LOGIN.id})



#/////////////////////////////// webservice ////////////////////////////////

def and_login_code(request):
    un = request.POST['uname']
    pw = request.POST['pswrd']

    users = login_table.objects.get(username = un, password = pw,type="user")
    if users is None:
        data = {"task" : "invalid"}
    else:
        data = {"task" : "valid","lid":users.id}
    l = json.dumps(data)
    return HttpResponse(l)



def user_regisration(request):
    first_name=request.POST['fname']
    last_name=request.POST['lname']
    age=request.POST['age']
    gender=request.POST['gender']
    image = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(image.name, image)
    address=request.POST['address']
    email=request.POST['email']
    weight=request.POST['weight']
    height=request.POST['height']
    username=request.POST['username']
    password=request.POST['password']

    log_obj = login_table()
    log_obj.username = username
    log_obj.password = password
    log_obj.type="user"
    log_obj.save()

    obj=user_table()
    obj.first_name=first_name
    obj.last_name=last_name
    obj.age=age
    obj.gender=gender
    obj.photo=fsave
    obj.address=address
    obj.email=email
    obj.weight=weight
    obj.height=height
    obj.LOGIN=log_obj
    obj.save()
    data = {'task': 'valid'}
    return JsonResponse(data)

def doc_rating1(request):
    user_id = request.POST['lid']
    doc_id = request.POST['did']
    rating = request.POST['rating']
    review = request.POST['review']
    obj=doctor_rating_table()
    obj.rating=rating
    obj.review=review
    obj.USER=user_table.objects.get(LOGIN_id=user_id)
    obj.DOCTOR=doctor_table.objects.get(id=doc_id)
    obj.date=datetime.now().today()
    obj.save()
    data = {'task': 'valid'}
    return JsonResponse(data)

def app_rating(request):
    user_id = request.POST['lid']
    rating = request.POST['rating']
    review = request.POST['review']
    obj=rating_table()
    obj.rating = rating
    obj.review = review
    obj.USER = user_table.objects.get(LOGIN_id=user_id)
    obj.date = datetime.now().today()
    obj.save()
    data = {'task': 'valid'}
    return JsonResponse(data)

def view_schedule(request):
    did=request.POST['did']
    ob = schedule_table.objects.filter(DOC_ID__id=did)
    data = []
    for i in ob:
        d = {"fromtime":str(i.from_time),"totime":str(i.to_time) , "date":str(i.date),"id":i.id}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)



def view_my_bookings(request):
    did=request.POST['lid']
    ob = booking_table.objects.filter(USER__LOGIN__id=did)
    data = []
    for i in ob:
        d = {"fromtime":str(i.SCHEDULE.from_time),"totime":str(i.SCHEDULE.to_time) , "date":str(i.SCHEDULE.date),"doc":i.SCHEDULE.DOC_ID.firstname+" "+i.SCHEDULE.DOC_ID.lastname,"status":i.status}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)





def view_doctor(request):
    ob = doctor_table.objects.all()
    data = []
    for i in ob:
        d = {"name":i.firstname +" "+i.lastname,"gender":i.gender,"email":i.email,"id":i.id,"qualification":i.qualification , "image":i.photo.url}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)



def view_doctor_search(request):
    name=request.POST['name']
    ob = doctor_table.objects.filter(firstname__istartswith=name)
    data = []
    for i in ob:
        d = {"name":i.firstname +" "+i.lastname,"gender":i.gender,"email":i.email,"id":i.id,"qualification":i.qualification , "image":i.photo.url}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)


def view_dietplan(request):
    did=request.POST['did']
    ob = dietplan_table.objects.filter(dietition__id=did)
    data = []
    for i in ob:
        d = {"BMI":i.BMI ,"Age":i.age , "Gender":i.gender , "Dietplan":i.dietplan}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)


def search_dietplan(request):
    did=request.POST['did']
    bmi=request.POST['bmi']
    ob = dietplan_table.objects.filter(dietition__id=did,BMI=bmi)
    data = []
    for i in ob:
        d = {"BMI":i.BMI ,"Age":i.age , "Gender":i.gender , "Dietplan":i.dietplan}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)



def prediction(request):
    print(request.POST)
    slvel=request.POST['slevel']
    gender=float(request.POST['gender'])
    age=float(request.POST['age'])
    urea=float(request.POST['urea'])
    cr=float(request.POST['cr'])
    hbalc=float(request.POST['hbalc'])
    cho=float(request.POST['chol'])
    tg=float(request.POST['tg'])
    hdl=float(request.POST['hdl'])
    ldl=float(request.POST['ldl'])
    vldl=float(request.POST['vldl'])
    bmi=float(request.POST['bmi'])
    print([gender,age,urea,cr,hbalc,cho,tg,hdl,ldl,vldl,bmi])
    ob=predict_fn([gender,age,urea,cr,hbalc,cho,tg,hdl,ldl,vldl,bmi])
    print(ob,"ggggggggggggggggggggggggggg")
    print(ob,"ggggggggggggggggggggggggggg")
    print(ob,"ggggggggggggggggggggggggggg")
    if ob==0:
        data = {"task": "No"}
    else:
        data = {"task": "Yes"}
    l = json.dumps(data)
    return HttpResponse(l)



def view_tip(request):
    print(request.POST,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    lid=request.POST['did']
    ob = tip_table.objects.filter(DIETITION__id=lid)
    data = []
    for i in ob:
        d = {"Tip":i.tips ,"Date":str(i.date) , "Time":str(i.time) }
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)


def view_dietitian(request):
    ob = dietitian_table.objects.all()
    data = []
    for i in ob:
        d = {"name":i.firstname +" "+i.lastname,"gender":i.gender,"email":i.email,"id":i.id,"qualification":i.qualification , "image":i.photo.url,"lid":i.LOGIN.id}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)




def view_dietitian_search(request):
    name=request.POST['name']
    ob = dietitian_table.objects.filter(firstname__istartswith=name)
    data = []
    for i in ob:
        d = {"name":i.firstname +" "+i.lastname,"gender":i.gender,"email":i.email,"id":i.id,"qualification":i.qualification , "image":i.photo.url,"lid":i.LOGIN.id}
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)



def send_doubt(request):
    lid=request.POST['lid']
    did=request.POST['did']
    doubt=request.POST['doubt']
    ob=doubt_table()
    ob.DOC_ID_id=did
    ob.UID=user_table.objects.get(LOGIN__id=lid)
    ob.doubt=doubt
    ob.reply="pending"
    ob.date=datetime.today()
    ob.save()
    data={"task":"valid"}
    l = json.dumps(data)
    return HttpResponse(l)



def view_doubt_reply(request):
    did=request.POST['did']
    lid=request.POST['lid']
    ob = doubt_table.objects.filter(DOC_ID__id=did,UID__LOGIN__id=lid)
    data = []
    for i in ob:
        d = {"doubt":i.doubt,"Date":str(i.date) , "reply":str(i.reply) }
        data.append(d)
    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)

def view_doubt_reply_search(request):
    did=request.POST['did']
    lid=request.POST['lid']
    date=request.POST['date']
    ob = doubt_table.objects.filter(DOC_ID__id=did,UID__LOGIN__id=lid,date=date)
    data = []
    for i in ob:
        d = {"doubt":i.doubt ,"Date":str(i.date) , "reply":str(i.reply) }
        data.append(d)

    print(data,"UUUUUUUUUUUUUUUUUUUUUU")
    l = json.dumps(data)
    return HttpResponse(l)


def booknow(request):
    lid=request.POST['lid']
    sid=request.POST['sid']
    ob=booking_table()
    ob.USER=user_table.objects.get(LOGIN__id=lid)
    ob.SCHEDULE_id=sid
    ob.status="booked"
    ob.time=datetime.now()
    ob.save()
    data={"task":"valid"}
    l = json.dumps(data)
    return HttpResponse(l)


def view_message2(request):
    print(request.POST)
    fromid=request.POST['fid']
    toid=request.POST['toid']
    mid=request.POST['lastmsgid']
    print(mid,"uuuuuuuuuuuu0")
    ob=chat_table.objects.filter(Q(TO_ID__id=toid,FROM_ID__id=fromid,id__gt=mid)|Q(TO_ID=fromid,FROM_ID=toid,id__gt=mid)).order_by('id')
    print(ob,"YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    data=[]
    print("++++++++==============================")
    print("++++++++==============================")
    print("++++++++==============================")
    for i in ob:
        r={"id":i.id,"date":i.date,"chat":i.message,"fromid":i.FROM_ID.id}
        data.append(r)
        print(r,"KKKKKKKKKKKKKKKKKKKKKKKKKKKK")
    # print(data,"JJJJJJJJJJJJJJJJJJJJJJJJJ")
    print(len(data),"=========================================")
    if len(data)>0:
        return JsonResponse({"status":"ok","res1":data})
    else:
        return JsonResponse({"status": "na"})



def in_message2(request):
    fromid = request.POST['fid']
    toid=request.POST['toid']
    chat = request.POST['msg']

    ob = chat_table()
    ob.message = chat
    ob.time = datetime.now().strftime("%H:%M:%S")
    ob.date = datetime.now()

    ob.FROM_ID = login_table.objects.get(id=fromid)
    ob.TO_ID = login_table.objects.get(id=toid)
    ob.save()
    data = {"status": "send"}
    r = json.dumps(data)

    print(r)
    return HttpResponse(r)