from django.urls import path
from . import views
 
app_name= "blog_app"

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('login/', views.login_user, name="login_user"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_user, name="logout_user"),
    path('about/', views.aboutpage, name="aboutpage"),
    path('contact/', views.contactpage, name="contactpage"),
    path('blog/', views.blogpage, name="blogpage"),
    path('<id>/', views.single_post, name="single_post"),
    path('add_comment/<post_id>/', views.add_comment, name="add_comment"),
    
     
    # path('about',views.aboutpage, name="aboutpage"),
]