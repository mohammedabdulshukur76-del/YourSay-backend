from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Review

def get_reviews(request):
    reviews = Review.objects.all()
    data = []
    for r in reviews:
        data.append({
            'id':          r.id,
            'name':        r.name,
            'location':    r.location,
            'type':        r.type,
            'type_label':  r.get_type_display(),
            'rating':      r.rating,
            'text':        r.text,
            'helpful':     r.helpful,
            'is_pinned':   r.is_pinned,
            'team_reply':  r.team_reply,
            'created_at':  r.created_at.strftime('%b %d, %Y'),
        })
    return JsonResponse({'reviews': data})


@csrf_exempt
def submit_review(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        body   = json.loads(request.body)
        review = Review.objects.create(
            name     = body.get('name', ''),
            location = body.get('location', ''),
            type     = body.get('type', 'general'),
            rating   = body.get('rating', 5),
            text     = body.get('text', ''),
        )
        return JsonResponse({
            'success':    True,
            'id':         review.id,
            'created_at': review.created_at.strftime('%b %d, %Y'),
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def mark_helpful(request, review_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    review = get_object_or_404(Review, id=review_id)
    review.helpful += 1
    review.save()
    return JsonResponse({'success': True, 'helpful': review.helpful})