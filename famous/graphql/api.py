import graphene
from polls import schema as pollsSchema

class Query(pollsSchema.Query, graphene.ObjectType):
    pass

# class Mutations(graphene.ObjectType):


schema = graphene.Schema(query=Query)