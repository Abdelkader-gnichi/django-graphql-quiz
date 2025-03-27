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

    all_questions = graphene.List(QuestionType)

    quiz_by_id = graphene.Field(QuizType, id=graphene.UUID())
    
    question_by_id = graphene.Field(QuestionType, id=graphene.UUID())

    answers_by_question_id = graphene.List(AnswerType, id=graphene.UUID())


    
    def resolve_quiz_by_id(root, info, id):
        return Quiz.objects.get(id=id)
    
    def resolve_all_questions(root, info):
        return Question.objects.all()
   
    def resolve_question_by_id(root, info, id):
        return Question.objects.get(id=id)
    
    def resolve_answers_by_question_id(root, info, id):
        return Answer.objects.filter(question__id=id)


class CreateCategory(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        # category = Category.objects.create(name=name)
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)

class Mutation(graphene.ObjectType):

    create_category =  CreateCategory.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)