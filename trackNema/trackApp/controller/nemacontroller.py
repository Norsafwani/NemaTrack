# Create your views here. where all the functions lies
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import date, datetime
from trackApp.models import AuthUser, AuthPermission
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout, authenticate, login
from django.core.files.storage import FileSystemStorage
from trackApp.models import Nema2, Nemareturnform

#Function for html create new Nema
def nemacreate(request):
    return render(request,'nema/nema_create.html',{})

#Function for Display Nema Data
def indexnema(request):
    nema = Nema2.objects.all()
    # print('print this', product)
    content = {
        'nema':nema,
    }
    return render(request, 'nema/nema_data.html', content)

#Function Submit Create New Nema
def submitnema(request):
    # id = request.session['id']
    # if request.session._session:
        if request.method=='POST':
            nema_id = request.POST['id']
            devui_no = request.POST['devui']
            appkey = request.POST['app_key']
            shipdatereceived = request.POST['ship_date_received']
            siteinstalldate = request.POST['site_install_date']
            datedeliver = request.POST['date_deliver']           
            lightsolname = request.POST['lightsol_name']           
            licenseactivedate = request.POST['license_active_date']          
            licenseexpireddate = request.POST['license_expired_date']          
            contractorname = request.POST['contractor_name']           
            endclientname = request.POST['end_client_name']           
            projecttendername = request.POST['project_tender_name']           
            donumber = request.POST['do_number']            
            remarks = request.POST['remarks']

            # For insert into database
            # object = nama model( namacolumn=nama variable, others - if any)
            track = Nema2(id= nema_id, devui=devui_no, app_key=appkey, ship_date_received=shipdatereceived, site_install_date= siteinstalldate, 
            date_deliver=datedeliver, lightsol_name = lightsolname, license_active_date=licenseactivedate, license_expired_date= licenseexpireddate,
            contractor_name= contractorname,  end_client_name= endclientname, project_tender_name= projecttendername, 
            do_number= donumber, remarks= remarks )
            track.save()
            return redirect('/nema')

# Function for Submit Nema2
def submitnema2(request):
    # id = request.session['id']
    if request.method=='POST':
        # nema_id = request.POST['id']
        # devnames = request.POST['devname']
        devui_no = request.POST['devui']
        appkey = request.POST['app_key']
        shipdatereceived = request.POST['ship_date_received']
        # shipdatereceived = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        siteinstalldate = request.POST['site_install_date'] 
        datedeliver = request.POST['date_deliver']
        lightsolname = request.POST['lightsol_name']  
        licenseactivedate = request.POST['license_active_date']  
        licenseexpireddate = request.POST['license_expired_date'] 
        contractorname = request.POST['contractor_name']   
        endclientname = request.POST['end_client_name']         
        projecttendername = request.POST['project_tender_name']       
        donumber = request.POST['do_number']            
        remarks = request.POST['remarks']
       
            # For insert into database -- , id= nema_id,
            # object = nama model( namacolumn=nama variable, others - if any)
        # track = Nema2( devname=devnames )
        track = Nema2(devui=devui_no, app_key=appkey, ship_date_received=shipdatereceived, site_install_date= siteinstalldate, 
            date_deliver=datedeliver, lightsol_name = lightsolname, license_active_date=licenseactivedate, license_expired_date= licenseexpireddate,
            contractor_name= contractorname,  end_client_name= endclientname, project_tender_name= projecttendername, 
            do_number= donumber, remarks= remarks )
        track.save()
    return redirect('/nema')
       

#Function for Delete Nema Data
def deletenema(request, id):
    deleteN = Nema2.objects.get(id=id)
    deleteN.delete()
    # success_url = reverse_lazy('indexproduct')
    return redirect('/indexnema')

#Function for Update Nema Data
def updatenema(request,id):
    nema = Nema2.objects.get(id=id)
    obj = {
        'nema': nema,
    }
    return render(request, 'nema/nema_update.html', obj)

