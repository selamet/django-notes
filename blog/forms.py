from django import forms
from .models import Blog


banned_email_list =['selamet@gmail.com','sassa@gmail.com','selo@gmail.com']

class IletisimForm(forms.Form):

    isim = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=50,label='isim',required=False)
    soyisim = forms.CharField(max_length=50,label='soyisim',required=False)
    email = forms.EmailField(max_length=50,label='email',required=True)
    email2 = forms.EmailField(max_length=50,label='email kontrol',required=True)
    icerik = forms.CharField(widget=forms.Textarea(attrs ={'class':'form-control'}),
                             max_length=1000,label='içerik')


    def __init__(self,*args,**kwargs):
        super(IletisimForm, self).__init__(*args,**kwargs) #kalıtım aldığı init fonksiyonları
        for field in self.fields:
           # print(field, self.fields[field])
            self.fields[field].widget.attrs={'class':'form-control'}
            self.fields['icerik'].widget=forms.Textarea(attrs={'class':'form-control'})
           # self.fields['icerik'] = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    def clean_isim(self):
        isim = self.cleaned_data.get('isim')
        if isim =='ahmet':
            raise forms.ValidationError('Lütfen ahmet dışında bir kullanıcı giriniz')
        return isim

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in banned_email_list:
            raise forms.ValidationError('lütfen banlı mail adresleri dışında mail giriniz')
        return email


    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email !=email2:
            #raise forms.ValidationError('emailler eşleşmedi')
            self.add_error('email','Emailler Eşleşmedi')
            self.add_error('email2', 'Emailler Eşleşmedi')


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields =['title','image','content','yayin_taslak','kategoriler'] # Blog modelindeki hangi alanları ile çalışacaksın

    def __init__(self,*args,**kwargs):
        super(BlogForm, self).__init__(*args,**kwargs) #kalıtım aldığı init fonksiyonları
        for field in self.fields:
           # print(field, self.fields[field])
            self.fields[field].widget.attrs={'class':'form-control'}
            self.fields['content'].widget=forms.Textarea(attrs={'class':'form-control'})


    def clean_content(self):
        icerik = self.cleaned_data.get('content')
        if len(icerik) <250:
            uzunluk =len(icerik)
            msg='Lütfen en az 250 karakter giriniz girilen karakter sayısı (%s)'%(uzunluk)
            raise forms.ValidationError(msg)
        return icerik


class PostSorugForm(forms.Form):
    YAYIN_TASLAK = [('all','HEPSİ'),('yayin','YAYIN'),('taslak','TASLAK')]
    search = forms.CharField(required=False,max_length=500, widget=forms.TextInput(attrs={'placeholder':'Bir şeyler arayınız',
                                                                                          'class':'form-control'}))
    taslak_yayin = forms.ChoiceField(label='', widget=forms.Select(attrs={'class':'form-control'}),
                                          choices=YAYIN_TASLAK,required=True)



