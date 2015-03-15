from django.conf.urls import patterns, url
from decompile import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^view_files/$', views.view_files, name='view_files'),
	url(r'^dcmpl/(?P<file_name>[\w\-]+)/$', views.dcmpl, name='dcmpl'),
	url(r'^show_dir/(?P<file_name>[\w\-]+)/$', views.show_dir, name='show_dir'),
	url(r'^edit_file/(?P<file_path>[\w\-\+\*\$]+)/$', views.edit_file, name='edit_file'),
)
