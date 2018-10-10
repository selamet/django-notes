from django import forms


banned_email_list =['selamet@gmail.com','sassa@gmail.com','selo@gmail.com']

class IletisimForm(forms.Form):
    isim = forms.CharField(max_length=50,label='isim',required=False)
    soyisim = forms.CharField(max_length=50,label='soyisim',required=False)
    email = forms.EmailField(max_length=50,label='email',required=True)
    email2 = forms.EmailField(max_length=50,label='email kontrol',required=True)
    icerik = forms.CharField(max_length=1000,label='içerik')


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