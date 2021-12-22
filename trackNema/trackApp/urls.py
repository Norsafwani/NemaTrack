from django.urls import path, include, re_path
from django.views.generic import TemplateView
from trackApp import views
from trackApp.controller import usercontroller, nemacontroller

urlpatterns = [

    #First Page = Login Page
    # path("",views.indexhome, name="indexhome"),567
    # path('',views.indexhome),

    path('', views.index),
    path('home', usercontroller.home, name="home"),

    # #NEMA DATA 
    # path ('indexnema', nemacontroller.indexnema),

    #INDEX
    path ('indexnema',nemacontroller.indexnema, name='indexnema'),

    #ADD NEW
    path ('nemacreate', nemacontroller.nemacreate),

    #SUBMIT ADD NEW
    path('submitnema',nemacontroller.submitnema),

    #DELETE 
    path ('deletenema/<int:id>', nemacontroller.deletenema),

    #UPDATE
    path('updatenema/<int:id>',nemacontroller.updatenema),

    #UPDATE SUBMIT
    path('updatesubmitnema',nemacontroller.updatesubmitnema),

    #SEARCH 
    path('searchnema',nemacontroller.searchnema),

    #LOGIN
    path('submit_login', usercontroller.submit_login),

    #LOGOUT
    path('logout_nema',usercontroller.logout_nema),

    #VIEW
    path('viewnema/<int:id>',nemacontroller.viewnema),
    
    #SUBMIT ADD TRY NEMA2
    path('submitnema2',nemacontroller.submitnema2),

    #RETURN FORM NEMA
    path('returnformnema/<int:id>',nemacontroller.returnformnema),

    #SUBMIT ADD TRY NEMA2
    path('submitreturnform',nemacontroller.submitreturnform),

    #RETURN FORM LIST
    path ('return_nema',nemacontroller.return_nema, name='return_nema'),

    # #RETURN FORM LIST
    # path ('upload_return',nemacontroller.upload_return, name='upload_return'),

    # #RETURN FORM LIST
    # path ('indexnematry',nemacontroller.indexnematry, name='indexnematry'),

    #UPLOAD EXCEL mslhnye....
    # path ('upload_excel',nemacontroller.upload_excel, name='upload_excel'),

    #UPLOAD FILE
    path ('my_view',nemacontroller.my_view, name='my_view'),

    #UPLOAD FILE(2)
    path ('form_upload',nemacontroller.form_upload, name='form_upload'),

    #Try UnixTime
    path ('trydate',nemacontroller.trydate, name='trydate'),
    path ('createdate',nemacontroller.createdate, name='createdate'),


]
