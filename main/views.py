from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from main.models import *
import os
import hashlib
import json
import ast


# Create your views here.
def index(request):
    return render(request,'main/index.html')

def inputForm(request):
    common = Common.objects.all()
    content = {'documents':common}
    return render(request,'main/inputForm.html',content)

def SearchForm(request):
    common = Common.objects.all()
    content = {'documents':common}
    return render(request,'main/SearchForm.html',content)

def SearchFormAjax(request):
    #rows = User.objects.filter(name='김원식')
    #rows = User.objects.filter(name=r'원')
    try:
        users = User.objects.all()
        
        sabun = request.GET.get('sabun','')
        name = request.GET.get('name','')
        pos_gbn_code = request.GET.get('pos_gbn_code','')
        join_day = request.GET.get('join_day','')
        retire_day = request.GET.get('retire_day','')
        join_gbn_code = request.GET.get('join_gbn_code','')
        put_yn = request.GET.get('put_yn','')
        job_type = request.GET.get('job_type','')

        if sabun:
            users = users.filter(sabun=sabun)
        if name:
            users = users.filter(name__regex=r'('+name+')')
        if pos_gbn_code:
            users = users.filter(pos_gbn_code = pos_gbn_code)
        if join_day:
            join_day = join_day[:4]+'-'+join_day[4:6]+'-'+join_day[6:8]
            users = users.filter(join_day = join_day)
        if retire_day:
            retire_day = retire_day[:4]+'-'+retire_day[4:6]+'-'+retire_day[6:8]
            users = users.filter(retire_day = retire_day)
        if join_gbn_code:
            users = users.filter(join_gbn_code = join_gbn_code)
        if put_yn:
            users = users.filter(put_yn = put_yn)
        if job_type:
            users = users.filter(job_type = job_type)



        # sabun_regex = request.GET['sabun']
        # if sabun_regex!='' or name_regex!='':
        #     rows = User.objects.filter(sabun__regex=r'('+sabun_regex+'|'+name_regex+'|word3)')
        print(users)
        raw_data = serializers.serialize('python', users)
    except:
        print(4)
        raw_data = serializers.serialize('python', User.objects.all())
    

    # this gives you a list of dicts
    # now extract the inner `fields` dicts
    actual_data = [d['fields'] for d in raw_data]
   
    # and now dump to JSON
    output = json.dumps(actual_data)

    testarray = ast.literal_eval(output)

    return JsonResponse(testarray,safe=False)
 

def loginView(request):
    return render(request, 'main/login.html')

def login(request):

    if 'user_id' in request.session.keys():
        return redirect('main_index')
    user_input_id = request.POST['loginEmail']
    user_input_pw = request.POST['loginPW']
    try:
        user = User.objects.get(user_id = user_input_id)
        encoded_userPW = user_input_pw.encode()
        encrypted_userPW = hashlib.sha256(encoded_userPW).hexdigest()

        if encrypted_userPW == user.user_pw:
            request.session['user_id'] = user.user_id
            request.session['user_name'] = user.user_name
            return redirect('main_index')
        else:
            return redirect('main_loginView')

    except ObjectDoesNotExist:
        message = '이메일이 존재하지 않습니다.'
        return render(request, 'main/error.html', { "message": message })

    except:
        message = '알 수 없는 오류가 발생하였습니다.'
        return render(request, 'main/error.html', { "message": message })

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect('main_loginView')

def download(request):
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/liquid; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response

    else:
        message = '알 수 없는 오류가 발생하였습니다.'
        return render(request, 'main/error.html', { "message": message })

def register(request):
    file = request.FILES.get('uploadFile')
    try:
        sabun = int(User.objects.latest("id").id)+1
    except User.DoesNotExist:
        sabun = 1
    #sabun = request.POST['SABUN']
    join_day = request.POST['JOIN_DAY']
    retire_day = request.POST['RETIRE_DAY']
    put_yn = request.POST['PUT_YN']
    name = request.POST['NAME']
    reg_no = request.POST['REG_NO']
    eng_name = request.POST['ENG_NAME']
    phone = request.POST['PHONE']
    hp = request.POST['HP']
    pos_gbn_code = request.POST['POS_GBN_CODE']
    cmp_reg_no = request.POST['CMP_REG_NO']
    crm_name = request.POST['CRM_NAME']
    sex = request.POST['SEX']
    if(request.POST['YEARS']!=''):
        years = request.POST['YEARS']
    else:
        years = 0
    email = request.POST['EMAIL']
    zip = request.POST['ZIP']
    addr1 = request.POST['ADDR1']
    addr2 = request.POST['ADDR2']
    dept_code = request.POST['DEPT_CODE']
    join_gbn_code = request.POST['JOIN_GBN_CODE']
    user_id = request.POST['ID']
    pwd = request.POST['PWD']
    if(request.POST['SALARY']!=''):
        salary = int(request.POST['SALARY'].replace(',',''))
    else:
        salary = 0
    kosa_reg_yn = request.POST['KOSA_REG_YN']
    kosa_class_code = request.POST['KOSA_CLASS_CODE']
    mil_yn = request.POST['MIL_YN']
    mil_type = request.POST['MIL_TYPE']
    mil_level = request.POST['MIL_LEVEL']
    mil_startdate = request.POST['MIL_STARTDATE']
    mil_enddate = request.POST['MIL_ENDDATE']
    job_type = request.POST['JOB_TYPE']
    gart_level = request.POST['GART_LEVEL']
    user = User(sabun=sabun, join_day=join_day, retire_day=retire_day, put_yn = put_yn, name=name, reg_no=reg_no, eng_name=eng_name, phone=phone, hp=hp, pos_gbn_code = pos_gbn_code, cmp_reg_no = cmp_reg_no, sex =sex, years=years, email=email, zip=zip, addr1=addr1, addr2=addr2, dept_code= dept_code, join_gbn_code = join_gbn_code, user_id = user_id, pwd=pwd, salary=salary, kosa_reg_yn = kosa_reg_yn, kosa_class_code=kosa_class_code, mil_yn =mil_yn, mil_type = mil_type, mil_level =mil_level, mil_startdate= mil_startdate, mil_enddate=mil_enddate, job_type=job_type, gart_level=gart_level, crm_name=crm_name)
    user.save()
    return render(request,'main/index.html')

