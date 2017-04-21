import os
import uuid
from zashel.utils import search_win_drive

__all__ = ["UUID",
           "USERS_FIELDS",
           "USERS_UNIQUE",
           "USERS_PERMISSIONS",
           "PARI_FIELDS",
           "PARI_UNIQUE",
           "PAYMENTS_FIELDS",
           "APLICATION_FIELDS",
           "METODOS_FIELDS",
           "CONFIG_FIELDS",
           "HOST", "PORT",
           "LOCAL_PATH",
           "PATH",
           "BASE_URI",
           "LOG_ERROR",
           "LOG_ERROR_PARI",
           "DATABASE_PATH",
           "REMOTE_PATH"]


#Identifier of session
UUID = uuid.uuid4()

USERS_FIELDS = ["id",
                "fullname",
                "role"]

USERS_UNIQUE = "id"

USERS_PERMISSIONS = ["type",
                     "model",
                     "verb",
                     "allowed"]

PARI_FIELDS = ["id_cliente",
               "id_cuenta",
               "numdoc",
               "fecha_factura",
               "id_factura",
               "segmento",
               "importe_adeudado",
               "estado_recibo"]

PARI_UNIQUE = "id_factura"

PAYMENTS_FIELDS = ["fecha",
                   "importe",
                   "observaciones",
                   "dni",
                   "id_cuenta",
                   "tel1",
                   "tel2",
                   "oficina"]

APLICATION_FIELDS = ["tipo", # Automático o Manual
                     "pagos__id",
                     "clientes_id_factura",
                     "importe_aplicado",
                     "nombre_cliente", # Manual
                     "numdoc",
                     "id_cuenta",
                     "periodo_facturado",
                     "metodos__id",
                     "via_de_pago"] #Crear Objeto Relacional con esto

METODOS_FIELDS = "nombre"

CONFIG_FIELDS = ["container",
                 "field"]

#Path Definitions

HOST, PORT = "localhost", 44752
LOCAL_PATH = os.path.join(os.environ["LOCALAPPDATA"], "pastel")
REMOTE_PATH = r"//pnaspom2/campanas$/a-c/cobros/financiacion"
PATH = search_win_drive("PASTEL")
DATABASE_PATH = os.path.join(PATH, "DB")
BASE_URI = "^/pastel/api/v1$"
LOG_ERROR = os.path.join(LOCAL_PATH, "log_error_{}".format(UUID))
LOG_ERROR_PARI = os.path.join(LOCAL_PATH, "log_error_pari_{}".format(UUID))