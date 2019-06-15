from django import forms

from .models import Area, Yurukai


class YurukaiForm(forms.ModelForm):
    # name = forms.CharField(label="ゆる会名", max_length=100)
    # area = forms.ModelChoiceField(Area.objects.all())

    class Meta:
        model = Yurukai
        fields = ["name", "tag", "area"]
