
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.db import models
from .models import Classe
from .models import Devoir
from .models import Participe,Realisation
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .form import DevoirForm, UploadFileForm,rendreDevoirForm
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
import subprocess,os.path
from os.path import basename
import sys
from subprocess import call




def recupNote(request,devoir_id):
    current_user = request.user
    realisations=Realisation.objects.filter(idDevoir=devoir_id)
    context={
        'realisations' : realisations,
        'current_user' : current_user,
        'devoir_id' : devoir_id
          }
    return render(request, 'pages/recupNotes.html', context)

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def invoiceView(request):
    return render(request, 'pages/invoice.html')


def devoir_rendre(request,devoir_id):
    current_user = request.user
    form = rendreDevoirForm(request.POST,request.FILES or None )

    if form.is_valid():


        instance = form.save(commit=False)
        instance.save()


        #David
        leDevoir=Devoir.objects.get(pk=devoir_id)
        lesRealisationsDevoir=Realisation.objects.filter(idDevoir=devoir_id)
        cRealisationEtudiant=""

        for uneRealisation in lesRealisationsDevoir:
            # sys.stderr.write("idEtu")
            # # sys.stderr.write(str(uneRealisation.idEtudiant))
            # # sys.stderr.write("userId")
            # #sys.stderr.write(current_user.id)
            if uneRealisation.idEtudiant == str(current_user.id) :
                cRealisationEtudiant=""
                cRealisationEtudiant=str(uneRealisation.reponse)

                idRea=uneRealisation.id
                correction(leDevoir,cRealisationEtudiant,idRea)
                return redirect('/index/')

        return redirect('/error/' )
    else:
        form = rendreDevoirForm(request.POST,request.FILES or None )
        unDevoir = Devoir.objects.get(pk=devoir_id)
        #unProf=User.objects.filter(username__icontains=uneClasse.professeur)
        context={
            'current_user' : current_user,
            'unDevoir' : unDevoir,
            "form" : form,
            'devoir_id' : devoir_id,

            }
    return render(request, 'pages/rendreDevoir_form.html', context)


def devoir_create(request,classe_id):
    uneClasse = Classe.objects.get(pk=classe_id)
    form=DevoirForm()
    current_user=request.user
    context={
        'uneClasse' : uneClasse,
        'classe_id' : classe_id,
        'form' : form,
        'current_user' : current_user,
    }
    if request.method == 'POST':
        form = DevoirForm(request.POST,request.FILES or None )

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/index/')
    else:

        return render(request, 'pages/devoir_form.html',context )


# def devoir_create(request, classe_id):
#
#     if request.method == 'POST':
#         form = DevoirForm(request.POST,request.FILES or None )
#         if form.is_valid():
#             form.save()
#             return redirect('/index/')
#         else :
#             uneClasse = Classe.objects.get(pk=classe_id)
#             context={
#             'uneClasse' : uneClasse,
#             #"form" : form,
#             'classe_id' : classe_id,
#             }
#             #return render(request, 'pages/devoir_form.html',context)

    # else :
    #     uneClasse = Classe.objects.get(pk=classe_id)
    #     form = DevoirForm(request.POST,request.FILES or None )
    #     context={
    #     'uneClasse' : uneClasse,
    #     "form" : form,
    #     'classe_id' : classe_id,
    #     }
    #     return render(request, 'pages/devoir_form.html',context )


def devoir_update(request, id=None):
    instance=get_object_or_404(Devoir,id=id)
    context = {
        "titre":instance.titre,
        "instance":instance,
    }
    return render(request, 'pages/devoir_form.html', context)





def detailsClasse2(request,classe_id,post):
    try:
        uneClasse = Classe.objects.get(pk=classe_id)
        devoirs = Devoir.objects.filter(idClasse=classe_id)
        context={
            'uneClasse' : uneClasse,
            'devoirs' : devoirs
        }
    except Classe.DoesNotExist:
        raise Http404("La classe n'existe pas")
    return render(request,'pages/detailsClasse.html',context)

