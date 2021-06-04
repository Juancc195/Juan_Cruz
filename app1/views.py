from django.shortcuts import render
from django.http import HttpResponse

cuota_registro =  [
            {
                'monto':'200000',
                'tasa':'8',
                'plazo':'10',
                'cuota':'2426.55',
                'total':'291186.23',
            },
            {
                'monto':'350000',
                'tasa':'15',
                'plazo':'8',
                'cuota':'6280.89',
                'total':'602965.62',
            },{
                'monto':'125000',
                'tasa':'7',
                'plazo':'10',
                'cuota':'1451.36',
                'total':'174162.72',
            },
]

def index(request):
    if request.method == 'POST':

        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        r = tasa / 100 / 12
        n = plazo * 12

        cuota = (monto*r)/(1-(1+r)** -n)
        total = cuota * n

        cuota_registro.append({
            'monto':monto,
            'tasa':tasa,
            'plazo':plazo,
            'cuota':round(cuota,2),
            'total':round(total,2),
        })
        ctx = {
            'cuota_registro': cuota_registro
        }

        return render(request, "registro/index.html", ctx)
    else:
        ctx = {
            'cuota_registro': cuota_registro
        }
        return render(request, "registro/index.html", ctx)