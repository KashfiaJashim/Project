from django.contrib import admin

from .models import Competition, SubmitCompetition, Review
# Register your models here.
admin.site.register(Competition)
admin.site.register(SubmitCompetition)
admin.site.register(Review)

