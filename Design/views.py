from django.shortcuts import render, redirect
from .models import Language,UserMst,Leaderboard
from . forms import languageform,userform
from django.http import JsonResponse
import pymysql


# def indexview(request):
#     return render(request,"index.html")

def home(request):
    return render(request, 'index.html')


def student_login(request):
    return render(request, "student_login.html")

def student_login1(request):
    if(request.method=="POST"):
        Username=request.POST['Username']
        Password=request.POST['Password']
        flag=0
        db=pymysql.connect(host="localhost",user="root",password="",database="codecronicals",port=3306)
        cursor=db.cursor()
        cursor.execute("select username, password from design_usermst")
        records = cursor.fetchall()
        if records:
            # User is found, redirect to intro.html (can be any view name)
            return redirect('intro')
        else:
            # Incorrect login, redirect to the index page
            return redirect('index')

        db.close()
        


def Logintrans(request):
    return render(request, "Userform.html")

def Logintrans1(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        ContactNo = request.POST['ContactNo']
        Username = request.POST['Username']
        Password = request.POST['Password']
        
        db = pymysql.connect(host="localhost", user="root", password="", database="codecronicals", port=3306)
        cursor = db.cursor()
        cursor.execute("INSERT INTO design_UserMst (name, email, contactno, username, password) VALUES (%s, %s, %s, %s, %s)",
                       (Name, Email, ContactNo, Username, Password))
        db.commit()
        db.close()
        return redirect('student_login') 
    

def intro(request):
    return render(request, "intro.html")

def map(request):
    return render(request, 'map.html', {'username': request.user.username})

def topic1(request):
    return render(request, "topic1.html")

def topic2(request):
    return render(request, "topic2.html")

def topic3(request):
    return render(request, "topic3.html")

def nested(request):
    return render(request, "nested.html")

def index1(request):
    return render(request, "index1.html")

def thanks(request):
    return render(request, "thanks.html")

def datatypes(request):
    return render(request, "datatypes.html")


def index2(request):
    return render(request, "index2.html")

def thanks2(request):
    return render(request, "thanks2.html")

def index3(request):
    return render(request, "index3.html")

def thanks3(request):
    return render(request, "thanks3.html")

def index4(request):
    return render(request, "index4.html")

def thanks4(request):
    return render(request, "thanks4.html")

def index5(request):
    return render(request, "index5.html")

def thanks5(request):
    return render(request, "thanks5.html")


def map1(request):
    return render(request, "map1.html")

def arithmetic(request):
    return render(request, "arithmetic.html")

def logical(request):
    return render(request, "logical.html")

def variables(request):
    return render(request, "variables.html")

def datatypes(request):
    return render(request, "datatypes.html")

def progress(request):
    return render(request, "progress.html")

def review(request):
    return render(request, "review.html")


def interactive_page(request):
    context = {
        'username': request.user.username,  # Pass the username to the template
    }
    return render(request, 'interactive_page.html', context)

def submit_score(request):
    if request.method == "POST":
        username = request.POST.get("username")
        score = int(request.POST.get("score"))

        # Save or update the leaderboard entry
        leaderboard_entry, created = Leaderboard.objects.update_or_create(
            username=username,
            defaults={"score": score}
        )
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"}, status=400)

def get_leaderboard(request):
    leaderboard = Leaderboard.objects.order_by("-score")[:10]  # Top 10 scores
    data = [{"username": entry.username, "score": entry.score} for entry in leaderboard]
    return JsonResponse(data, safe=False)