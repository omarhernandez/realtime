from django.conf.urls.defaults import patterns,url

 #creamos nueva rama de urls

urlpatterns = patterns('apps.inicio.views', #prefijos de la vista que queremos jalar archivo donde estamos jalando las vistas

			url(r'^$' ,    'publish' ,  name = 'view_ublish') ,  
			) 
