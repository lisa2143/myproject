from django.contrib import admin
from .models import BoardModel
from .models import Comment
from .models import Reply

# Register your models here.
admin.site.register(BoardModel)
