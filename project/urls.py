from django.conf.urls import patterns, url

urlpatterns = patterns('project.views',

    # contracts
    url(regex=r'^contract/add/(?P<contact_id>\d+)/$',
        view='contract_create_or_edit',
        name='contract_add'),
    url(regex=r'^contract/edit/(?P<id>\d+)/$',
        view='contract_create_or_edit',
        name='contract_edit'),
    url(regex=r'^contract/(?P<id>\d+)/$',
        view='contract_detail',
        name='contract_detail'),
    url(regex=r'^contract/delete/(?P<id>\d+)/$',
        view='contract_delete',
        name='contract_delete'),
    url(regex=r'^contract/download/(?P<id>\d+)/$',
        view='contract_download',
        name='contract_download'),
    url(regex=r'^contract/uploaded_contract_download/(?P<id>\d+)/$',
        view='contract_uploaded_contract_download',
        name='contract_uploaded_contract_download'),
    url(regex=r'^contract/ajax/$',
        view='contract_get_content',
        name='contract_get_content'),

    # projects
    url(regex=r'^add/$',
        view='project_create_or_edit',
        name='project_add'),
    url(regex=r'^edit/(?P<id>\d+)/$',
        view='project_create_or_edit',
        name='project_edit'),
    url(regex=r'^(?P<id>\d+)/$',
        view='project_detail',
        name='project_detail'),
    url(regex=r'^running_list/$',
        view='project_running_list',
        name='project_running_list'),
    url(regex=r'^finished_list/$',
        view='project_finished_list',
        name='project_finished_list'),
    url(regex=r'^delete/(?P<id>\d+)/$',
        view='project_delete',
        name='project_delete'),

    # proposals
    url(regex=r'^proposal/add/(?P<project_id>\d+)/$',
        view='proposal_create_or_edit',
        name='proposal_add'),
    url(regex=r'^proposal/edit/(?P<id>\d+)/$',
        view='proposal_create_or_edit',
        name='proposal_edit'),
    url(regex=r'^proposal/(?P<id>\d+)/$',
        view='proposal_detail',
        name='proposal_detail'),
    url(regex=r'^proposal/delete/(?P<id>\d+)/$',
        view='proposal_delete',
        name='proposal_delete'),
    url(regex=r'^proposal/change_state/(?P<id>\d+)/$',
        view='proposal_change_state',
        name='proposal_change_state'),
    url(regex=r'^proposal/download/(?P<id>\d+)/$',
        view='proposal_download',
        name='proposal_download'),
    url(regex=r'^proposal/contract_download/(?P<id>\d+)/$',
        view='proposal_contract_download',
        name='proposal_contract_download'),
    url(regex=r'^proposal/uploaded_contract_download/(?P<id>\d+)/$',
        view='proposal_uploaded_contract_download',
        name='proposal_uploaded_contract_download'),
    url(regex=r'^proposal/contract/ajax/$',
        view='proposal_get_contract',
        name='proposal_get_contract'),

    # catalog
    url(regex=r'^catalog/$',
        view='catalog_list',
        name='catalog_list'),
    url(regex=r'^catalog/add/$',
        view='catalog_add',
        name='catalog_add'),
    url(regex=r'^catalog/section_search/$',
        view='catalog_section_search',
        name='catalog_section_search'),
    url(regex=r'^catalog/item_search/$',
        view='catalog_item_search',
        name='catalog_item_search'),
    url(regex=r'^catalog/edit/$',
        view='catalog_edit',
        name='catalog_edit'),
    url(regex=r'^catalog/delete/$',
        view='catalog_delete',
        name='catalog_delete'),
    url(regex=r'^catalog/move/$',
        view='catalog_move',
        name='catalog_move'),
    url(regex=r'^catalog/section_rename/$',
        view='catalog_section_rename',
        name='catalog_section_rename'),
    url(regex=r'^catalog/section_delete/$',
        view='catalog_section_delete',
        name='catalog_section_delete'),
)
