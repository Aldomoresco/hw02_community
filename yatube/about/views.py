# from django.shortcuts import render
from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title'] = 'Об авторе проекта'
        context['just_text'] = 'Раздел в процуссе заполнения.'
        context['just_author'] = 'Об авторе.'
        return context


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['just_title1'] = 'Технологии'
        context['just_text1'] = 'Стрвница  "Технологии" в процессе заполнения.'
        context['just_author1'] = 'Вот что я умею.'
        return context
