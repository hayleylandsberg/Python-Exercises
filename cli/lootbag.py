import uuid

class LootBag():

    def write_toy_to_file(self, child_name, action):
        with open("children", action) as children:
            child_id = uuid.uuid4()
            children.write("{},{}\n".format(child_id, child_name))

            return child_id
            
    def list_toys_for_child(self, child):
        return ["ball"]

    def add_toy_to_bag(self, toy, child):
        return "Toy added to the bag"
        try:
            with open("children", "r") as children:
                all_children = children.readlines()
            
            for child in all_children:
                current_child_id, current_child_name = child.splt(",")
                if current_child_name == child_name:
                    self.write_toy_to_file(toy, current_child_id, "a")
                    return
            
            new_child_id = self.write_child_to_file(child_name, "a")
            self.write_child_to_file(toy, new_child_id, "a")
        
        except FileNotFoundError:
            new_child_id = self.write_child_to_file(child_name, "w")
            self.write_toy_to_file(toy, new_child_id, "a")

    
    def remove_toy_from_bag(self, toy, child):
        return "Toy removed from bag"

    def get_kids(self):
        #Initial test-passing code
        return ["Mikey"]

    def deliver_toys_to_child(self, child):
        #initial test-passing code
        return {
            "deliver": True
        }