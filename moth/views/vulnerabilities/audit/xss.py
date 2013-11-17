from moth.views.base.vulnerable_template_view import VulnerableTemplateView
from django.shortcuts import render


class SimpleXSSView(VulnerableTemplateView):
    title = 'Cross-Site scripting (trivial)'
    description = 'Echo query string parameter to HTML without any encoding'
    url_path = 'xss/simple_xss.py'
    
    def get(self, request, *args, **kwds):
        context = self.get_context_data()
        context['html'] = request.GET['text']
        return render(request, self.template_name, context)