def idchk(request):
    try:  
        user = User.objects.get(user_id=request.GET['user_id'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)

def updateForm(request):
    common = Common.objects.all()
    user = User.objects.get(sabun=request.GET['sabun'])
    try:
        profile = Profilea.objects.get(upload_id =user.id, file_name=user.profile)
    except Exception as e:
        profile = None

    try:
        cmp_reg_image = Cmp_reg_imagea.objects.get(upload_id =user.id, file_name=user.cmp_reg_image)
    except Exception as e:
        cmp_reg_image = None

    try:
        carrier = Carriera.objects.get(upload_id =user.id, file_name=user.carrier)
    except Exception as e:
        carrier = None
        
        
        
   
    content = {'documents':common, 'documents2':user, 'profile':profile, 'cmp_reg_image':cmp_reg_image, 'carrier':carrier}
    return render(request,'main/UpdateForm.html',content)

def update(request):
    
    user = User.objects.get(sabun=request.POST['SABUN'])
    try:
        if request.FILES.getlist('uploadFile')[0]:
            print(16,request.FILES.getlist('uploadFile')[0])
            user_file = request.FILES.getlist('uploadFile')[0]
            origin_file_name = user_file.name
            now_HMS = datetime.today().strftime('%H%M%S')
            file_upload_name = now_HMS+'_'+origin_file_name
            user_file.name = file_upload_name
            user.profile=file_upload_name
            profile = Profilea(file_path=user_file, file_name=file_upload_name, upload_id=user)
            profile.save()
            print('profile 첨부 됨')
    
    except Exception as e:
        print('profile 첨부 안됨')

    try:
        if request.FILES.getlist('uploadFile2')[0]:
            user_file = request.FILES.getlist('uploadFile2')[0]
            origin_file_name = user_file.name
            now_HMS = datetime.today().strftime('%H%M%S')
            file_upload_name = now_HMS+'_'+origin_file_name
            user_file.name = file_upload_name
            user.cmp_reg_image=file_upload_name
            cmp_reg_image = Cmp_reg_imagea(file_path=user_file, file_name=file_upload_name, upload_id=user)
            cmp_reg_image.save()
            print('사업자등록증 첨부 됨')

    except Exception as e:
        print('사업자등록증 첨부안됨')

    try:
        if request.FILES.getlist('uploadFile3')[0]:
            user_file = request.FILES.getlist('uploadFile3')[0]
            origin_file_name = user_file.name
            now_HMS = datetime.today().strftime('%H%M%S')
            file_upload_name = now_HMS+'_'+origin_file_name
            user_file.name = file_upload_name
            user.carrier=file_upload_name
            carrier = Carriera(file_path=user_file, file_name=file_upload_name, upload_id=user)
            carrier.save()
            print('이력서 첨부 됨')

    except Exception as e:
        print('이력서 첨부 안됨')

    user.name = request.POST['NAME']
    user.join_day = request.POST['JOIN_DAY']
    user.retire_day = request.POST['RETIRE_DAY']
    user.put_yn = request.POST['PUT_YN']
    user.name = request.POST['NAME']
    user.reg_no = request.POST['REG_NO']
    user.eng_name = request.POST['ENG_NAME']
    user.phone = request.POST['PHONE']
    user.hp = request.POST['HP']
    user.pos_gbn_code = request.POST['POS_GBN_CODE']
    user.cmp_reg_no = request.POST['CMP_REG_NO']
    user.sex = request.POST['SEX']
    if(request.POST['YEARS']!=''):
        user.years = request.POST['YEARS']
    else:
        user.years = 0
    user.email = request.POST['EMAIL']
    user.zip = request.POST['ZIP']
    user.addr1 = request.POST['ADDR1']
    user.addr2 = request.POST['ADDR2']
    user.dept_code = request.POST['DEPT_CODE']
    user.join_gbn_code = request.POST.get('JOIN_GBN_CODE',False)
    user.user_id = request.POST['ID']
    user.pwd = request.POST['PWD']
    if(request.POST['SALARY']!=''):
        user.salary = int(request.POST['SALARY'].replace(',',''))
    else:
        user.salary = 0
    user.kosa_reg_yn = request.POST['KOSA_REG_YN']
    user.kosa_class_code = request.POST['KOSA_CLASS_CODE']
    user.mil_yn = request.POST.get('MIL_YN',False)
    user.mil_type = request.POST.get('MIL_TYPE',False)
    user.mil_level = request.POST.get('MIL_LEVEL', False)
    user.mil_startdate = request.POST['MIL_STARTDATE']
    user.mil_enddate = request.POST['MIL_ENDDATE']
    user.job_type = request.POST['JOB_TYPE']
    user.gart_level = request.POST['GART_LEVEL']
    user.crm_name = request.POST['CRM_NAME']
    user.save()
    return render(request,'main/SearchForm.html')

	
