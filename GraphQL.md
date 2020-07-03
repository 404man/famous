# GraphQl
  GraphQl 有 三个 Relay, Apollo and gql
##  graphene-django 

### Installation 
* 在 requirements.txt 添加一下 包
```
graphene==3.0b2  // 是python 库用于快速简单的构建 schemas/types
graphene-django==3.0b3
graphene-federation==0.1.0  // 实现 graphene  https://github.com/preply/graphene-federation
graphql-core>=3 // 是GraphQl.js 的端口
graphql-relay==3.0.0 // Relay library for GraphQL-core.
```
GraphQL-Relay-Py is a Python port of graphql-relay-js, while GraphQL-Core is a Python port of GraphQL.js, the reference implementation of GraphQL for JavaScript.

*  Settings
  ```
  INSTALLED_APPS = (
    # ...
    'django.contrib.staticfiles', # Required for GraphiQL
      'graphene_django',
  )

  GRAPHENE = {
      'SCHEMA': 'famous.schema.schema' # Where your Graphene schema lives
  }
  ```
* Urls
We need to set up a GraphQL endpoint in our Django app, so we can serve the queries.
```
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    path('graphql', GraphQLView.as_view(graphiql=True)),
]
```
### Examples 
Here is a simple Django model:
https://github.com/graphql-python/graphene-django/

```
from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
```

To create a *GraphQL* schema for it you simply have to write the following:

```
from graphene_django import DjangoObjectType
import graphene

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()

schema = graphene.Schema(query=Query)
```
Then you can query the __schema__:

```
query = '''
    query {
      users {
        name,
        lastName
      }
    }
'''
result = schema.execute(query)
```

##  文件目录 结构

* 各种 models 建在  famous 内， 然后再加一个graphql 目录
* graphql 里建 views.py(提供处理方法, urls.py 用到) 和 api.py (总的schema入口文件
, urls.py 会用到)