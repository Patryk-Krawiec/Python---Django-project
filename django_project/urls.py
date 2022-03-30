from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rejestracja/', user_view.register, name='register'),
    path('profil/', user_view.profile, name='profile'),
    path('logowanie/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('wyloguj/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('hasło-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('hasło-reset/gotowe/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('hasło-reset-potwierdz/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('hasło-reset-sukces/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)