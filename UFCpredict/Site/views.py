from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm

from Prediction import  LGBM

def index(request):
    error=""
    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            subject1 = form.cleaned_data['fighter1']
            subject2 = form.cleaned_data['fighter2']

            lgbmResult = LGBM(subject1,subject2)
            if lgbmResult[0] !=0:


                if lgbmResult[2] ==1:
                    InformR = subject2
                    InformB = subject1
                    probaToWin1 = "probability to win for " + subject2 + " is " + str(lgbmResult[4][0])
                    probaToWin2 = "probability to win for " + subject1 + " is " + str(lgbmResult[4][1])
                else:
                    InformR = subject1
                    InformB = subject2
                    probaToWin1 = "probability to win for " + subject1 + " is " + str(lgbmResult[4][0])
                    probaToWin2 = "probability to win for " + subject2 + " is " + str(lgbmResult[4][1])
            #    InformR +="Age: "+ inform['R_Age'][0]
                InformR += "\nHeight: "+ str(lgbmResult[3]['R_Height_cms'])
                InformR += "\nWeight: " + str(lgbmResult[3]['R_Weight_lbs'])
                InformR += "\nWins: " + str(lgbmResult[3]['R_wins'])
                InformR += "\nLosses: " + str(lgbmResult[3]['R_losses'])
                InformR += "\nDraw: " + str(lgbmResult[3]['R_draw'])

      #          InformB +="Age: "+ lgbmResult[3]['B_Age']
                InformB += "\nHeight: " + str(lgbmResult[3]['B_Height_cms'])
                InformB += "\nWeight: " + str(lgbmResult[3]['B_Weight_lbs'])
                InformB += "\nWins: " + str(lgbmResult[3]['B_wins'])
                InformB += "\nLosses: " + str(lgbmResult[3]['B_losses'])
                InformB += "\nDraw: " + str(lgbmResult[3]['B_draw'])
                if lgbmResult[1] == lgbmResult[2]:
                    error = "winner: " + subject1
                else:
                    error = "winner: " + subject2
                content = {'winner': error, 'InformR': InformR, 'InformB': InformB, 'probaToWin1': probaToWin1, 'probaToWin2': probaToWin2}
                return render(request, 'Site/prediction.html', content)
            else:
                error="Error: cannot find fight between this fighters"

        else:
            error="invalid form"
    else:
        form = TaskForm()


    content = {        'form': form,        'error': error    }
    return render(request, 'Site/index.html', content)



def about(request):
    return render(request, 'Site/about.html')

def predPage(request):
    return render(request, 'Site/prediction.html')
