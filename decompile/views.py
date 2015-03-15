from django.shortcuts import render
from django.http import HttpResponseRedirect
from decompile.forms import apkForm
from decompile.models import APKFile
import os
import xml.etree.ElementTree as ET

string = []

# Create your views here.
def index(request):
	return render(request, "decompile/index.html", {})

def upload(request):

	if request.method == 'POST':
		form = apkForm(request.POST, request.FILES)
		if form.is_valid:
			newApk = APKFile(apkfile = request.FILES['apkfile'])
			newApk.save()
			file_name = newApk.apkfile.name[:-4]
			print file_name
			decompile_apk(file_name)
			return view_files(request)
		else:
			print form.errors
	else:
		form = apkForm()

	
	return render(request, "decompile/upload.html", {'form':form})

def decompile_apk(file_name):
	#decompiling
	command = "apktool d "+file_name+".apk"
	chdir = '/home/kalyan/djangoprojects/apkDecompiler/decompile/apkfiles'
	os.chdir(chdir)
	os.system(command)

def dcmpl(request, file_name):
	
	print file_name
	#xml parsing
	tree = ET.parse('/home/kalyan/djangoprojects/apkDecompiler/decompile/apkfiles/'+file_name+'/AndroidManifest.xml')
	root = tree.getroot()
	activities = []
	services = []
	for application in root.findall('application'):
		for activity in application.findall('activity'):
			activities.append(activity.attrib['{http://schemas.android.com/apk/res/android}name'])
		for service in application.findall('service'):
			services.append(activity.attrib['{http://schemas.android.com/apk/res/android}name'])
	context_dict = {}
	
	context_dict['activities']=activities
	context_dict['services']=services

	return render(request, 'decompile/success.html', context_dict)

def view_files(request):
	apkfiles = APKFile.objects.all();
	return render(request, 'decompile/view_files.html',{'apkfiles':apkfiles})

def traverse(dir):
	string.append('<ul class="nav">')
	for item in os.listdir(dir):

		dirpath = os.path.join(dir, item)
		ext1 = '.html'
		ext2 = '.smali'
		ext3 = '.xml'
		ext4 = '.cfg'
		ext5 = '.css'
		li_name = item

		param = dirpath.replace("/", "+")
		param = param.replace(".", "*")
		if ext1 in item or ext2 in item or ext3 in item or ext4 in item or ext5 in item:
			li_name = '<a href="/decompile/edit_file/'+param+'/" >'+item+'</a>'

		string.append('<li>'+li_name+'</li>')

		fullpath = os.path.join(dir, item)
		if os.path.isdir(fullpath):
			traverse(fullpath)
	string.append('</ul>')

def show_dir(request, file_name):
	path = '/home/kalyan/djangoprojects/apkDecompiler/decompile/apkfiles/'+file_name+'/'
	traverse(path)
	return render(request, 'decompile/show_dir.html', {'final_list':''.join(string)})

def edit_file(request, file_path):
	file1 = file_path.replace("+","/")
	file1 = file1.replace("*", ".")
	file_extn = file1[file1.find(".")+1:]

	with open(file1, 'r') as content_file:
		content = content_file.read()

	return render(request, 'decompile/edit_file.html', { 'content':str(content), 'file_extn':file_extn })