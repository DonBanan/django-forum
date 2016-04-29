import datetime
from django.contrib.contenttypes.models import ContentType
from django import template
register = template.Library()

from ..forms import ChatForm


from ..models import Chat

@register.simple_tag(takes_context=True)
def chat_list(context, tpl='chat/chat_list.html'):
	context['now'] = datetime.datetime.now()
	chat_list = Chat.objects.all().order_by('-created_at')
	context['chat_list'] = chat_list
	t = template.loader.get_template(tpl)
	return t.render(template.Context(context))
