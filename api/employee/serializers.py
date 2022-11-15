from rest_framework import serializers
from employee.models import EmployeeDetails,WorkingExperiences,Qualifications,Projects


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeDetails
        fields = ['name', 'email','phone','age','gender','hno','street','city','state','image']


class WorkingExperiencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkingExperiences
        exclude = ['id','employee']


class QualificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualifications
        exclude = ['id','employee']


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ['id','employee']


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    workingExperience = serializers.SerializerMethodField()
    addressDetails = serializers.SerializerMethodField()
    qualifications = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeDetails
        fields = ('name', 'email','phone','age','gender','addressDetails','workingExperience','qualifications','projects','image')

    def get_gender(self,instance) :
        return instance.get_gender_display()

    def get_addressDetails(self,instance) :
        return {
                "hno": instance.hno,
                "street": instance.street,
                "state": instance.state,
                "city": instance.city,
            }

    def get_workingExperience(self,instance) :
            request = self.context.get('request')
            if WorkingExperiences.objects.filter(employee__pk=instance.pk).exists():
                instances = WorkingExperiences.objects.filter(employee__pk=instance.pk)
                return WorkingExperiencesSerializer(instances, many=True, context={"request": request}).data


    def get_qualifications(self,instance) :
        request = self.context.get('request')
        if Qualifications.objects.filter(employee__pk=instance.pk).exists():
            instances = Qualifications.objects.filter(employee__pk=instance.pk)
            return QualificationsSerializer(instances, many=True, context={"request": request}).data


    def get_projects(self,instance) :
        request = self.context.get('request')
        if Projects.objects.filter(employee__pk=instance.pk).exists():
            instances = Projects.objects.filter(employee__pk=instance.pk)
            return ProjectsSerializer(instances, many=True, context={"request": request}).data