from django.urls import re_path

from chatapp.consumer import chatting


websocket_urlpatterns=[
    re_path(r"ws/chat/(?P<room_name>\w+)/$",chatting.as_asgi()),
]