from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.


class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Quiz(BaseModel):

    title = models.CharField(max_length=255, default=_("New Quiz"))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title}'
    

SCALE = {
    0: _('Fundamental'),
    1: _('Beginner'),
    2: _('Intermediate'),
    3: _('Advanced'),
    4: _('Expert')
}

TYPE = {
    0: _('Multiple Choices'),
    1: _('Single Choice')
}

class Question(BaseModel):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_('Type of Question'))
    difficulty = models.IntegerField(choices=SCALE, default=0,verbose_name=_('Difficulty Level'))
    is_active = models.BooleanField(verbose_name=_('Active Status'))

    def __str__(self):
        return f'{self.title}'
    

class Answer(BaseModel):

    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='answers')

    answer_text = models.TextField(verbose_name=_("Answer Text"))
    is_right = models.BooleanField()

    def __str__(self):
        return f'{self.answer_text}'
    