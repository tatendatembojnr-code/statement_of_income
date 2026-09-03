from odoo import models, fields

class AccountAccount(models.Model):
    _inherit = 'account.account'

    comprehensive_income_category = fields.Selection([
        ('insurance_revenue', 'Insurance Revenue'),
        ('insurance_service_expenses', 'Insurance Service Expenses'),
        ('investment_income', 'Investment Income'),
        ('net_insurance_finance_expenses', 'Net Insurance Finance Expenses'),
        ('finance_cost', 'Finance Cost'),
        ('operating_expenses', 'Operating Expenses'),
        ('income_tax', 'Income Tax Expense'),
        ('other_comprehensive_income', 'Other Comprehensive Income'),
    ], string="Statement of Comp. Income Category")
