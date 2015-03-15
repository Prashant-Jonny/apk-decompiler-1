from django	import forms

class apkForm(forms.Form):
	apkfile = forms.FileField( label='upload your apk file here', help_text='only .apk files')
