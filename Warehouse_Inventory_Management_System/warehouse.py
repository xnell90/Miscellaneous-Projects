class Item:
    """ Example class for an item in the warehouse management system. You may
        modify or extend this in any way you need.
    """
    def __init__(self, size):
        self.size = size

    def count(self):
        return 1

class Container:
    instances = []

    def __init__(self, larger_containers):
        self.containers = []
        self.larger_containers = larger_containers
        Container.instances.append(self)

    def __len__(self):
        return len(self.containers)

    def count(self):
        count_containers = 1

        for container in self.containers:
            container_name = type(container).__name__

            if container_name == "Item": count_containers += 1
            elif len(container.containers) == 0: count_containers += 1
            else: count_containers += container.count()

        return count_containers

    def add(self, thing):
        if type(thing).__name__ in self.larger_containers: return False

        for container in Container.instances:
            if container.contains(thing): container.remove(thing)

        has_space = thing.size <= self.available_capacity
        if has_space:
            self.containers.append(thing)
            self.current_capacity   += thing.size
            self.available_capacity -= thing.size

        return has_space

    def contains(self, thing):
        for container in self.containers:
            if container == thing: return True
            elif type(container).__name__ == "Item": continue
            elif container.contains(thing): return True
            else: continue

        return False

    def remove(self, thing = None):
        object_removed = None

        if thing is None:
            object_removed = self.containers[-1]
            del self.containers[-1]
            return object_removed

        for index, container in enumerate(self.containers):
            if container == thing:
                object_removed = container
                del self.containers[index]
                return object_removed

            if type(container).__name__ == "Item": continue

            object_removed = container.remove(thing)
            if object_removed is not None: return object_removed

        return object_removed

    def extract(self, thing):
        return self.remove(thing)

    def pack(self, thing):
        for container in self.containers:
            if container.add(thing): return True


class Warehouse(Container):
    def __init__(self):
        Container.__init__(self, [])

    def __len__(self):
        return Container.__len__(self)

    def count(self):
        return Container.count(self)

    def add(self, thing):
        if type(thing).__name__ != "Warehouse": self.containers.append(thing)
        return type(thing).__name__ != "Warehouse"

    def contains(self, thing):
        return Container.contains(self, thing)

    def remove(self, thing = None):
        return Container.remove(self, thing)

    def pack(self, thing):
        return Container.pack(self, thing)

class Shelf(Container):
    def __init__(self):
        Container.__init__(self, ["Warehouse", "Shelf"])
        self.size               = 100
        self.current_capacity   = 0
        self.available_capacity = 100

    def __len__(self):
        return Container.__len__(self)

    def count(self):
        return Container.count(self)

    def add(self, thing):
        if type(thing).__name__ == "Item" and thing.size <= 7: return False
        return Container.add(self, thing)

    def contains(self, thing):
        return Container.contains(self, thing)

    def remove(self, thing = None):
        return Container.remove(self, thing)

    def pack(self, thing):
        return Container.pack(self, thing)

class Bin(Container):
    def __init__(self):
        Container.__init__(self, ["Warehouse", "Shelf", "Bin"])
        self.size               = 10
        self.current_capacity   = 0
        self.available_capacity = 10

        def __len__(self):
            return Container.__len__(self)

        def count(self):
            return Container.count(self)

        def add(self, thing):
            return Container.add(self, thing)

        def contains(self, thing):
            return Container.contains(self, thing)

        def remove(self, thing = None):
            return Container.remove(self, thing)

        def pack(self, thing):
            return Container.pack(self, thing)

class Box(Container):
    def __init__(self):
        Container.__init__(self, ["Warehouse", "Shelf", "Bin", "Box"])
        self.size               = 5
        self.current_capacity   = 0
        self.available_capacity = 5

        def __len__(self):
            return Container.__len__(self)

        def count(self):
            return Container.count(self)

        def add(self, thing):
            return Container.add(self, thing)

        def contains(self, thing):
            return Container.contains(self, thing)

        def remove(self, thing = None):
            return Container.remove(self, thing)

        def pack(self, thing):
            return Container.pack(self, thing)

class Bag(Container):
    def __init__(self):
        Container.__init__(self, ["Warehouse", "Shelf", "Bin", "Box", "Bag"])
        self.size               = 2
        self.current_capacity   = 0
        self.available_capacity = 2

        def __len__(self):
            return Container.__len__(self)

        def count(self):
            return Container.count(self)

        def add(self, thing):
            return Container.add(self, thing)

        def contains(self, thing):
            return Container.contains(self, thing)

        def remove(self, thing = None):
            return Container.remove(self, thing)

        def pack(self, thing):
            return Container.pack(self, thing)

#Added a few tests to check if count and __len__ works.
if __name__ == "__main__":
    bag = Bag()
    bag.add(Item(1))
    bag.add(Item(1))

    len_test = (len(bag) == 2)
    count_test = (bag.count() == 3)

    if len_test and count_test:
        print("Pass: __len__ and count() works for bag")

    box = Box()
    box.add(bag)
    box.add(Item(1))

    len_test = (len(box) == 2)
    count_test = (box.count() == 5)

    if len_test and count_test:
        print("Pass: __len__ and count() works for box")

    bin = Bin()
    bin.add(box)

    len_test = (len(bin) == 1)
    count_test = (bin.count() == 6)

    if len_test and count_test:
        print("Pass: __len__ and count() works for bin")

    shelf = Shelf()
    shelf.add(bin)

    len_test = (len(shelf) == 1)
    count_test = (shelf.count() == 7)

    if len_test and count_test:
        print("Pass: __len__ and count() works for shelf")

    warehouse = Warehouse()
    warehouse.add(shelf)

    len_test = (len(warehouse) == 1)
    count_test = (warehouse.count() == 8)

    if len_test and count_test:
        print("Pass: __len__ and count() works for warehouse")
