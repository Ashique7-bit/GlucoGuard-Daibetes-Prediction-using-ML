"""Gluco_Gaurd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from GG_App import views

urlpatterns = [
    path('',views.logincc,name='logincc'),
    path('login_code',views.login_code,name='login_code'),
    path('man_dietitian',views.man_dietitian,name='man_dietitian'),
    path('add_dietitian',views.add_dietitian,name='add_dietitian'),
    path('man_doc',views.man_doc,name='man_doc'),
    path('add_doc',views.add_doc,name='add_doc'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('doc_rating',views.doc_rating,name='doc_rating'),
    path('Rating_review',views.Rating_review,name='Rating_review'),
    path('man_dietplan',views.man_dietplan,name='man_dietplan'),
    path('add_dietplan',views.add_dietplan,name='add_dietplan'),
    path('man_tip',views.man_tip,name='man_tip'),
    path('add_tip',views.add_tip,name='add_tip'),
    path('dietitian_home',views.dietitian_home,name='dietitian_home'),
    path('man_schedule',views.man_schedule,name='man_schedule'),
    path('add_schedule',views.add_schedule,name='add_schedule'),
    path('doc_home',views.doc_home,name='doc_home'),
    path('doubt',views.doubt,name='doubt'),
    path('reply/<int:id>',views.reply,name='reply'),
    path('logout',views.logout,name='logout'),
    path('add_new_dietitian',views.add_new_dietitian,name='add_new_dietitian'),
    path('edit_dietitian/<int:id>',views.edit_dietitian,name='edit_dietitian'),
    path('edit_doc/<int:id>',views.edit_doc,name='edit_doc'),
    path('edited_diet',views.edited_diet,name='edited_diet'),
    path('edited_doc',views.edited_doc,name='edited_doc'),
    path('delete_dietitian/<int:id>',views.delete_dietitian,name='delete_dietitian'),
    path('delete_doctor/<int:id>',views.delete_doctor,name='delete_doctor'),
    path('add_new_doc',views.add_new_doc,name='add_new_doc'),
    path('Rating_review_search',views.Rating_review_search,name='Rating_review_search'),
    path('schedule_code',views.schedule_code,name='schedule_code'),
    path('edit_schedule/<int:id>',views.edit_schedule,name='edit_schedule'),
    path('update_schedule',views.update_schedule,name='update_schedule'),
    path('delete_schedule/<int:id>',views.delete_schedule,name='delete_schedule'),
    path('delete_dietplan/<int:id>',views.delete_dietplan,name='delete_dietplan'),
    path('dietplan',views.dietplan,name='dietplan'),
    path('man_tip',views.man_tip,name='man_tip'),
    path('add_dietplan',views.add_dietplan,name='add_dietplan'),
    path('add_dietplancode',views.add_dietplancode,name='add_dietplancode'),
    path('searchdate',views.searchdate,name='searchdate'),
    path('add_tipcode',views.add_tipcode,name='add_tipcode'),
    path('edit_tip/<int:id>',views.edit_tip,name='edit_tip'),
    path('edit_tipcode',views.edit_tipcode,name='edit_tipcode'),
    path('delete_tip/<int:id>',views.delete_tip,name='delete_tip'),
    path('man_doubt',views.man_doubt,name='man_doubt'),
    path('schedule_search',views.schedule_search,name='schedule_search'),
    path('doubt_search',views.doubt_search,name='doubt_searchf'),
    path('send_reply',views.send_reply,name='send_reply'),
    path('dietitian_search',views.dietitian_search,name='dietitian_search'),
    path('doc_search',views.doc_search,name='doc_search'),
    path('edit_dietplan/<int:id>',views.edit_dietplan,name='edit_dietplan'),
    path('edit_dietplancode',views.edit_dietplancode,name='edit_dietplancode'),



    path('view_doubt_reply_search',views.view_doubt_reply_search,name='view_doubt_reply_search'),



    path('chatwithuser', views.chatwithuser, name='chatwithuser'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),



    path('user_regisration', views.user_regisration, name='user_regisration'),
    path('and_login_code', views.and_login_code, name='and_login_code'),
    path('doc_rating1', views.doc_rating1, name='doc_rating1'),
    path('app_rating', views.app_rating, name='app_rating'),
    path('view_schedule', views.view_schedule, name='view_schedule'),
    path('view_doctor', views.view_doctor, name='view_doctor'),
    path('view_dietplan', views.view_dietplan, name='view_dietplan'),
    path('view_tip', views.view_tip, name='view_tip'),
    path('view_dietitian', views.view_dietitian, name='view_dietitian'),
    path('send_doubt', views.send_doubt, name='send_doubt'),
    path('view_doubt_reply', views.view_doubt_reply, name='view_doubt_reply'),
    path('view_doubt_reply_search', views.view_doubt_reply_search, name='view_doubt_reply_search'),
    path('booknow', views.booknow, name='booknow'),
    path('in_message2', views.in_message2, name='in_message2'),
    path('view_message2', views.view_message2, name='view_message2'),
    path('search_dietplan', views.search_dietplan, name='search_dietplan'),
    path('view_doctor_search', views.view_doctor_search, name='view_doctor_search'),
    path('view_dietitian_search', views.view_dietitian_search, name='view_dietitian_search'),
    path('prediction', views.prediction, name='prediction'),
    path('view_my_bookings', views.view_my_bookings, name='view_my_bookings'),


]
