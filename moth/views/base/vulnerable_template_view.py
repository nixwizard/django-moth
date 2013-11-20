import urlparse

from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


class VulnerableTemplateView(TemplateView):
    '''
    All vulnerabilities inherit from this template, which will render the data
    returned by the subclasses, disable anti-CSRF, etc.
    '''
    # The template to use to render this view
    template_name = "moth/vulnerability.html"
    
    # The title that will appear on the rendered HTML
    title = None
    
    # The description that will appear on the rendered HTML
    description = None
    
    # The URL pattern string (not regex for now) which we'll try to match before
    # sending information to this view. This is parsed by the router view.
    url_path = None
    
    # Is this a real vulnerability or a false positive check?
    false_positive_check = False

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(VulnerableTemplateView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(VulnerableTemplateView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['description'] = self.description
        context['false_positive_check'] = self.false_positive_check
        return context

    def get_url_path(self):
        '''
        :return: The URL path, without any query string. To be used mainly in
                 routing to the right view without taking parameters (?text=1)
                 into account.
        '''
        return urlparse.urlparse(self.url_path).path
        
    def get(self, request, *args, **kwds):
        if self.HTML is not None:
            context = self.get_context_data()
            context['html'] = self.HTML
            return render(request, self.template_name, context)
        else:
            return super(VulnerableTemplateView, self).get(request, *args, **kwds)