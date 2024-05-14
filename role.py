from enum import Enum


class Role(Enum):
   Admin ="Admin"
   Personnel= "Personnel"
   Client= "Client"
   def role_str(self):
    return self.role.value

# Création des rôles avec leurs autorisations
# admin_role = Role("Admin", ["add_product", "update_product", "delete_product", "add_personnel", "update_personnel", "delete_personnel"])
# personnel_role = Role("Personnel", ["change_order_status"])
# client_role = Role("Client", ["place_order", "add_to_cart", "update_cart_item_quantity", "clear_cart"])
