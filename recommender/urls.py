from django.urls import path, include
from .views import index, start_page, portrait_landscape_view, friend_or_snapshot_view, everything_view, portrait_landscape_fixed_lens, portrait_landscape_interchangeable_lens, pentax_iq_view, olympus_stylus_view, konica_bigmini_view

urlpatterns = [
    path('', index, name='home'),
    path('start', start_page, name='home'),
    path('p1', portrait_landscape_view, name='p1'),
    path('p2', friend_or_snapshot_view, name='p2'),
    path('minolta_himatic', everything_view, name='p3'),
    path('p1/1', portrait_landscape_fixed_lens, name='p1/1'),
    path('p1/2', portrait_landscape_interchangeable_lens, name='p1/2'),
    path('pentax_iq', pentax_iq_view),
    path('olympus_stylus', olympus_stylus_view),
    path('konica_bigmini', konica_bigmini_view),
]

