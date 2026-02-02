import csv
from django.core.management.base import BaseCommand
from student_app.models import Student, Subject, Score

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']

        subject_map = {
            'toan': 'Toán',
            'ngu_van': 'Ngữ văn',
            'ngoai_ngu': 'Ngoại ngữ',
            'vat_li': 'Vật lí',
            'hoa_hoc': 'Hóa học',
            'sinh_hoc': 'Sinh học',
            'lich_su': 'Lịch sử',
            'dia_li': 'Địa lí',
            'gdcd': 'GDCD',
        }

        for code, name in subject_map.items():
            Subject.objects.get_or_create(code=code, defaults={'name': name})

        BATCH_SIZE = 2000
        score_batch = []

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for i, r in enumerate(reader, start=1):
                student, _ = Student.objects.get_or_create(
                    sbd=r['sbd'],
                    defaults={'foreign_language_code': r.get('ma_ngoai_ngu')}
                )

                for subject_code in subject_map.keys():
                    val = r.get(subject_code)
                    if val:
                        subject = Subject.objects.get(code=subject_code)
                        score_batch.append(
                            Score(student=student, subject=subject, score=float(val))
                        )

                if len(score_batch) >= BATCH_SIZE:
                    Score.objects.bulk_create(score_batch, ignore_conflicts=True)
                    score_batch = []
                    print(f"Processed {i} students...")

        if score_batch:
            Score.objects.bulk_create(score_batch, ignore_conflicts=True)
