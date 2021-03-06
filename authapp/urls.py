from django.urls import path, include
from .views import ShopLoginView, ShopLogoutView, ShopPasswordChangeView, ShopPasswordChangeDoneView, ShopUserView, \
    RegistrationUserView, SelfUserDetailView, SelfUserUpdateView, ManagerUserUpdateView, ManagerUserDetailView, \
    ManagerUserListView, CustomerUserDetailView

app_name = 'auth'
urlpatterns = [
    path('login/', ShopLoginView.as_view(), name='log_in'),
    path('logout/', ShopLogoutView.as_view(), name='log_out'),
    path('password_change/', ShopPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', ShopPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('user/', SelfUserDetailView.as_view(), name='user'),
    path('register/', RegistrationUserView.as_view(), name='register'),
    path('user/update/', SelfUserUpdateView.as_view(), name='user_update'),
    path('man/user/', ManagerUserListView.as_view(), name='manager_user_list'),
    path('man/user/<int:pk>/', ManagerUserDetailView.as_view(), name='manager_user_detail'),
    path('man/user/<int:pk>/update/', ManagerUserUpdateView.as_view(), name='manager_user_update'),
    path('<int:pk>/', CustomerUserDetailView.as_view(), name='customer_user_detail'),
]
