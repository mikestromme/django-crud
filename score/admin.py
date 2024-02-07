from django.contrib import admin
from score.models import Score

# show all columns in the admin console instead of just 
# the name which line 10 does if this isn't included
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']


admin.site.register(Score, ScoreAdmin)