def index(request):
    current_user = request.user
    group = Group.objects.get(name="Prof")
    if group in current_user.groups.all():
        #PROFESSEURS
        classes = Classe.objects.filter(professeur__icontains=request.user.username)
        allClasses= Classe.objects.all()
        context={
            'classes' : classes,
            'user' : current_user,
            'allClasses' : allClasses
        }
        return render(request, 'pages/indexProf.html', context)
    else:
        #ELEVE
        allClasses= Classe.objects.all()
        allDevoirs= Devoir.objects.all()
        allParticipeEleve= Participe.objects.filter(idEtudiant=request.user.id)
        listDevoirs=[]
        for unDevoir in allDevoirs:
            for uneParticipation in allParticipeEleve:
                if unDevoir.id == int(uneParticipation.idDevoir):
                    listDevoirs.append(unDevoir)
        taille=len(listDevoirs)
        context={
            'allClasses' : allClasses,
            'allDevoirs' : allClasses,
            'allParticipeEleve' : allParticipeEleve,
            'user' : current_user,
            'listDevoirs' : listDevoirs,
            'taille' : taille
        }
        return render(request, 'pages/indexEleve.html',context)

def detailsClasse(request,classe_id):
    try:
        uneClasse = Classe.objects.get(pk=classe_id)
        devoirs = Devoir.objects.filter(idClasse=classe_id)
        context={
            'uneClasse' : uneClasse,
            'devoirs' : devoirs
        }
    except Classe.DoesNotExist:
        raise Http404("La classe n'existe pas")
    return render(request,'pages/detailsClasse.html',context)

def remplirNouveauDevoir(request,classe_id):
    uneClasse = Classe.objects.get(pk=classe_id)
    context={
            'uneClasse' : uneClasse,
        }
    return render(request,'pages/remplirNouveauDevoir.html',context)


def detailsDevoir(request,devoir_id):
    try:
        current_user=request.user
        unDevoir = Devoir.objects.get(pk=devoir_id)
        group=Group.objects.get(name="Prof")

        if group in current_user.groups.all():
            Prof="TRUE"
        else:
            Prof="FALSE"

        context={
            'Prof' : Prof,
            'unDevoir' : unDevoir
        }
    except Classe.DoesNotExist:
        raise Http404("La classe n'existe pas")
    return render(request,'pages/detailsDevoir.html',context)







def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def reponse(request):
    return render(request, 'pages/maReponse.html')

def cours(request):
    return render(request, 'pages/cours.html')

def login(request):
    return render(request, 'registration/login.html')

def pathEntrees(leDevoir):
    entree = ""
    fileEntree = open(leDevoir.pathEntrees.path, "r")
    freadsEntree = fileEntree.readlines()
    for f in freadsEntree:
        entree += f.strip()+ " "

    sys.stderr.write("Entre "+entree)
    return entree


def pathSortie(leDevoir):
    sortie = ""
    fileSortie = open(leDevoir.pathCorrection.path, "r")
    freadsSortie = fileSortie.readlines()
    for f in freadsSortie:
        sortie=f
    return sortie


def correction(leDevoir,realisationEtudiant,idRea):
    entree=pathEntrees(leDevoir)



    sortie=pathSortie(leDevoir)
    sys.stderr.write("sortie : "+sortie+"\n")


    nameFiles=realisationEtudiant+" "
    print (call(["ls", "-l"]))
    command = "python media/" +nameFiles+entree # commande shell
    sys.stderr.write("commande FDP : "+command+"\n")
    process = subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=None, shell=True)

    # version épurée
    # démarre la commande shell
    output = process.communicate()
    sys.stderr.write("output : "+output[0].decode('utf-8')+"\n")

    out = str(output[0].decode('utf-8')).strip() # return en utf8 pour supprimer les symbole inutile et enlever les espaces
    uneRealisation = Realisation.objects.get(pk=idRea)
    # uneRealisation.note=20
    # uneRealisation.save()
    sys.stderr.write("out : "+out+"\n")
    if (int(sortie) == int(out)): # la variable string est à remplacer par les valeurs saisis parle prof
        uneRealisation.note = 20
        uneRealisation.save()
        return 20
    else:
        uneRealisation.note = 10
        uneRealisation.save()
        return 0
