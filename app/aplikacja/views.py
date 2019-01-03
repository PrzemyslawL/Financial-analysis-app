from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from aplikacja.forms import CurrentRatioAddForm, AddCompanyForm, QuickRatioAddForm, CashRatioAddForm, \
    ROAAddForm, ROEAddForm, ROSAddForm, ExamplesForm, ContactForm
from .models import Company, CurrentRatio, QuickRatio, CashRatio, ReturnOnEquity, ReturnOnAssets, ReturnOnSales
from django.core.mail import send_mail, BadHeaderError


class CompanyView(View):
    def get(self, request, company_id):
        company_name = Company.objects.get(id=company_id)

        ctx = {
            'company_name': company_name,
        }
        return render(request, "company.html", ctx)


class AddCompanyView(View):
    def get(self, request):
        form = AddCompanyForm()
        ctx = {
            "form": form
        }
        return render(request, "add_company.html", ctx)

    def post(self, request):
        form = AddCompanyForm(request.POST)
        if form.is_valid():

            company_name = Company.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("add_company.html")

        else:
            ctx = {'form': form}
            return render(request, 'add_company.html', ctx)


class CurrentRatioAddView(View):
    def get(self, request):
        form = CurrentRatioAddForm()
        ctx = {'form': form}
        return render(request, 'add_current_ratio.html', ctx)

    def post(self, request):
        form = CurrentRatioAddForm(request.POST)
        if form.is_valid():
            current_ratio = form.save(commit=False)
            current_ratio.current_ratio = current_ratio.current_assets / current_ratio.current_liabilities
            current_ratio.save()
            return HttpResponseRedirect("result_current_ratio/{}".format(current_ratio.id))
        return render(request, 'add_current_ratio.html', {'form': form})


class QuickRatioAddView(View):
    def get(self, request):
        form = QuickRatioAddForm()
        ctx = {'form': form}
        return render(request, 'add_quick_ratio.html', ctx)

    def post(self, request):
        form = QuickRatioAddForm(request.POST)
        if form.is_valid():
            quick_ratio = form.save(commit=False)
            quick_ratio.quick_ratio = (quick_ratio.cash + quick_ratio.marketable_securities +
                                       quick_ratio.accounts_receivable) / quick_ratio.current_liabilities
            quick_ratio.save()
            return HttpResponseRedirect("result_quick_ratio/{}".format(quick_ratio.id))
        return render(request, 'add_quick_ratio.html', {'form': form})


class CashRatioAddView(View):
    def get(self, request):
        form = CashRatioAddForm()
        ctx = {'form': form}
        return render(request, 'add_cash_ratio.html', ctx)

    def post(self, request):
        form = CashRatioAddForm(request.POST)
        if form.is_valid():
            cash_ratio = form.save(commit=False)
            cash_ratio.cash_ratio = cash_ratio.cash / cash_ratio.current_liabilities
            cash_ratio.save()
            return HttpResponseRedirect("result_cash_ratio/{}".format(cash_ratio.id))
        return render(request, 'add_cash_ratio.html', {'form': form})


class CurrentRatioResultView(View):
    def get(self, request, current_ratio_id):
        current_ratio_id = CurrentRatio.objects.get(id=current_ratio_id)

        ctx = {'current_ratio': current_ratio_id}
        return render(request, 'result_current_ratio.html', ctx)


class QuickRatioResultView(View):
    def get(self, request, quick_ratio_id):
        quick_ratio_id = QuickRatio.objects.get(id=quick_ratio_id)

        ctx = {'quick_ratio': quick_ratio_id}
        return render(request, 'result_quick_ratio.html', ctx)


class CashRatioResultView(View):
    def get(self, request, cash_ratio_id):
        cash_ratio_id = CashRatio.objects.get(id=cash_ratio_id)

        ctx = {'cash_ratio': cash_ratio_id}
        return render(request, 'result_cash_ratio.html', ctx)


class CurrentRatioView(View):
    def get(self, request):
        form = ExamplesForm()
        ctx = {'form': form}
        return render(request, 'current_ratio.html', ctx)

    def post(self, request):
        form = ExamplesForm(request.POST)
        if form.is_valid():
            year_from = form.cleaned_data['year_from']
            year_to = form.cleaned_data['year_to']
            company = form.cleaned_data['company_name']
            current_ratio = CurrentRatio.objects.filter(year__gte=year_from, year__lte=year_to, company_name=company)
            ctx = {'current_ratio': current_ratio}
            return render(request, 'current_ratio.html', ctx)


class QuickRatioView(View):
    def get(self, request):
        form = ExamplesForm()
        ctx = {'form': form}
        return render(request, 'quick_ratio.html', ctx)

    def post(self, request):
        form = ExamplesForm(request.POST)
        if form.is_valid():
            year_from = form.cleaned_data['year_from']
            year_to = form.cleaned_data['year_to']
            company = form.cleaned_data['company_name']
            quick_ratio = QuickRatio.objects.filter(year__gte=year_from, year__lte=year_to, company_name=company)
            ctx = {'quick_ratio': quick_ratio}
            return render(request, 'quick_ratio.html', ctx)


