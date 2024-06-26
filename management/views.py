from django.db.models.functions import ExtractMonth
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import StaffUser, TimeTable
from authentication.permissions import IsInSameSchool, IsStaffUser
from constants import UserLoginMessage, UserResponseMessage, TimeTableMessage, ReportCardMesssage, month_mapping
from management.serializers import ManagementProfileSerializer, TimeTableSerializer, TimeTableDetailViewSerializer, \
    ExamReportCardSerializer, StudentReportCardSerializer
from pagination import CustomPagination
from student.models import ExmaReportCard
from superadmin.models import SchoolProfile
from utils import create_response_data


# Create your views here.

class ManagementProfileView(APIView):
    """
    This class is used to fetch detail of management
    """
    permission_classes = [IsStaffUser, IsInSameSchool]

    def get(self, request):
        try:
            user = request.user
            if user.user_type == 'non-teaching':
                teacher_user = StaffUser.objects.get(user=user, user__school_id=request.user.school_id, role="Payroll Management")
                user_detail = ManagementProfileSerializer(teacher_user)
        except StaffUser.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=e.args[0],
                data={}
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        response_data = create_response_data(
            status=status.HTTP_201_CREATED,
            message=UserResponseMessage.USER_DETAIL_MESSAGE,
            data=user_detail.data
        )
        return Response(response_data, status=status.HTTP_201_CREATED)


