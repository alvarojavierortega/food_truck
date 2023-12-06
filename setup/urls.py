from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi

class Gen(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        for definition in schema.definitions.keys():
            if hasattr(schema.definitions[definition]._NP_serializer, "get_examples"):
                examples = schema.definitions[definition]._NP_serializer.get_examples()
                for example in examples.keys():
                    if example in schema.definitions[definition]["properties"]:
                        schema.definitions[definition]["properties"][example][
                            "example"
                        ] = examples[example]
        return schema

schema_view = get_schema_view(
   openapi.Info(
      title="Food trucks' Application",
      default_version='v1.0',
      description="This application finds Food trucks' locations",
      terms_of_service="",
      contact=openapi.Contact(email="alvarojavierortega.com@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   generator_class=Gen
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('food_trucks.urls')), 
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT} ),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
] 

