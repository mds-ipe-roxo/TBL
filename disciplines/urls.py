from django.conf.urls import url
from . import views

app_name = 'disciplines'
urlpatterns = [
    # /profile/create_discipline/
    url(
        r'^profile/create-discipline/$',
        views.DisciplineCreationView.as_view(),
        name='create'
    ),
    # /profile/list-discipline/
    url(
        r'^profile/list-discipline/$',
        views.DisciplineListSearchView.as_view(),
        name='search'
    ),
    # /profile/update-discipline/discipline-name
    url(
        r'^profile/update-discipline/(?P<slug>[\w_-]+)/$',
        views.DisciplineUpdateView.as_view(),
        name='update'
    ),
    # /profile/delete-discipline/discipline-name
    url(
        r'^profile/delete-discipline/(?P<slug>[\w_-]+)/$',
        views.DisciplineDeleteView.as_view(),
        name='delete'
    ),
    # /profile/enter-discipline/discipline-name
    url(
        r'^profile/enter-discipline/(?P<slug>[\w_-]+)/$',
        views.DisciplineListSearchView.as_view(),
        name='enter'
    ),
    # /profile/discipline-name/
    url(
        r'^profile/(?P<slug>[\w_-]+)/$',
        views.ShowDisciplineView.as_view(),
        name='details'
    ),
    # /profile/discipline-name/student-list/
    url(
        r'^profile/(?P<slug>[\w_-]+)/students/$',
        views.StudentListView.as_view(),
        name='students'
    ),
]
