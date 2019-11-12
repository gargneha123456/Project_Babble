# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import student, group, group_members
from queries.models import query
from announcements.models import Announcement
from datetime import datetime
from django.shortcuts import render, redirect
from events.models import event
from polls.models import poll
from resources.models import resource, subject

def login_view(request):
    if request.method == "GET":
        return render(request,'authenticate/login.html')
    if request.method == "POST":
        un = request.POST.get('username')

        pw = request.POST.get('pass')

        exist = student.objects.filter(SID = un ).exists()

        if exist:
            ob = student.objects.get(SID=un)
            if ob.Password == pw :

                if ob.Last_Login is None:
                    ob.Last_Login = datetime.now()
                    ob.save()
                    return redirect('/newuser/')
                else:
                    ob.Last_Login = datetime.now()
                    ob.save()
                    request.session['sid'] = ob.SID
                    return redirect('/dashboard/')

        return render(request,'authenticate/do.html')


def new_view(request):
    if request.method == "GET":
        return render(request, 'authenticate/new.html')
    if request.method == "POST":
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        print(p1)
        print(p2)
        sid = request.session['sid']
        ins = student.objects.get(SID=sid)
        if p1 == p2:
            ins.Password = p1
            ins.save()
            print('yes')
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        email = request.POST.get('email')
        pno = request.POST.get('phone_number')
        print(pno)
        print(fn)
        print(ln)
        print(email)

        ins.Name = fn + ' ' + ln
        ins.Email = email
        ins.Contact = pno
        ins.save()
        return redirect('/dashboard/')



def home_view(request):

    sid = request.session['sid']
    instance = student.objects.get(SID=sid)
    queries = query.objects.all()
    groups = group.objects.all()
    polls = poll.objects.all()
    announcements = Announcement.objects.all()
    members = group_members.objects.filter(SID= sid)
    if request.method == 'POST':
        a = request.POST.get('xyz')
        b = request.POST.get('sub')
        obj = query(Asker=instance,Content=a,Timestamp=datetime.now(),Subject=b )
        obj.save()

    return render(request,'authenticate/dashboard.html', { "instance": instance,"queries":queries, "groups":groups, "announcements":announcements,"polls":polls,"members":members})

def file_view(request):
    sid = request.session['sid']
    instance = student.objects.get(SID=sid)
    members = group_members.objects.filter(SID=sid)
    announcements = Announcement.objects.all()
    groups = group.objects.all()
    resources = resource.objects.all()
    subjects = subject.objects.all()
    return render(request,'authenticate/resources.html',{"instance": instance,"groups":groups,"announcements":announcements,"members":members,"resources":resources,"subjects":subjects})

def profile_view(request):
    groups = group.objects.all()
    sid = request.session['sid']
    instance = student.objects.get(SID=sid)
    members = group_members.objects.filter(SID=sid)
    announcements = Announcement.objects.all()
    return render(request,'authenticate/profile.html',{"groups":groups,"instance":instance,"announcements":announcements,"members":members})

def setting_view(request):
    sid = request.session['sid']
    instance = student.objects.get(SID=sid)
    groups = group.objects.all()
    members = group_members.objects.filter(SID=sid)
    announcements = Announcement.objects.all()
    return render(request,'authenticate/setting.html',{"instance":instance,"groups":groups,"announcements":announcements,"members":members})

def group_view(request, pk):
    groups = group.objects.all()
    sid = request.session['sid']
    instance = student.objects.get(SID=sid)
    grp = group.objects.get(Name = pk)
    events = event.objects.filter(GID = grp)
    announcements = Announcement.objects.filter(GID=grp)
    polls = poll.objects.filter(GID=grp)
    members = group_members.objects.filter(SID=instance,GID=grp)

    return render(request,'authenticate/group.html',{"instance":instance,"groups":groups,"events":events,"announcements":announcements,"polls":polls,"members":members})

def myqueries(request):
    sid = request.session['sid']
    instance = student.objects.get(SID=sid)
    members = group_members.objects.filter(SID=sid)
    announcements = Announcement.objects.all()
    groups = group.objects.all()
    queries = query.objects.filter(Asker=sid)
    return render(request, 'authenticate/myqueries.html',{"instance": instance, "groups": groups, "announcements": announcements, "members": members,"queries":queries})