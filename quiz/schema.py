import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Quiz, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = '__all__'


class Query(graphene.ObjectType):

    all_quiz = DjangoListField(QuizType)
    
    all_questions = DjangoListField(QuestionType)

   


schema = graphene.Schema(query=Query)