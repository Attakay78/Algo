from tree_algo import BiTreeNode

electronics = BiTreeNode("Electronics")
phone = BiTreeNode("Phone")
laptop = BiTreeNode("Laptop")

electronics.add_child(phone)
electronics.add_child(laptop)

iphone = BiTreeNode("Iphone")
samsung = BiTreeNode("Samsung")
nokia = BiTreeNode("Nokia")

phone.add_child(iphone)
phone.add_child(samsung)
phone.add_child(nokia)

toshiba = BiTreeNode("Toshiba")
dell = BiTreeNode("Dell")

laptop.add_child(toshiba)
laptop.add_child(dell)

electronics.print_tree(level=3)
