from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from web.views import account
from web.views import home
from web.views import asset
from web.views import business
from web.views import user
from web.views import idc
from web.views import tag


urlpatterns = [
    url(r'^login.html$', account.LoginView.as_view()),
    url(r'^logout.html$', account.LogoutView.as_view()),

    url(r'^$', home.IndexView.as_view()),
    url(r'^index.html$', home.IndexView.as_view()),
    url(r'^cmdb.html$', home.CmdbView.as_view()),


    # 资产管理
    url(r'^asset.html$', asset.AssetListView.as_view()),
    url(r'^assets.html$', asset.AssetJsonView.as_view()),
    url(r'^asset-(?P<device_type_id>\d+)-(?P<asset_nid>\d+).html$', asset.AssetDetailView.as_view()),
    url(r'^edit-asset-(?P<device_type_id>\d+)-(?P<asset_nid>\d+).html$', asset.AssetEditlView.as_view()),
    url(r'^add-asset.html$', asset.AddAssetView.as_view()),


    #  业务线管理
    url(r'^business.html$', business.BusinessListView.as_view()),
    url(r'^business-json.html$', business.BusinessJsonView.as_view()),

    #  IDC管理
    url(r'^idc.html$', idc.IdcListView.as_view()),
    url(r'^idc-json.html$', idc.IdcJsonView.as_view()),


    # 用户管理
    url(r'^users.html$', user.UserListView.as_view()),
    url(r'^user.html$', user.UserJsonView.as_view()),

    #  标签管理
    url(r'^tag.html$', tag.TagListView.as_view()),
    url(r'^tag-json.html$', tag.TagJsonView.as_view()),

    # 资产首页绘图信息
    url(r'^chart-(?P<chart_type>\w+).html$', home.ChartView.as_view()),
]