from django.contrib import admin

from.models import Ingredient, RecipeIngredient, Recipe, Tag


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    autocomplete_fields = ('ingredient',)
    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('ingredient')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'tags_list',
        'cooking_time'
    )
    search_fields = (
        'name',
        'author__first_name',
        'author__last_name',
        'author__username',
    )
    list_filter = ('tags',)
    autocomplete_fields = ('author', 'tags',)
    inlines = [RecipeIngredientInline]

    def tags_list(self, obj):
        if tags := obj.tags.all():
            tags_list = ', '.join([tag.name for tag in tags[:2]])
            if len(tags) > 2:
                tags_list += f' и еще {len(tags) - 2}'
            return tags_list

    tags_list.short_description = 'Теги'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color',)
    search_fields = ('name', )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    search_fields = ('name',)




