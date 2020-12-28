from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from .models import Article, ScopeToArticle, Scope


class ScopeToArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            print(f'form = {form}\nform_type = {type(form)}')
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeToArticleInline(admin.TabularInline):
    model = ScopeToArticle
    formset = ScopeToArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeToArticleInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
