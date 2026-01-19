from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def dashboard_data(request):
    data = {
        "usuario": {
            "nombre": "Miguel Perez",
            "cargo": "Supervisor",
            "pendientes": 3
        },
        "actividades": [
            {
                "id": 1,
                "tiempo": "Hace 10 min",
                "texto": "Juan entregó bomba X200 disponible.",
                "color": "#009688"
            },
            {
                "id": 2,
                "tiempo": "Hace 2 hrs",
                "texto": "Notificó fuga en tubería principal.",
                "color": "#e91e63"
            },
            {
                "id": 3,
                "tiempo": "Ayer 04:00 PM",
                "texto": "Alarma de temperatura alta en motor.",
                "color": "#ff9800"
            }
        ]
    }
    return Response(data)