class ExamTimeTableView(APIView):
    """
    This class is used to fetch exam timetable.
    """
    permission_classes = [IsStaffUser, IsInSameSchool]
    pagination_class = CustomPagination

    def get(self, request):
        try:
            user = request.user
            current_date = timezone.now().date()
            teacher_user = StaffUser.objects.get(user=user, user__school_id=request.user.school_id,
                                                 role="Payroll Management")
            exam_timetable = TimeTable.objects.filter(status=1, school_id=user.school_id).order_by('-id')
            if request.query_params.get('exam') == 'current_exam':
                exam_timetable = exam_timetable.filter(exam_month__gte=current_date.replace(day=1)).order_by('-id')

            if request.query_params.get('exam') == 'post_exam':
                exam_timetable = exam_timetable.filter(exam_month__lt=current_date.replace(day=1)).order_by('-id')

            # Paginate the queryset
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(exam_timetable, request)

            serializers = TimeTableSerializer(paginated_queryset, many=True)
            response = {
                'status': status.HTTP_200_OK,
                'count': len(serializers.data),
                'message': TimeTableMessage.TIMETABLE_FETCHED_SUCCESSFULLY,
                'data': serializers.data,
                'pagination': {
                    'page_size': paginator.page_size,
                    'next': paginator.get_next_link(),
                    'previous': paginator.get_previous_link(),
                    'total_pages': paginator.page.paginator.num_pages,
                    'current_page': paginator.page.number,
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        except StaffUser.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=e.args[0],
                data={}
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class ExamTimeTableDetailView(APIView):
    """
    This class is used to fetch detail of the timetable according to the class.
    """
    permission_classes = [IsStaffUser, IsInSameSchool]

    def get(self, request, pk):
        try:
            user = request.user
            teacher_user = StaffUser.objects.get(user=user, user__school_id=request.user.school_id,
                                                 role="Payroll Management")
            exam_timetable = TimeTable.objects.get(id=pk, status=1, school_id=user.school_id)
            serializer = TimeTableDetailViewSerializer(exam_timetable)
            response = create_response_data(
                status=status.HTTP_200_OK,
                message=TimeTableMessage.TIMETABLE_FETCHED_SUCCESSFULLY,
                data=serializer.data
            )
            return Response(response, status=status.HTTP_200_OK)
        except TimeTable.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=TimeTableMessage.TIMETABLE_NOT_EXIST,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except StaffUser.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=e.args[0],
                data={}
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class ExamTimeTableDeleteView(APIView):
    """
    This class is used to delete declared timetable which is added by teacher.
    """
    permission_classes = [IsStaffUser, IsInSameSchool]

    def delete(self,request,pk):
        try:
            user = request.user
            teacher_user = StaffUser.objects.get(user=user, user__school_id=request.user.school_id,
                                                 role="Payroll Management")
            exam_timetable = TimeTable.objects.get(id=pk, status=1, school_id=user.school_id)
            exam_timetable.delete()
            response = create_response_data(
                status=status.HTTP_200_OK,
                message=TimeTableMessage.TIMETABLE_DELETED_SUCCESSFULLY,
                data={}
            )
            return Response(response, status=status.HTTP_200_OK)

        except TimeTable.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=TimeTableMessage.TIMETABLE_NOT_EXIST,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except StaffUser.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=e.args[0],
                data={}
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class ExamReportCardListView(APIView):
    """
    This class is used to fetch report card.
    """
    permission_classes = [IsStaffUser, IsInSameSchool]
    pagination_class = CustomPagination

    def get(self, request):
        try:
            user = request.user
            teacher_user = StaffUser.objects.get(user=user, user__school_id=request.user.school_id,
                                                 role="Payroll Management")
            curriculum = request.query_params.get('curriculum', None)
            class_name = request.query_params.get('class', None)
            section = request.query_params.get('section', None)
            exam_type = request.query_params.get('exam_type', None)
            exam_month = request.query_params.get('exam_month', None)
            exam_year = request.query_params.get('exam_year', None)

            report_card = ExmaReportCard.objects.filter(status=1, school_id=request.user.school_id).order_by('-id')

            if curriculum:
                report_card = report_card.filter(curriculum=curriculum)
            if class_name:
                report_card = report_card.filter(class_name=class_name)
            if section:
                report_card = report_card.filter(class_section=section)
            if exam_type:
                report_card = report_card.filter(exam_type=exam_type)
            if exam_month:
                month_number = month_mapping.get(exam_month)
                report_card = report_card.annotate(month=ExtractMonth('exam_month')).filter(month=month_number)
            if exam_year:
                report_card = report_card.filter(updated_at__year=exam_year)
            if exam_month and exam_year:
                month_number = month_mapping.get(exam_month)
                report_card = report_card.annotate(month=ExtractMonth('exam_month')).filter(month=month_number, updated_at__year=exam_year)
            if curriculum and class_name:
                report_card = report_card.filter(curriculum=curriculum, class_name=class_name)
            if curriculum and class_name and section:
                report_card = report_card.filter(curriculum=curriculum, class_name=class_name, class_section=section)
            if curriculum and class_name and section:
                report_card = report_card.filter(curriculum=curriculum, class_name=class_name, class_section=section)
            if curriculum and class_name and section and exam_type:
                report_card = report_card.filter(curriculum=curriculum, class_name=class_name, class_section=section, exam_type=exam_type)
            if curriculum and class_name and section and exam_type and exam_month:
                month_number = month_mapping.get(exam_month)
                report_card = report_card.annotate(month=ExtractMonth('exam_month')).filter(curriculum=curriculum, class_name=class_name, class_section=section, exam_type=exam_type, month=month_number)
            # Paginate the queryset
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(report_card, request)

            serializer = ExamReportCardSerializer(paginated_queryset, many=True)
            response = {
                'status': status.HTTP_200_OK,
                'count': len(serializer.data),
                'message': ReportCardMesssage.REPORT_CARD_FETCHED_SUCCESSFULLY,
                'data': serializer.data,
                'pagination': {
                    'page_size': paginator.page_size,
                    'next': paginator.get_next_link(),
                    'previous': paginator.get_previous_link(),
                    'total_pages': paginator.page.paginator.num_pages,
                    'current_page': paginator.page.number,
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        except StaffUser.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=e.args[0],
                data={},
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class ExamReportCardFilterListView(APIView):
    """
    This class is used to fetch report card according to provided curriculum, class, and section.
    """
    permission_classes = [IsStaffUser, IsInSameSchool]
    pagination_class = CustomPagination

    def get(self, request):
        try:
            user = request.user
            teacher_user = StaffUser.objects.get(user=user, user__school_id=request.user.school_id,
                                                 role="Payroll Management")

            curriculum = request.query_params.get('curriculum')
            class_name = request.query_params.get('class')
            section = request.query_params.get('section')
            exam_type = request.query_params.get('exam_type')
            exam_month = request.query_params.get('exam_month')
            exam_year = request.query_params.get('exam_year')

            if curriculum and class_name and section and exam_type and exam_year:
                report_card = ExmaReportCard.objects.filter(status=1, school_id=request.user.school_id, curriculum=curriculum, class_name=class_name, class_section=section,
                                                            updated_at__year=exam_year, exam_type=exam_type).order_by('-id')
                if exam_month:
                    month_number = month_mapping.get(exam_month)
                    report_card = report_card.annotate(month=ExtractMonth('exam_month')).filter(month=month_number)
                # Paginate the queryset
                paginator = self.pagination_class()
                paginated_queryset = paginator.paginate_queryset(report_card, request)

                serializer = ExamReportCardSerializer(paginated_queryset, many=True)
                response = {
                    'status': status.HTTP_200_OK,
                    'count': len(serializer.data),
                    'message': ReportCardMesssage.REPORT_CARD_FETCHED_SUCCESSFULLY,
                    'data': serializer.data,
                    'pagination': {
                        'page_size': paginator.page_size,
                        'next': paginator.get_next_link(),
                        'previous': paginator.get_previous_link(),
                        'total_pages': paginator.page.paginator.num_pages,
                        'current_page': paginator.page.number,
                    }
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = create_response_data(
                    status=status.HTTP_400_BAD_REQUEST,
                    message="Please provide curriculum, class, section, exam_month, exam_type, and exam_year.",
                    data={}
                )
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except StaffUser.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=e.args[0],
                data={},
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class StudentReportCardView(APIView):
    """
    This class is used to fetch report card according ot provided student roll_no.
    """
    permission_classes = [IsStaffUser, IsInSameSchool]

    def get(self, request):
        try:
            user = request.user
            current_date = timezone.now().date()
            teacher_user = StaffUser.objects.get(user=user, user__school_id=request.user.school_id,
                                                 role="Payroll Management")
            student_name = request.query_params.get('student_name')
            curriculum = request.query_params.get('curriculum', None)
            class_name = request.query_params.get('class', None)
            section = request.query_params.get('section', None)
            exam_type = request.query_params.get('exam_type', None)
            exam_month = request.query_params.get('exam_month', None)
            exam_year = request.query_params.get('exam_year', None)
            report_card = ExmaReportCard.objects.filter(status=1, school_id=request.user.school_id)
            if student_name:
                report_card = report_card.filter(student_name=student_name, updated_at__year=current_date.year)

            if student_name and curriculum and class_name and section and exam_type and exam_year:
                month_number = month_mapping.get(exam_month)
                report_card = report_card.annotate(month=ExtractMonth('exam_month')).filter(student_name=student_name, curriculum=curriculum, class_name=class_name, class_section=section,
                                                            updated_at__year=exam_year, exam_type=exam_type, month=month_number)

            serializer = StudentReportCardSerializer(report_card, many=True)
            response = create_response_data(
                status=status.HTTP_200_OK,
                message=ReportCardMesssage.REPORT_CARD_FETCHED_SUCCESSFULLY,
                data=serializer.data
            )
            return Response(response, status=status.HTTP_200_OK)

        except StaffUser.DoesNotExist:
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=e.args[0],
                data={},
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)