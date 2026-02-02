from django.shortcuts import render
from .models import Student, Score

def check_score(request):
    sbd = request.GET.get('sbd')
    if not sbd:
        return render(request, 'student_app/result.html')
    try:
        student = Student.objects.get(sbd=sbd)
        scores = Score.objects.filter(student=student).select_related('subject')
        return render(request, 'student_app/result.html', {
            'student': student,
            'scores': scores
        })
    except Student.DoesNotExist:
        return render(request, 'student_app/result.html', {
            'error': 'Không tìm thấy SBD'
        })
