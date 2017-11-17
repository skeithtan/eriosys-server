from graphene_django.types import DjangoObjectType
from .models import *

from graphene import (
    ObjectType,
    List,
    Field,
    Int,
    Boolean, String)


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class ResidencyAddressHistoryType(DjangoObjectType):
    class Meta:
        model = ResidencyAddressHistory


class StudentProgramType(DjangoObjectType):
    class Meta:
        model = StudentProgram


class Query(ObjectType):
    students = List(StudentType, archived=Boolean(), year_archived=Int(), category=String())
    resident_address_histories = List(ResidencyAddressHistoryType)
    student_programs = List(StudentProgramType)

    student = Field(StudentType, id=Int())
    resident_address_history = Field(ResidencyAddressHistoryType, id=Int())
    student_program = Field(StudentProgramType, id=Int())

    def resolve_students(self, info, **kwargs):
        archived = kwargs.get('archived', False)
        year_archived = kwargs.get('year_archived')
        category = kwargs.get('category', 'all')

        students = Student.archived.filter(archived_at__year=year_archived) if archived else Student.current.all()

        if category == 'all':
            return students

        return students.filter(category=category)

    def resolve_resident_address_histories(self, info, **kwargs):
        return ResidencyAddressHistory.objects.all()

    def resolve_student_programs(self, info, **kwargs):
        return StudentProgram.objects.all()

    def resolve_student(self, info, **kwargs):
        return Student.objects.get(pk=kwargs.get('id'))

    def resolve_resident_address_history(self, info, **kwargs):
        return ResidencyAddressHistory.objects.get(pk=kwargs.get('id'))

    def resolve_student_program(self, info, **kwargs):
        return StudentProgram.objects.get(pk=kwargs.get('id'))
