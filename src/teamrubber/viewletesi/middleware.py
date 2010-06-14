import re
import os
from chameleon.zpt.template import PageTemplateFile

esi_re = re.compile('/\+\+viewlet\+\+(.*?)\:(.*?)(\?|$)')

class ESIMiddleware(object):
    
    def __init__(self,app,template_path=None):
        self.app = app
        self.templates = {}

        # We load the set of allowed templates on startup, this means you have
        # to restart the wsgi stack if you want to add templates, but totally
        # removes the possibility of directory traversal attacks.
        if template_path is not None:
            template_ids = os.listdir(template_path)
            for template_id in template_ids:
                filename = os.path.join(template_path,template_id)
                template = PageTemplateFile(filename)

                if template_id.endswith('.pt'):
                    template_id = template_id[:-3]
                self.templates[template_id] = template
    
    def __call__(self,environ,start_response):
        if "HTTP_X_ESI_DISABLE" in environ and 'i_might_be_a_moderator' not in environ.get("HTTP_COOKIE",""):
            disabled_viewlets = environ["HTTP_X_ESI_DISABLE"].split(',')
    
            match = esi_re.search(environ.get("PATH_INFO",''))
            if match:
                viewlet_name = "%s:%s" % (match.group(1),match.group(2))
                if viewlet_name in disabled_viewlets:
                    start_response('200 OK',[('Content-Type','text/html')])

                    # Build a sane filename.
                    template_id = "%s-%s" % (match.group(1),match.group(2))
                    template_id = template_id.replace('.','-')
                    # Do we have a template for this?
                    template = self.templates.get(template_id)
                    if template is not None:
                        return [template(environ=environ,middleware=self)]
                    else:
                        return ['']
            
        return self.app(environ,start_response)
    

def ESIMiddlewareFactory(global_config, **local_conf):
    def wrapper(app):
        return ESIMiddleware(app,template_path=local_conf.get("path"))
    return wrapper
