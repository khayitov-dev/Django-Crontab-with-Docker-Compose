from .models import Text

def add_text():
    Text.objects.create(text='this is text')