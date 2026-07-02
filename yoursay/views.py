from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from issues.models import Issue
from transactions.models import Transaction

def get_stats(request):

    total_received = Transaction.objects.filter(
        type='credit'
    ).aggregate(total=Sum('amount'))['total'] or 0

    total_spent = Transaction.objects.filter(
        type='debit'
    ).aggregate(total=Sum('amount'))['total'] or 0

    balance = total_received - total_spent

    issues_resolved = Issue.objects.filter(status='done').count()

    recent_txns = Transaction.objects.all()[:6]
    transactions = []
    for tx in recent_txns:
        transactions.append({
            'id':       tx.id,
            'name':     tx.name,
            'description': tx.description,
            'amount':   float(tx.amount),
            'type':     tx.type,
            'category': tx.get_category_display(),
            'status':   tx.status,
            'status_label': tx.get_status_display(),
            'icon':     tx.icon,
            'date':     tx.date.strftime('%b %d, %Y'),
        })

    top_issues = Issue.objects.all()[:3]
    issues = []
    for issue in top_issues:
        issues.append({
            'id':          issue.id,
            'title':       issue.title,
            'status':      issue.status,
            'votes':       issue.votes,
            'fund_goal':   float(issue.fund_goal),
            'fund_raised': float(issue.fund_raised),
        })

    return JsonResponse({
        'total_received':  float(total_received),
        'total_spent':     float(total_spent),
        'balance':         float(balance),
        'issues_resolved': issues_resolved,
        'transactions':    transactions,
        'top_issues':      issues,
    })

def create_admin(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        return HttpResponse("✅ Admin created! Go to <a href='/admin/'>/admin/</a> to login.")
    return HttpResponse("✅ Admin already exists. Go to <a href='/admin/'>/admin/</a> to login.")