import json
from django.core.management.base import BaseCommand
from articles.models import Article


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('articles.json', 'r') as json_file:
            data = json.load(json_file)
            for line in data:
                new_article = Article(
                    title=line['fields']['title'],
                    text=line['fields']['text'],
                    published_at=line['fields']['published_at'],
                    image=line['fields']['image'],
                )
                new_article.save()
