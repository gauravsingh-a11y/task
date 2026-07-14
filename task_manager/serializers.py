from rest_framework import serializers
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "firstname","lastname", "password","is_active"]

    # 📧 Email unique validation
    def validate_email(self, value):
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    #  Create user
    def create(self, validated_data):
        password = validated_data.pop("password", None)

        user = User.objects.create_user(
            email=validated_data.get("email"),
            password=password,
            firstname=validated_data.get("firstname", ""),
            lastname=validated_data.get("lastname", ""),
            # phone_number=validated_data.get("phone_number")
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    
    password = serializers.CharField(required=False)

    def validate(self, data):
        email = data.get("email")        
        password = data.get("password")
        if not email: 
            raise serializers.ValidationError("Email is required")
        try:
            if email:
                user = User.objects.get(email=email.lower())
            
        except User.DoesNotExist:
            raise serializers.ValidationError("User not Exist")
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password")
        # if not user.is_active:
        #     raise serializers.ValidationError("Account is disabled")
        # if not user.is_verified:
        #     raise serializers.ValidationError("Account is not verified")
        
            
        data["user"] = user
        return data