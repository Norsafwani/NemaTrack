from django.urls import path, include, re_path
from django.views.generic import TemplateView
from trackApp import views
from trackApp.controller import usercontroller, nemacontroller

urlpatterns = [

    #First Page = Login Page
    # path("",views.indexhome, name="indexhome"),567
    path("", views.home, name="home"),
    # path('',views.indexhome),

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

    #UPDATESUBMIT
    path('updatesubmitnema',nemacontroller.updatesubmitnema),

    #SEARCH 
    path('searchnema',nemacontroller.searchnema),

    #LOGIN
    path('submit_login', usercontroller.submit_login),

    #LOGOUT
    path('logout_nema',usercontroller.logout_nema),

    #VIEW
    path('viewnema/<int:id>',nemacontroller.viewnema),
    
    # SUBMIT ADD TRY NEMA2
    path('submitnema2',nemacontroller.submitnema2),

    #RETURN FORM NEMA
    path('returnformnema/<int:id>',nemacontroller.returnformnema),

    #SUBMIT ADD TRY NEMA2
    path('submitreturnform',nemacontroller.submitreturnform),




]