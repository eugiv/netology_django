from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_cnt = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_cnt += 1

        if is_main_cnt == 0:
            raise ValidationError("Укажите основной раздел.")
        elif is_main_cnt > 1:
            raise ValidationError("Основной раздел должен быть только один.")

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
