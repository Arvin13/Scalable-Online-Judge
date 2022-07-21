from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from .models import Contest, Problem
import subprocess
from .forms import NewUserForm as nuf
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request,usern, passw):
    con = [ usern, passw,'ant']
    return render(request, 'judge/test.html', { 'con' :con})


def signup(request):
    if request.method == 'POST':
        form = nuf(request.POST)
        if form.is_valid():
            if form.check_name() and form.check_mail():
                form.create_new_user()
                return contest(request)
    else:
        form = nuf()
    return render(request, 'judge/signup.html', {'form' : form})

def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return contest(request)
            else:
                return render(request, 'judge/signin.html', {'msg' : 'Password is incorrect'})
        else:
            return render(request, 'judge/signin.html', {'msg' : 'Username is incorrect'})

    else:
        return render(request, 'judge/signin.html', {'msg' : ''})

@login_required()
def contest(request):
    contest_list = Contest.objects.all()[:10]
    username = request.user.get_username()
    context = { "contest_list" : contest_list, 'username' : username }
    return render(request, 'judge/contest.html', context)

@login_required(login_url='/signin/')
def problem(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    problem_list = contest.problem_set.all()[:10]
    return render(request, 'judge/problem.html', {'problem_list' : problem_list, 'contest':contest})

@login_required(login_url='/signin/')
def submit(request, contest_id, problem_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    problems = contest.problem_set.all()
    problem = get_object_or_404(problems, pk=problem_id)
    test_case_list = problem.test_case_set.all()[:2]
    return render(request, 'judge/submission.html', {'problem' : problem, 'test_case_list' : test_case_list, 'contest_id' : contest_id})

@login_required(login_url='/signin/')
def result(request, contest_id, problem_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    problems = contest.problem_set.all()
    problem = get_object_or_404(problems, pk=problem_id)
    test_case_list = problem.test_case_set.all()

    test_case_t = len(test_case_list)
    test_case_p = 0
    test_case_f = 0
    pos_cl = 'NA'
    pos_ol = 'NA'
    ty = 0
    lang = request.POST['plang']
    if (lang == 'Python'):
        result = 'Pass'
        if request.FILES['input-file'] or request.POST['input-file']:
            f = request.FILES['input-file']
            with open(r'inputfile.py', 'w+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk.decode('UTF-8'))
        else:
            f = request.POST['input-code']
            ty = 1
            with open(r'inputfile.py', 'w+') as dest:
                dest.write(f)
        for tc in test_case_list:
            tci = tc.Input
            tco = tc.Output
            if ty==0:
                p = subprocess.Popen(['python3',r'inputfile.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True)
            else:
                p = subprocess.Popen(['python3',r'1_1_test.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True)
            a,b = p.communicate(input=tci)
            o = a.strip()
            e = b.strip()
            if (e==''):
                userout = o
                if (userout==tco):
                    test_case_p += 1
                else:
                    test_case_f += 1
                    result = "Failed"
            else:
                result = ('').join(list(e))
                break
    
    else:
        result = lang + ' Language Currently Not Supported'
    
    context = {
        'test_case_t' : test_case_t,
        'test_case_p' : test_case_p,
        'test_case_f' : test_case_f,
        'pos_cl' : pos_cl,
        'pos_ol' : pos_ol,
        'result' : result,
        'contest' : contest,
        'problem' : problem
        }
    
    return render(request, 'judge/result.html', context)
