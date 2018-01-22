from django.shortcuts import render

def index(request):
    # posts=[]
    posts=[
        {'id':'1','tittle'  :   '1er article','body'  : 'Bienvenue sur mon blog','footer'  :'au revoir!'},
        {'id':'2','tittle'  :   '1er article','body'  : 'Ce blog est mon entrainement sur python','footer'  :'au revoir!'},
        {'id':'3','tittle'  :   '2eme article','body'  : 'pour le moment, j\'aime bien ce langage!!','footer'  :'au revoir!'},
    ]

    return render(request, 'blog/index.html',{'posts':posts})
