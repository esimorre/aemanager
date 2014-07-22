from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',

    # expenses
    url(regex=r'^expenses/$',
        view='expense_list',
        name='expense_list'),
    url(regex=r'^expenses/add/$',
        view='expense_add',
        name='expense_add'),
    url(regex=r'^expenses/edit/$',
        view='expense_edit',
        name='expense_edit'),
    url(regex=r'^expenses/delete/$',
        view='expense_delete',
        name='expense_delete'),
    url(regex=r'^expenses/list_export/$',
        view='expense_list_export',
        name='expense_list_export'),

    # invoices
    url(regex=r'^invoice/$',
        view='invoice_list',
        name='invoice_list'),
    url(regex=r'^invoice/list_export/$',
        view='invoice_list_export',
        name='invoice_list_export'),
    url(regex=r'^invoice/add/$',
        view='invoice_create_or_edit',
        name='invoice_add_without_proposal'),
    url(regex=r'^invoice/add/(?P<customer_id>\d+)/$',
        view='invoice_create_or_edit',
        name='invoice_add'),
    url(regex=r'^invoice/add/(?P<customer_id>\d+)/(?P<proposal_id>\d+)/$',
        view='invoice_create_or_edit',
        name='invoice_add_from_proposal'),
    url(regex=r'^invoice/edit/(?P<id>\d+)/$',
        view='invoice_create_or_edit',
        name='invoice_edit'),
    url(regex=r'^invoice/(?P<id>\d+)/$',
        view='invoice_detail',
        name='invoice_detail'),
    url(regex=r'^invoice/delete/(?P<id>\d+)/$',
        view='invoice_delete',
        name='invoice_delete'),
    url(regex=r'^invoice/download/(?P<id>\d+)/$',
        view='invoice_download',
        name='invoice_download'),
    url(regex=r'^invoice/proposals/$',
        view='invoice_proposals',
        name='invoice_proposals'),

)
