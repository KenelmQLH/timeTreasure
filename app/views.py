from django.shortcuts import HttpResponse, render, redirect
from app.models import *
import json

def login(request):
    if request.method == "GET":
        return render(request, 'login.html', {'flag': 1})  # 0/1用于判断
    else:
        # POST
        func = request.POST.get("func")
        
        u = request.POST.get("usr")
        p = request.POST.get("pwd")
        print(" ----------------register func-------------------")
        if func == "register":
            p2 = request.POST.get("pwd_confirm")
            phone = request.POST.get("phone")
            code = request.POST.get("code")
            try:
                Users.objects.create(
                    uname=u,
                    password=p,
                )
                print(".........in add user: uname = ",u)
            except Exception as e:
                print("!" * 50)
                return redirect('/login/', {'flag': 1})
        
        print(" ----------------login func-------------------")
        print(u,p)
        # u = 'qinlonghu'
        # p = 'QLH765qlh'
        results = Users.objects.filter(uname=u, password=p)
        if not results:
            # 查询为空则返回
            return render(request, 'login.html', {'flag': 0})

        return_id = results[0].uid
        print(" ----------------YES!-------------------")
        print("return_id = " + str(return_id))
        return redirect('/index/'+str(return_id), {'uid': return_id})


def index_projects(request, uid):
    if request.method == "GET":
        # uid = request.GET.get("uid")
        # 两种方式
        # u_obj = Users.objects.get(uid=uid)
        # results = u_obj.projects_set.all()
        results = Projects.objects.filter(users__uid=uid)
        project_list = []

        print('*'*50)
        print(results)
        for p in results:
            ele = {
                "pid": p.pid,
                "pname": p.pname,
                "ptime": p.ptime.to_integral,
            }
            project_list.append(ele)
            print(ele)
        print('*' * 50)
        info = {
            'project_list': project_list,
            'uid': uid,
        }
        return render(request, 'index.html', info)
    else:
        return render(request, 'index.html')


def add_project(request):
    uid = request.POST.get("uid")
    pname = request.POST.get("pname")
        
    ret = {'status': False, 'message': "项目名称不能为空"} 
    
    if pname == None or pname=="" :
        return HttpResponse(json.dumps(ret))
    
    # 此处应该加入项目判断
    # if else
    ret = {'status': True, 'message': "ok"} 
    
    try:
        Projects.objects.create(
            pname=pname,
            users_id=uid,
        )
        print(".........in add project: uid = ",uid)
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))



def deleteproject(request):
    # uid = int(request.GET.get("uid"))
    pid = int(request.POST.get("pid"))
    ret = {'status': True, 'message': None}
    try:
        Projects.objects.filter(pid=pid).delete()
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


def index_subprojects(request,uid,pid):
    if request.method == "GET":
        print("in sub_index ~~~", pid, "~~~")
        results = Subprojects.objects.filter(projects_id=pid)
        subproject_list = []

        print('*' * 50)
        print(results)
        for p in results:
            p.sptime = p.sptime / 60
            # print("......",p.sptime,type(p.sptime))
            ele = {
                "spid": p.spid,
                "spname": p.spname,
                # 以小时显示
                "sptime": p.sptime.to_integral,
                "numrecord":p.numrecord,
            }
            subproject_list.append(ele)
            print(ele)
        print('*' * 50)
        info = {
            'subproject_list': subproject_list,
            'pid': pid,
            'uid':uid,
        }
        return render(request, 'index_subprojects.html', info)
    else:
        return render(request, 'index_subprojects.html')

def add_subproject(request):
    pid = request.POST.get("pid")
    spname = request.POST.get("spname")
    # 此处应该加入项目判断
    # if else
    ret = {'status': True, 'message': None}
    
    if spname == None or spname=="" :
        return HttpResponse(json.dumps(ret))

    ret = {'status': True, 'message': "ok"} 
    try:
        Subprojects.objects.create(
        spname=spname,
        projects_id=pid,
        )
        print("in add subproject: pid = ",pid)
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


def del_subproject(request):
    # uid = int(request.GET.get("uid"))
    spid = int(request.POST.get("spid"))
    ret = {'status': True, 'message': None}
    try:
        Subprojects.objects.filter(spid=spid).delete()
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


def add_record(request):
    spid = int(request.POST.get("spid"))
    # 按照分钟来存储
    rtime = int(request.POST.get("ms")) / 60000
    print("in adding time: ", rtime,type(rtime))
    ret = {'status': True, 'message': None}
    try:
        Records.objects.create(
        rtime = rtime,
        subprojects_id=spid,
        )
        obj = Subprojects.objects.get(spid=spid)
        obj.sptime = int(obj.sptime) + rtime
        obj.numrecord = int(obj.numrecord) + 1
        obj.save()
    
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))

