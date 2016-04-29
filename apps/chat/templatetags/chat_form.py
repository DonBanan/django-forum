import datetime
from django.contrib.contenttypes.models import ContentType
from django import template
register = template.Library()

from ..forms import ChatForm


from ..models import Chat

@register.simple_tag(takes_context=True)
def chat_form(context, tpl='chat/chat_form.html'):
	request = context.get('request')
	chat_form = ChatForm(request.POST or None)
	if chat_form.is_valid():
		new_chat = chat_form.save(commit=False)
		new_chat.user = request.user
		new_chat.save()
		chat_form = ChatForm()
	context['chat_form'] = chat_form
	t = template.loader.get_template(tpl)
	return t.render(template.Context(context))