#Funtion for Submit Update Nema Data
def updatesubmitnema(request):
    if request.method == "POST":
        # user_id = request.session['user_id']
        # now = datetime.now() 
        # id = request.POST['id']
        id = request.POST['id']
        devui_no = request.POST['devui']       
        appkey = request.POST['app_key']
        shipdatereceived = request.POST['ship_date_received']
        siteinstalldate = request.POST['site_install_date']
        datedeliver = request.POST['date_deliver']         
        lightsolname = request.POST['lightsol_name']      
        licenseactivedate = request.POST['license_active_date']      
        licenseexpireddate = request.POST['license_expired_date']       
        contractorname = request.POST['contractor_name']      
        endclientname = request.POST['end_client_name']   
        projecttendername = request.POST['project_tender_name']     
        donumber = request.POST['do_number']    
        remarks = request.POST['remarks']
             
        # print(devui)
        nema = Nema2.objects.get(id=id)
        nema.devui = devui_no
        nema.app_key = appkey
        nema.ship_date_received = shipdatereceived
        nema.site_install_date = siteinstalldate
        nema.date_deliver = datedeliver
        nema.lightsol_name = lightsolname
        nema.license_active_date = licenseactivedate
        nema.license_expired_date = licenseexpireddate
        nema.contractor_name = contractorname
        nema.end_client_name = endclientname
        nema.project_tender_name = projecttendername
        nema.do_number = donumber
        nema.remarks = remarks
        # nema.date_modified = now
        # nema.modified_by = user_id
        nema.save()
    return redirect('/nema')

#Function for Searching 
def searchnema(request):
    # global nemas
    if request.method == "POST":
        searchNema =  request.POST['searchNema'] 
        #nemas(Return search result)
        nemas = Nema2.objects.filter(devui__contains=searchNema)
        nemas2 = Nema2.objects.filter(app_key__contains=searchNema)

        # app_key__contains=searchNema
        obj = {
        'searchNema': searchNema,
        'nemas': nemas,
        'nemas2': nemas2,
        }

        return render(request, 'nema/nema_search.html', obj)
    else:
        return render(request, 'nema/nema_search.html', {})

#Function for html create new Nema
# def nemacreate(request):
#     return render(request,'nema/nema_create.html',{})

#Function fo view 1 specific Nema
def viewnema(request,id):
    # admin = ''
    objnema = Nema2.objects.get(id=id)
    obj = {
        'objnema': objnema
    }
    return render(request, 'nema/nema_view.html', obj)

#Function fo Return Form Nema
def returnformnema(request,id):
    # admin = ''
    objnema2 = Nema2.objects.get(id=id)
    obj = {
        'objnema2': objnema2
    }
    return render(request, 'nema/nema_form.html', obj)

#Function Submit Return Form
def submitreturnform(request):
    # id = request.session['id']
        if request.method=='POST':
            date_uninstall = request.POST['dateuninstall']
            date_detect = request.POST['datedetect']      
            profdescribe = request.POST['prof_describe']          
            # proofvideo = request.POST['proof_video'] --proof_video = proofvideo,
            nosiri = request.POST['no_siri']
            document = request.POST['documents'] 
            # For insert into database
            # object = nama model( namacolumn=nama variable, others - if any)
            form = Nemareturnform(dateuninstall=date_uninstall, datedetect=date_detect, 
            prof_describe=profdescribe, no_siri=nosiri, documents=document)
            form.save()
            return render(request, 'nema/nema_form.html', {})

#Function for upload File (File System Storage)
def fileupload(request):
    if request.method == 'POST' and request.FILES['documents']:
        documents = request.FILES['documents']
        fs = FileSystemStorage()
        filename = fs.save(product_file.name, product_file)
        uploaded_file_url = fs.url(filename)

        return render(request, 'nema_form.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'product/createproduct.html')

# #Function for Upload Files & Images
# def form_upload(request):
#     if request.method == 'POST':
#         form = Nemareturnform(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('nema')
#     else:
#         form = Nemareturnform()
#     return render(request, 'nema/nema_form.html', {
#         'form': form
#     })

#Function for Display Return Nema [List]
def return_nema(request):
    returnnema = Nemareturnform.objects.all()
    # print('print this', product)
    content = {
        'returnnema':returnnema,
    }
    return render(request, 'nema/return_form_list.html', content)

#TRY UPLOAD - MODEL - Document
#Function for Display Return Nema [List]
def return_nema(request):
    returnnema = Nemareturnform.objects.all()
    # print('print this', product)
    content = {
        'returnnema':returnnema,
    }
    return render(request, 'nema/return_form_list.html', content)

def upload_return(request):
    return render(request,'nema/nema_form.html',{})
    