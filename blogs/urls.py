"""
URL configuration for blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from pro import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('newblog/',views.newblog,name='newblog'),
    path('about/',views.about,name='about'),
    path('index/',views.index,name='index'),
    path('myblogs/',views.myblogs,name='myblogs'),
    path('drafts/',views.drafts,name='drafts'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout_page/',views.logout_page,name='logout_page'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('LinkedIn/',views.LinkedIn,name='LinkedIn'),
    path('GitHub/',views.GitHub,name='GitHub'),
    path('delete_publish/<int:id>/',views.delete_publish,name='delete_publish'),
    # path('save_draft/<int:id>/<str:text>/', views.save_draft, name='save_draft'),
    path('save_draft/',views.save_draft, name='save_draft'),
    path('update_draft/<int:id>/', views.update_draft, name='update_draft'),
    path('download/<str:type>/', views.download, name='download'),
    path('delete_draft/<int:id>/',views.delete_draft,name='delete_draft'),
    path('publish_draft/<int:id>/',views.publish_draft,name='publish_draft'),
    path('edit_publish/<int:id>/',views.edit_publish,name='edit_publish'),
    path('icon_publish/<int:id>/<str:icon>/',views.icon_publish,name='icon_publish')
]
