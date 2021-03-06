from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse
import calendar
import datetime

from .models import Routine, Routine_comment, Routine_detail
# Create your views here

#메인 달력 화면
def main(request):
    # 현재 년도, 월 가져오기
    Now = datetime.datetime.now()
    year = Now.year
    month = Now.month
    
    # 캘린더 구현
    mycal = calendar.HTMLCalendar(calendar.SUNDAY)
    mycalendar = mycal.formatmonth(year, month)
    
    template = loader.get_template('diarys/main.html')
    context = {
        "mycalendar": mycalendar,
        
    }
    return HttpResponse(template.render(context, request))

def index2(request):
    if request.method == "GET":
        routine_list = Routine.objects.all()
        template = loader.get_template('diarys/index2.html')
        context = {
            "routine_list": routine_list,
        }
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        title1 = request.POST['title']
        body1 = request.POST['body']
        # Routine.objects.create(name=title1, sets=body1)
        return redirect("/diarys/practice/")

#운동일지 화면
def daily_workout(request, year, month, date):
    if request.method == "POST":
        template = loader.get_template('diarys/daily.html')
        Name = request.POST["Name"]
        sets = request.POST["sets"]
        modelkey = str(year) + str(month) + str(date)
        Routine.objects.create(name=Name, sets=sets, modelkey=modelkey)
            
        return redirect("/diarys/" + str(year) + "/" + str(month) + "/" + str(date) + "/")
    else:
        set_date = datetime.datetime(year, month, date)
        next_date_ = set_date + datetime.timedelta(days=1)
        prev_date_ = set_date - datetime.timedelta(days=1)
        next_date = str(next_date_).split()[0].split("-")[-1]
        next_month = str(next_date_).split()[0].split("-")[-2]
        next_year = str(next_date_).split()[0].split("-")[-3]
        prev_date = str(prev_date_).split()[0].split("-")[-1]
        prev_month = str(prev_date_).split()[0].split("-")[-2]
        prev_year = str(prev_date_).split()[0].split("-")[-3]
        
        ymd = str(year) + str(month) + str(date)
        routine_list = Routine.objects.filter(modelkey=ymd)
        routine_comment = Routine_comment.objects.filter(modelkey=ymd)

        ##볼륨계산
        volume_total = 0
        for routine in routine_list:
            details = routine.routine_detail_set.all()
            for routine_detail in details:
                volume_total += float(routine_detail.weight) * float(routine_detail.reps)
            
        
        template = loader.get_template('diarys/daily.html')
        context = {
            "year": year,
            "month": month,
            "date": date,
            "next_date": next_date,
            "next_month": next_month,
            "next_year": next_year,
            "prev_date": prev_date,
            "prev_month": prev_month,
            "prev_year": prev_year,
            "routine_list": routine_list,
            "volume_total": volume_total,
            "routine_comment": routine_comment,           
        }
        return HttpResponse(template.render(context, request))
    
def add_routine(request, year, month, date, routine_id):
    routine = get_object_or_404(Routine, pk=routine_id)
    routine_detail = Routine_detail(routine=routine, weight=request.POST["weight"], reps=request.POST["reps"])
    routine_detail.save()
    return redirect("/diarys/" + str(year) + "/" + str(month) + "/" + str(date) + "/")

def edit_routine(request, year, month, date, routine_id):
    routine = get_object_or_404(Routine, pk=routine_id)
    routine.name = request.POST["Name"]
    routine.sets = request.POST["sets"]
    routine.save()
    return redirect("/diarys/" + str(year) + "/" + str(month) + "/" + str(date) + "/")

def delete_routine(request, year, month, date, routine_id):
    routine = get_object_or_404(Routine, pk=routine_id)
    routine.delete()
    return redirect("/diarys/" + str(year) + "/" + str(month) + "/" + str(date) + "/")

def comment(request, year, month, date):
    modelkey = str(year) + str(month) + str(date)
    Routine_comment.objects.create(comment=request.POST["comment"], modelkey=modelkey)
    return redirect("/diarys/" + str(year) + "/" + str(month) + "/" + str(date) + "/")

def del_comment(request, year, month, date, comment_id):
    comment = get_object_or_404(Routine_comment, pk=comment_id)
    comment.delete()
    return redirect("/diarys/" + str(year) + "/" + str(month) + "/" + str(date) + "/")
