from django import forms
from .models import Company, CurrentRatio, QuickRatio, CashRatio, ReturnOnAssets, ReturnOnEquity, ReturnOnSales, \
    DebtRatio, EquityRatio, DebtToEquityRatio

YEAR = (
    ('2000', '2000'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
)


class AddCompanyForm (forms.Form):
    company_name = forms.CharField(max_length=128)
    street = forms.CharField(max_length=64)
    city = forms.CharField(max_length=64)


class CurrentRatioAddForm(forms.ModelForm):
    class Meta:
        model = CurrentRatio
        exclude = ['current_ratio']


class QuickRatioAddForm(forms.ModelForm):
    class Meta:
        model = QuickRatio
        exclude = ['quick_ratio']


class CashRatioAddForm(forms.ModelForm):
    class Meta:
        model = CashRatio
        exclude = ['cash_ratio']


class ROAAddForm (forms.ModelForm):
    class Meta:
        model = ReturnOnAssets
        exclude = ['return_on_assets']


class ROEAddForm (forms.ModelForm):
    class Meta:
        model = ReturnOnEquity
        exclude = ['return_on_equity']


class ROSAddForm (forms.ModelForm):
    class Meta:
        model = ReturnOnSales
        exclude = ['return_on_sales']


class DebtRatioAddForm(forms.ModelForm):
    class Meta:
        model = DebtRatio
        exclude = ['debt_ratio']


class EquityRatioAddForm(forms.ModelForm):
    class Meta:
        model = EquityRatio
        exclude = ['equity_ratio']


class DebtToEquityRatioAddForm(forms.ModelForm):
    class Meta:
        model = DebtToEquityRatio
        exclude = ['debt_to_equity_ratio']


class ExamplesForm(forms.Form):
    company_name = forms.ModelChoiceField(queryset=Company.objects.all())
    year_from = forms.ChoiceField(choices=YEAR)
    year_to = forms.ChoiceField(choices=YEAR)


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, max_length=64)
    subject = forms.CharField(required=True, max_length=32)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=256)

