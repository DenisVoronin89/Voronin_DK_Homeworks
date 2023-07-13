from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from mainapp.views import index_view, IngredientListView, IngredientDetailView, HomeView
# from userapp.views import RegisterView,

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path("", index_view),
    path('__debug__/', include('debug_toolbar.urls')),
    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_detail'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('register/', RegisterView.as_view()),
    # path('user/profile/', user_profile_view, name='user_profile'),
]

# URL для статических файлов, только для режима разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)