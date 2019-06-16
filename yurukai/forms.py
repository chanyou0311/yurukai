from django import forms

from bootstrap_datepicker_plus import DateTimePickerInput

from .models import Area, Yurukai, Schedule


class ModelFormWithFormSetMixin:
    def __init__(self, *args, **kwargs):
        super(ModelFormWithFormSetMixin, self).__init__(*args, **kwargs)
        self.formset = self.formset_class(
            instance=self.instance, data=self.data if self.is_bound else None
        )

    def is_valid(self):
        return (
            super(ModelFormWithFormSetMixin, self).is_valid()
            and self.formset.is_valid()
        )

    def save(self, commit=True):
        saved_instance = super(ModelFormWithFormSetMixin, self).save(commit)
        self.formset.save(commit)
        return saved_instance


class ScheduleForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        widget=DateTimePickerInput(format="%Y/%m/%d %H:%M"),
        input_formats=["%Y/%m/%d %H:%M"],
    )
    end_time = forms.DateTimeField(
        widget=DateTimePickerInput(format="%Y/%m/%d %H:%M"),
        input_formats=["%Y/%m/%d %H:%M"],
    )

    class Meta:
        model = Schedule
        fields = ["yurukai", "start_time", "end_time"]


ScheduleFormSet = forms.inlineformset_factory(
    parent_model=Yurukai, model=Schedule, form=ScheduleForm, extra=5
)


class YurukaiForm(ModelFormWithFormSetMixin, forms.ModelForm):
    formset_class = ScheduleFormSet
    name = forms.CharField(label="ゆる会名", max_length=100)
    area = forms.ModelChoiceField(Area.objects.all())

    class Meta:
        model = Yurukai
        fields = ["name", "tag", "area"]
