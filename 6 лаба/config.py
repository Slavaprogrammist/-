from enum import Enum

token = "5026050386:AAFYSd_Sw75IcKZDm_k4IFsnjlGMuxsSqyo"
db_file = "database.vdb"

CURRENT_STATE = "CURRENT_STATE"

class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать строки (str)
    """
    S_START = "0"  # Начало нового диалога
    STATE_FIRST_NUM = "1"
    STATE_SECOND_NUM = "2"
    STATE_THIRD_NUM = "3"