from django.contrib import admin

from .models import Category, Subcategory, Post, Vote, TopicMessage, Moderated


class SubcategoryInline(admin.StackedInline):
	model = Subcategory
	extra = 0


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	inlines = [SubcategoryInline,]
admin.site.register(Category, CategoryAdmin)


admin.site.register(Post)

admin.site.register(Vote)

admin.site.register(TopicMessage)
admin.site.register(Moderated)