from django import template

register = template.Library()


@register.filter
def is_recipient(post, user):
    return post.recipient.filter(id=user.profile.id).exists()