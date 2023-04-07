from django.contrib import admin
from .models import User,Movie,Song,UserProfile,signup,signin

admin.site.register(User),
admin.site.register(Movie),
admin.site.register(Song),
admin.site.register(UserProfile),
admin.site.register(signup),
admin.site.register(signin),
