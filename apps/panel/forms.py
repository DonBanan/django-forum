# coding: utf-8
from django import forms
from ..blog.models import Category, Subcategory


class AddCategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['title', 'short_description', 'slug']


class AddSubcategoryForm(forms.ModelForm):
	class Meta:
		model = Subcategory
		fields = ['category', 'title', 'slug']