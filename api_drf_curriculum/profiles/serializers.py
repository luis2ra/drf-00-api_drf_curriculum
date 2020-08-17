from rest_framework import serializers
from profiles.models import Plan
from profiles.enums import PlanTypeEnum


class PlanSerializer(serializers.ModelSerializer):
    type_plan = serializers.SerializerMethodField()
    image_style = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['id', 'name', 'type_plan', 'image',
                  'image_style', 'amount', 'max_suscriptors',
                  'is_selected']

    def get_image_style(self, obj):
        data = {
            "width": 20, 
            "height": 25, 
            "resizeMode": "stretch" }
        return data

    def get_type_plan(self, obj):
        return PlanTypeEnum[obj.type_plan].value