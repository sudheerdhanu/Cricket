from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from CricketBlog.views import \
    (
    team_list,
    create_team,
    team_detail,
    create_player,
    main_page,
    fix_match,
    win,

)

urlpatterns = [
    path('', main_page,name='main_page'),
    path('team_list/', team_list,name='team_list'),
    path('create_team/', create_team,name='create_team'),
    path('create_player/', create_player,name='create_player'),
    path('fix_match/', fix_match,name='fix_match'),
    path('win/', win,name='win'),
    path('team_detail/(?P<id>\d+)/$',team_detail , name='team_detail'),
]