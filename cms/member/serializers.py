from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Member
from django_countries.serializer_fields import CountryField as CountrySerializerField
from datetime import date


# class UserSerializer(serializers.ModelSerializer):
#     password_confirm = serializers.CharField(write_only=True, style={'input_type': 'password'})
#     password = serializers.CharField(write_only=True, style={'input_type': 'password'})

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_confirm')
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def validate(self, attrs):
#         password = attrs.get('password')
#         password_confirm = attrs.get('password_confirm')

#         # Check if passwords match
#         if password != password_confirm:
#             raise serializers.ValidationError("Password and password confirmation do not match.")
        
#         # Check if password meets the password validation criteria
#         validate_password(password)

#         return attrs

#     def create(self, validated_data):
#         # Remove password_confirm from validated data
#         validated_data.pop('password_confirm')

#         # Create the User instance
#         user = User.objects.create_user(**validated_data)
#         return user
    # def update(self, instance, validated_data):
    #     # Handle updating the user, including password if it is provided
    #     password = validated_data.get('password', None)
    #     if password:
    #         instance.set_password(password)
        
    #     # Update the user fields
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
        
    #     return instance

class MemberSerializer(serializers.ModelSerializer):
    nationality = CountrySerializerField()
    class Meta:
        model = Member
        fields = ('id', 'user', 'first_name', 'middle_name', 'last_name' , 'email', 'gender', 'dob', 'address', 
                  'phone1', 'phone2', 'nationality', 'photo_url', 'status')
        read_only_fields = ('user',)
        
    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)
        
        # Override the nationality field to display the full country name
        representation['nationality'] = instance.nationality.name if instance.nationality else None
        
        return representation
    
    def validate_dob(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value