class CashRatioView(View):
    def get(self, request):
        form = ExamplesForm()
        ctx = {'form': form}
        return render(request, 'cash_ratio.html', ctx)

    def post(self, request):
        form = ExamplesForm(request.POST)
        if form.is_valid():
            year_from = form.cleaned_data['year_from']
            year_to = form.cleaned_data['year_to']
            company = form.cleaned_data['company_name']
            cash_ratio = CashRatio.objects.filter(year__gte=year_from, year__lte=year_to, company_name=company)
            ctx = {'cash_ratio': cash_ratio}
            return render(request, 'cash_ratio.html', ctx)


class ROAAddView(View):
    def get(self, request):
        form = ROAAddForm()
        ctx = {'form': form}
        return render(request, 'roa_add.html', ctx)

    def post(self, request):
        form = ROAAddForm(request.POST)
        if form.is_valid():
            return_on_assets = form.save(commit=False)
            return_on_assets.return_on_assets = return_on_assets.net_income / return_on_assets.total_assets
            return_on_assets.save()
            return HttpResponseRedirect("result_return_on_assets/{}".format(return_on_assets.id))
        return render(request, 'roa_add.html', {'form': form})


class ROEAddView(View):
    def get(self, request):
        form = ROEAddForm()
        ctx = {'form': form}
        return render(request, 'roe_add.html', ctx)

    def post(self, request):
        form = ROEAddForm(request.POST)
        if form.is_valid():
            return_on_equity = form.save(commit=False)
            return_on_equity.return_on_equity = return_on_equity.net_income / return_on_equity.equity
            return_on_equity.save()
            return HttpResponseRedirect("result_return_on_equity/{}".format(return_on_equity.id))
        return render(request, 'roe_add.html', {'form': form})


class ROSAddView(View):
    def get(self, request):
        form = ROSAddForm()
        ctx = {'form': form}
        return render(request, 'ros_add.html', ctx)

    def post(self, request):
        form = ROSAddForm(request.POST)
        if form.is_valid():
            return_on_sales = form.save(commit=False)
            return_on_sales.return_on_sales = return_on_sales.net_income / return_on_sales.net_sales
            return_on_sales.save()
            return HttpResponseRedirect("result_return_on_sales/{}".format(return_on_sales.id))
        return render(request, 'ros_add.html', {'form': form})


class ReturnOnAssetsResultView(View):
    def get(self, request, return_on_assets_id):
        return_on_assets_id = ReturnOnAssets.objects.get(id=return_on_assets_id)

        ctx = {'return_on_assets': return_on_assets_id}
        return render(request, 'result_return_on_assets.html', ctx)


class ReturnOnEquityResultView(View):
    def get(self, request, return_on_equity_id):
        return_on_equity_id = ReturnOnEquity.objects.get(id=return_on_equity_id)

        ctx = {'return_on_equity': return_on_equity_id}
        return render(request, 'result_return_on_equity.html', ctx)


class ReturnOnSalesResultView(View):
    def get(self, request, return_on_sales_id):
        return_on_sales_id = ReturnOnSales.objects.get(id=return_on_sales_id)

        ctx = {'return_on_sales': return_on_sales_id}
        return render(request, 'result_return_on_sales.html', ctx)


class ReturnOnAssetsView(View):
    def get(self, request):
        form = ExamplesForm()
        ctx = {'form': form}
        return render(request, 'return_on_assets.html', ctx)

    def post(self, request):
        form = ExamplesForm(request.POST)
        if form.is_valid():
            year_from = form.cleaned_data['year_from']
            year_to = form.cleaned_data['year_to']
            company = form.cleaned_data['company_name']
            return_on_assets = ReturnOnAssets.objects.filter(year__gte=year_from, year__lte=year_to, company_name=company)
            ctx = {'return_on_assets': return_on_assets}
            return render(request, 'return_on_assets.html', ctx)


class ReturnOnEquityView(View):
    def get(self, request):
        form = ExamplesForm()
        ctx = {'form': form}
        return render(request, 'return_on_equity.html', ctx)

    def post(self, request):
        form = ExamplesForm(request.POST)
        if form.is_valid():
            year_from = form.cleaned_data['year_from']
            year_to = form.cleaned_data['year_to']
            company = form.cleaned_data['company_name']
            return_on_equity = ReturnOnEquity.objects.filter(year__gte=year_from, year__lte=year_to, company_name=company)
            ctx = {'return_on_equity': return_on_equity}
            return render(request, 'return_on_equity.html', ctx)


class ReturnOnSalesView(View):
    def get(self, request):
        form = ExamplesForm()
        ctx = {'form': form}
        return render(request, 'return_on_sales.html', ctx)

    def post(self, request):
        form = ExamplesForm(request.POST)
        if form.is_valid():
            year_from = form.cleaned_data['year_from']
            year_to = form.cleaned_data['year_to']
            company = form.cleaned_data['company_name']
            return_on_sales = ReturnOnSales.objects.filter(year__gte=year_from, year__lte=year_to, company_name=company)
            ctx = {'return_on_sales': return_on_sales}
            return render(request, 'return_on_sales.html', ctx)


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['przemyslaw.liszewski@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success_view(request):
    form = ContactForm()
    return render(request, "contact.html", {'form': form})
