"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import url
from aplikacja.views import CurrentRatioAddView, QuickRatioView, CashRatioView, AddCompanyView, CompanyView, \
    CurrentRatioResultView, CurrentRatioView, QuickRatioAddView, QuickRatioResultView, CashRatioAddView, \
    CashRatioResultView, ReturnOnAssetsView, ROAAddView, ReturnOnAssetsResultView, ReturnOnSalesView, \
    ROSAddView, ReturnOnSalesResultView, ReturnOnEquityView, ROEAddView, ReturnOnEquityResultView, \
    contact_view, success_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^cash_ratio', CashRatioView.as_view(), name="cash-ratio-view"),
    url(r'^quick_ratio', QuickRatioView.as_view(), name="quick-ratio-view"),
    url(r'^add_company', AddCompanyView.as_view(), name="add-company-view"),
    url(r'^company/(?P<company_id>(\d)+)', CompanyView.as_view()),
    url(r'^current_ratio', CurrentRatioView.as_view(), name="current-ratio-view"),
    url(r'^add_current_ratio', CurrentRatioAddView.as_view(), name="current-ratio-add-view"),
    url(r'^result_current_ratio/(?P<current_ratio_id>(\d)+)', CurrentRatioResultView.as_view(),
        name="current-ratio-result-view"),
    url(r'^quick_ratio', QuickRatioView.as_view(), name="quick-ratio-view"),
    url(r'^add_quick_ratio', QuickRatioAddView.as_view(), name="quick-ratio-add-view"),
    url(r'^result_quick_ratio/(?P<quick_ratio_id>(\d)+)', QuickRatioResultView.as_view(),
        name="quick-ratio-result-view"),
    url(r'^cash_ratio', CashRatioView.as_view(), name="cash-ratio-view"),
    url(r'^add_cash_ratio', CashRatioAddView.as_view(), name="cash-ratio-add-view"),
    url(r'^result_cash_ratio/(?P<cash_ratio_id>(\d)+)', CashRatioResultView.as_view(),
        name="cash-ratio-result-view"),
    url(r'^return_on_assets', ReturnOnAssetsView.as_view(), name="return-on-assets-view"),
    url(r'^roa_add', ROAAddView.as_view(), name="roa-add-view"),
    url(r'^result_return_on_assets/(?P<return_on_assets_id>(\d)+)', ReturnOnAssetsResultView.as_view(),
        name="return-on-assets-result-view"),
    url(r'^return_on_equity', ReturnOnEquityView.as_view(), name="return-on-equity-view"),
    url(r'^roe_add', ROEAddView.as_view(), name="roe-add-view"),
    url(r'^result_return_on_equity/(?P<return_on_equity_id>(\d)+)', ReturnOnEquityResultView.as_view(),
        name="return-on-equity-result-view"),
    url(r'^return_on_sales', ReturnOnSalesView.as_view(), name="return-on-sales-view"),
    url(r'^ros_add', ROSAddView.as_view(), name="ros-add-view"),
    url(r'^result_return_on_sales/(?P<return_on_sales_id>(\d)+)', ReturnOnSalesResultView.as_view(),
        name="return-on-sales-result-view"),
    url(r'^all_analysis$', TemplateView.as_view(template_name='all_analysis.html')),
    url(r'^contact$', contact_view, name="contact"),
    url(r'^faq$', TemplateView.as_view(template_name='faq.html')),
    url(r'^success', success_view, name="success"),

]
