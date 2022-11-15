from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employee.models import EmployeeDetails,WorkingExperiences,Qualifications,Projects
from api.employee.serializers import EmployeeSerializer,EmployeeDetailsSerializer,WorkingExperiencesSerializer,QualificationsSerializer,ProjectsSerializer

# auto id generation function for creating a reg number
def get_auto_id(model):
    auto_id = 1
    try:
        latest_auto_id =  model.objects.all()[:1]
        if latest_auto_id:
            for auto in latest_auto_id:
                auto_id = auto.id + 1
    except:
        pass
    return auto_id

# employeee get and ceate view
@api_view(['GET', 'POST'])
def employee(request):
    """
    List all code employees, or create a new employee.
    """
    if request.method == 'GET':
        if EmployeeDetails.objects.filter().exists():
            instances = EmployeeDetails.objects.all()
            serializer = EmployeeDetailsSerializer(instances, many=True)

            response_data = {
                "StatusCode": 200,
                "message" : "employee details found",
                "success" : True,
                "employees" : serializer.data
                }
            return Response(response_data, status=status.HTTP_200_OK)
        else :
            response_data = {
                "StatusCode": 200,
                "message" : "employee details not found",
                "success" : False,
                "employees" : []
                }
            return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        employee_serializer = EmployeeSerializer(data=request.data)
        experience_serializer = WorkingExperiencesSerializer(data=request.data)
        qualification_serializer = QualificationsSerializer(data=request.data)
        project_serializer = ProjectsSerializer(data=request.data)
        email = request.data["email"]

        print(email,type(email))

        if not EmployeeDetails.objects.filter(email=email).exists():
            if employee_serializer.is_valid():
                if experience_serializer.is_valid():
                    if qualification_serializer.is_valid():
                        if project_serializer.is_valid():

                            auto_id = get_auto_id(EmployeeDetails)

                            employee = employee_serializer.save(
                                regid = "EMP" + str(auto_id).zfill(3)
                            )

                            experience_serializer.save(
                                employee = employee
                            )

                            qualification_serializer.save(
                                employee = employee
                            )

                            project_serializer.save(
                                employee = employee
                            )

                            response_data = {
                                "StatusCode": 200,
                                "message" : "employee created successfully",
                                "regid" : employee.regid,
                                "success" : True,
                            }

                            return Response(response_data, status=status.HTTP_200_OK)
                        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    return Response(qualification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response(experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(employee_serializer, status=status.HTTP_400_BAD_REQUEST)

        response_data = {
            "StatusCode": 200,
            "message" : "employee already exist",
            "success" : False,
            }

        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def edit_employee(request):
    """
    Retrieve, update or delete a code employee.
    params : regid
    """
    if request.GET.get("regid") :
        regid = request.GET.get("regid")

        try:
            employee = EmployeeDetails.objects.get(regid=regid)
        except EmployeeDetails.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = EmployeeDetailsSerializer(employee)

            response_data = {
                "StatusCode": 200,
                "message" : "employee details found",
                "success" : True,
                "employee" : serializer.data
                }
            return Response(response_data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            experience = WorkingExperiences.objects.get(employee=employee)
            qualifications = Qualifications.objects.get(employee=employee)
            projects = Projects.objects.get(employee=employee)

            employee_serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            experience_serializer = WorkingExperiencesSerializer(experience, data=request.data, partial=True)
            qualification_serializer = QualificationsSerializer(qualifications, data=request.data, partial=True)
            project_serializer = ProjectsSerializer(projects, data=request.data, partial=True)

            if employee_serializer.is_valid():
                if experience_serializer.is_valid():
                    if qualification_serializer.is_valid():
                        if project_serializer.is_valid():

                            employee = employee_serializer.save()

                            experience_serializer.save()

                            qualification_serializer.save()

                            project_serializer.save()

                            response_data = {
                                "StatusCode": 200,
                                "message" : "employee Updated successfully",
                                "regid" : employee.regid,
                                "success" : True,
                            }

                            return Response(response_data, status=status.HTTP_200_OK)
                        else :
                            return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else :
                        return Response(qualification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else :
                    return Response(experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else :
                return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            if EmployeeDetails.objects.filter(regid=regid).exists():
                WorkingExperiences.objects.filter(employee=employee).delete()
                Qualifications.objects.filter(employee=employee).delete()
                Projects.objects.filter(employee=employee).delete()
                EmployeeDetails.objects.filter(regid=regid).delete()

                response_data = {
                    "StatusCode": 200,
                    "message" : "employee deleted successfully",
                    "success" : True,
                }

                return Response(response_data, status=status.HTTP_200_OK)
            else :
                response_data = {
                    "StatusCode": 200,
                    "message" : "no employee found with this regid",
                    "success" : False,
                }

                return Response(response_data, status=status.HTTP_200_OK)
    else :
        response_data = {
            "StatusCode": 400,
            "message" : "invalid body request",
            "success" : False,
        }

        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
