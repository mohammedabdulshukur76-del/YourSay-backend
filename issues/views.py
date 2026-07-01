from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Issue

def get_issues(request):
    issues = Issue.objects.all()

    data = []
    for issue in issues:
        data.append({
            'id':           issue.id,
            'title':        issue.title,
            'description':  issue.description,
            'location':     issue.location,
            'category':     issue.get_category_display(),
            'status':       issue.status,
            'status_label': issue.get_status_display(),
            'fund_goal':    float(issue.fund_goal),
            'fund_raised':  float(issue.fund_raised),
            'votes':        issue.votes,
            'submitted_by': issue.submitted_by,
            'created_at':   issue.created_at.strftime('%b %d, %Y'),
        })

    return JsonResponse({'issues': data})


@csrf_exempt
def submit_issue(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    try:
        body = json.loads(request.body)

        issue = Issue.objects.create(
            title        = body.get('title', ''),
            description  = body.get('description', ''),
            location     = body.get('location', ''),
            category     = body.get('category', 'other'),
            submitted_by = body.get('submitted_by', ''),
            fund_goal    = body.get('fund_goal', 0),
            status       = 'review',
            votes        = 0,
        )

        return JsonResponse({
            'success': True,
            'id':      issue.id,
            'message': 'Issue submitted successfully'
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def vote_issue(request, issue_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    issue = get_object_or_404(Issue, id=issue_id)
    issue.votes += 1
    issue.save()

    return JsonResponse({
        'success': True,
        'votes':   issue.votes
    })