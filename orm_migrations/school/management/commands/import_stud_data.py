import json
from django.core.management.base import BaseCommand
from school.models import Student, Teacher
from website import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.FILE, encoding='utf-8') as file:
            reader = json.load(file)

            for item in reader:
                if item['model'] == 'school.teacher':
                    new_teacher = Teacher(name=item['fields']['name'],
                                          subject=item['fields']['subject'])
                    new_teacher.save()
                if item['model'] == 'school.student':
                    new_student = Student(name=item['fields']['name'],
                                          group=item['fields']['group'])
                    new_student.save()
                    teacher = Teacher.objects.all().get(id=item['fields']['teacher'])
                    new_student.teacher.add(teacher)
