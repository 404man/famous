import graphene
from graphene_django.types import DjangoObjectType

from .models import Question, Choice

# 定义类型
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice


# 定义动作，类似POST, PUT, DELETE

# class QuestionInput(graphene.InputObjectType):
#     question_text = graphene.String(required=True)

# class CreateQuestion(graphene.Mutation):
#     # api的输入参数
#     class Arguments:
#         question_data = QuestionInput(required=True)

#     # api的响应参数
#     ok = graphene.Boolean()
#     question = graphene.Field(QuestionType)

#     # api的相应操作，这里是create
#     def mutate(self, info,  question_data):
#         question_text = Question.objects.create(question_text=question_data['question_text'])
#         ok = True
#         return CreateQuestion()

  
class Query(object):
    question = graphene.Field(QuestionType, id=graphene.Int())
    all_questions = graphene.List(QuestionType)

    choice = graphene.Field(ChoiceType, id=graphene.Int())
    all_choices = graphene.List(ChoiceType)

    # get one
    def resolve_question(self, context, id=None):
        if id is not None:
            return Question.objects.get(pk=id)
    def resolve_choice(self, context, id=None):
        if id is not None:
            return Choice.objects.get(pk=id)

    # get list
    def resolve_all_questions(self, context):
        return Question.objects.all()

    def resolve_all_choices(self, context):
        return Choice.objects.all()

