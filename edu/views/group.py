from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from edu.permission import IsManager, IsTeacher
from edu.serializers import GroupSerializer
from edu.services import GroupService

class GroupListView(APIView):
    """API View to list all groups."""
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser |
                          IsManager | IsTeacher]


    def get(self, request):
        groups = GroupService.get_all_groups()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupDetailView(APIView):
    """API View to retrieve a group by ID."""
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser |
                          IsManager | IsTeacher]


    def get(self, request, id):
        group = GroupService.get_group_by_id(id)
        if group:
            serializer = GroupSerializer(group)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND)
