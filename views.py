from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Agent

# Create your views here.
def agentView(request):
    return render(request, 'AgentSignUp.html')

def login(request):
    return render(request, 'login.html')

def returningAgent(request):
    try:
        x = Agent.objects.get(username = request.POST['returninguser'],password = request.POST['returningpass'])
        diction = {
            'f' : x.firstName,
            'l' : x.lastName,
            'c' : x.agencyName,
            'p' : x.username
            }
        return render(request, 'dashboard.html', diction)
    except:
        return HttpResponseRedirect('/agent/')


def newAgent(request):
    #Basic Info
    fn = request.POST['q3_name[first]']
    ln = request.POST['q3_name[last]']
    username = request.POST['username']
    password = request.POST['password']
    an = request.POST['q14_agencyName']
    be = request.POST['q4_businessEmail']
    sa1 = request.POST['q5_businessAddress[addr_line1]']
    sa2 = request.POST['q5_businessAddress[addr_line2]']
    c = request.POST['q5_businessAddress[city]']
    s = request.POST['q5_businessAddress[state]']
    postal = request.POST['q5_businessAddress[postal]']
    p1 = request.POST['q6_businessOr[area]']
    p2 = request.POST['q6_businessOr[phone]']
    
    fullPhone = str(p1) + str(p2)
    
    #Specialty Coverages
    pL = request.POST["q7_whatLines[]"]
    #tr = request.POST['q7_phoneNumber']
    #wc = request.POST['q7_phoneNumber']
    #ml = request.POST['q7_phoneNumber']
    #prop = request.POST['q7_phoneNumber']
    #cy = request.POST['q7_phoneNumber']
    #ex = request.POST['q7_phoneNumber']
    #product = request.POST['q7_phoneNumber']

    #Industries
    retail = request.POST['q10_whatIndustries[]']
    #tech = request.POST['q3_name[first]']
    #manufacturing = request.POST['q3_name[first]']
    #wholesale = request.POST['q3_name[first]']
    #transportation = request.POST['q3_name[first]']
    #construction = request.POST['q3_name[first]']
    #publicEntity = request.POST['q3_name[first]']
    #agriculture = request.POST['q3_name[first]']
    #realEstate = request.POST['q3_name[first]']

    smb = request.POST['q11_whatSize[]']
    #mm = request.POST['q3_name[first]']
    #large = request.POST['q3_name[first]']
    additonalInfo = request.POST['q12_helpCustomers']

    agent = Agent(firstName = fn, lastName = ln, agencyName = an, bizEmail = be, streetAddress1 = sa1, streetAddress2 = sa2,
    city = c, state = s, postal = postal, p1 = p1, p2 =p2, username = username, password = password)
    agent.save()

    return HttpResponseRedirect('/agent/' + str(username) + '/')

def agentDashboard(request, agent_id):
    agent = Agent.objects.get(username = agent_id)
    fullPhone = str(agent.p1) + str(agent.p2)
    thisdict = {
        'f' : agent.firstName,
        'l' : agent.lastName,
        'c' : agent.agencyName,
        'p' : fullPhone
    }
    return render(request, 'dashboard.html', thisdict)

def homePage(request):
    return render(request, 'homepage.html')


