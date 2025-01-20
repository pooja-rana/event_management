from enum import Enum


class UserConst(Enum):
    USERNAME_REGEX = r"^(?=.{8,15}$)(?=.*[a-zA-Z])[A-Za-z10-9]+$"
    PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&^()_+|}" \
                     r"{\]\[:><.,\/\\;'=~`\"-])[A-Za-z\d@$!#%*?&^()_+|}{\]\[:><.,\/\\;'=~`\"-]{8,64}$"
    DATE_AND_TIME_FORMAT = "%d-%m-%Y %H:%M"
