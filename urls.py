from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "blog"

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.post_list, name="post_list"),
    path('posts/<str:category>', views.post_list, name="post_list_category"),
    # path('posts/', views.PostListView.as_view(), name="post_list"),
    path('posts/detail/<post_id>', views.post_detail, name="post_detail"),
    # path('posts/<pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('Ticket/', views.ticket, name="ticket"),
    path('posts/<post_id>/comment', views.post_comment, name="post_comment"),
    path('search/', views.post_search, name="post_search"),
    path('profile/', views.profile, name="profile"),
    path('profile/create_post', views.create_post, name="create_post"),
    path('profile/create_post/<post_id>', views.edit_post, name="edit_post"),
    path('profile/delete_post/<post_id>', views.delete_post, name="delete_post"),
    path('profile/delete_image/<image_id>', views.delete_image, name="delete_image"),
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
    path('password-change/',auth_view.PasswordChangeView.as_view(success_url="done"),name="password_change"),
    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(), name="password_change-done"),
    path('password-reset/', auth_view.PasswordResetView.as_view(success_url="done"), name="password_reset"),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(success_url="/blog/password-reset/complete"), name="password_reset_confirm"),
    path('password-reset/complete/', auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('register/', views.register, name="register"),
    path('account-edit/',views.edit_user,name="user_edit"),
    path('user-information/<user_id>', views.user_information, name="user_information"),
]
