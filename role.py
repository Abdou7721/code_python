from enum import Enum


class Role(Enum):
   Admin ="Admin"
   Personnel= "Personnel"
   Client= "Client"
   def role_str(self):
    return self.role.value
