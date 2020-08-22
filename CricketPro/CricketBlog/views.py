from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TeamForm, PlayersForm, MatchFixForm, ScoreBoardForm
from .models import Team, Player


def get_id():
    sample="TEAM"+str(2000)
    count=Team.objects.all().count()
    return count+1



def team_list(request):
    list_team=Team.objects.all()
    return render(request,'list_teams.html',{'list':list_team})

# def create_team(request):
#     form=TeamForm()
#     if request.method=="POST":
#         form=TeamForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             print("before save")
#             form.save(commit=False)
#             print("After save")
#
#             return redirect('team_list')
#     return render(request,'cteate_team.html',{'form':form})
def create_team(request):
    form=TeamForm()
    if request.method=="POST":
        form=TeamForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.identifier=get_id()
            obj.save()
            return redirect('team_list')
    return render(request,'cteate_team.html',{'form':form})
# def vvv(request):
#     if request.method=='POST':
#         try:
#             print("Post data", request.POST)
#             name = request.POST.get('name')
#             logo_url = request.POST.get('logo_url')
#             club_state = request.POST.get('club_state')
#             identifier = get_id()
#             print(name,logo_url,club_state)
#
#             match = Team.objects.create(identifier=identifier, name=name, logo_url=logo_url, club_state=club_state)
#             messages.info(request, 'Team Created sucessfully')
#             return redirect('team_list')
#         except Exception as e:
#             messages.error(request,'form not submitted')
#             return HttpResponse(e)
#     return render(request,'cteate_team.html')


def create_player(request):
    form=PlayersForm()
    if request.method=="POST":
        form=PlayersForm(request.POST, request.FILES)
        print(request.POST)
        try:
            if form.is_valid():
                form.save(commit=True)
                return redirect('team_list')
        except Exception as e:
            return HttpResponse(e)


    return render(request,'create_players.html',{'form':form})
def team_detail(request,id):
    # list_team = Team.objects.filter(identifier=id).select_related('team')
    players=Player.objects.filter(team_id=id).select_related('team')


    return render(request,'team_payers_list.html',{'players':players})

def main_page(request):
    return render(request,'base.html')

def fix_match(request):
    pass
    # form=MatchFixForm()
    # if request.method=='POST':
    #     form=MatchFixForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return redirect('win')
    # return render(request,'fix_match.html',{'form':form})

def win(request):
    pass
#     form=ScoreBoardForm()
#     if request.method=="POST":
#         form=ScoreBoardForm(request.POST,request.FILES)
#         if form.is_valid():
#             won=form.save(commit=True)
#
#             return render('team_list')
#     return render(request,'winning_score.html',{'form':form})
# #
# # def points_between_teams(request):
# #     form=PointsForm()
# #     if request.method=="POST":
# #         form=PointsForm(request.POST,request.FILES)
# #         if form.is_valid():
# #             obj=form.save(commit=True)
# #
# #             return redirect('main_page')
# #
# #
# #     return render(request,'points.html',{'form':form})
#
#
# def view_point(request):
#
#     teams=Team.objects.get(identifier=3)
#
#     return HttpResponse()
#
