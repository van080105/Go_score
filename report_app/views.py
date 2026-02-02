from django.shortcuts import render
from student_app.models import Score,Subject
from django.db.models import Count, Q, Sum, When, FloatField, Case

def count_levels_by_subject(subject):
    return {
        ">=8": Score.objects.filter(subject=subject, score__gte=8).count(),
        "6-8": Score.objects.filter(subject=subject, score__gte=6, score__lt=8).count(),
        "4-6": Score.objects.filter(subject=subject, score__gte=4, score__lt=6).count(),
        "<4": Score.objects.filter(subject=subject, score__lt=4).count(),
    }

def report_page(request):
    subjects = Subject.objects.all()
    data = {}

    for subject in subjects:
        data[subject.name] = count_levels_by_subject(subject)

    return render(request, "report_app/report.html", {"data": data})

def top10_page(request):
    students = (
        Score.objects
        .filter(subject__code__in=['toan', 'vat_li', 'hoa_hoc'])
        .values('student__sbd')
        .annotate(
            toan=Sum(
                Case(
                    When(subject__code='toan', then='score'),
                    output_field=FloatField()
                )
            ),
            ly=Sum(
                Case(
                    When(subject__code='vat_li', then='score'),
                    output_field=FloatField()
                )
            ),
            hoa=Sum(
                Case(
                    When(subject__code='hoa_hoc', then='score'),
                    output_field=FloatField()
                )
            ),
            total=Sum('score')
        )
        .order_by('-total')[:10]
    )

    return render(request, "report_app/top10.html", {"students": students})
