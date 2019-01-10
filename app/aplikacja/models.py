from django.db import models


class Company (models.Model):
    company_name = models.CharField(max_length=128, unique=True)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.company_name


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


class CurrentRatio (models.Model):
    current_ratio = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    current_assets = models.DecimalField(max_digits=10, decimal_places=3)
    current_liabilities = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.current_ratio


class QuickRatio (models.Model):
    quick_ratio = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    cash = models.DecimalField(max_digits=10, decimal_places=3)
    marketable_securities = models.DecimalField(max_digits=10, decimal_places=3)
    accounts_receivable = models.DecimalField(max_digits=10, decimal_places=3)
    current_liabilities = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.quick_ratio


class CashRatio (models.Model):
    cash_ratio = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    cash = models.DecimalField(max_digits=10, decimal_places=3)
    current_liabilities = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.cash_ratio


class ReturnOnAssets (models.Model):
    return_on_assets = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    net_income = models.DecimalField(max_digits=10, decimal_places=3)
    total_assets = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.return_on_assets


class ReturnOnEquity (models.Model):
    return_on_equity = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    net_income = models.DecimalField(max_digits=10, decimal_places=3)
    equity = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.return_on_equity


class ReturnOnSales (models.Model):
    return_on_sales = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    net_income = models.DecimalField(max_digits=10, decimal_places=3)
    net_sales = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.return_on_sales


class DebtRatio (models.Model):
    debt_ratio = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    total_liabilities = models.DecimalField(max_digits=10, decimal_places=3)
    total_assets = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.debt_ratio


class EquityRatio (models.Model):
    equity_ratio = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    total_equity = models.DecimalField(max_digits=10, decimal_places=3)
    total_assets = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.equity_ratio


class DebtToEquityRatio (models.Model):
    debt_to_equity_ratio = models.DecimalField(max_digits=10, decimal_places=3)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.CharField(max_length=64, choices=YEAR, default="2018")
    total_liabilities = models.DecimalField(max_digits=10, decimal_places=3)
    total_equity = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        unique_together = ('company_name', 'year')

    def __str__(self):
        return self.debt_to_equity_ratio
