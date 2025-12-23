from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #para cada pagina uma rota é necessaria, determinamos a rota em path, a function pra acesso em view
    # e no html o {% url 'cads' %} para acesso
    path('', views.index,name='index'),
    path('templates/cads.html', views.cads,name='cads'),
    path('template/login.html', views.login,name='login'),
    path('template/home_user.html', views.home_user,name='home_user')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


