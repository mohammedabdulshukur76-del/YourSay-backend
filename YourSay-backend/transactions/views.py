from django.http import JsonResponse
from .models import Transaction

def get_transactions(request):
    transactions = Transaction.objects.all()

    data = []
    for tx in transactions:
        data.append({
            'id':          tx.id,
            'name':        tx.name,
            'description': tx.description,
            'amount':      float(tx.amount),
            'type':        tx.type,
            'category':    tx.get_category_display(),
            'status':      tx.status,
            'status_label':tx.get_status_display(),
            'icon':        tx.icon,
            'date':        tx.date.strftime('%b %d, %Y'),
        })

    return JsonResponse({'transactions': data})