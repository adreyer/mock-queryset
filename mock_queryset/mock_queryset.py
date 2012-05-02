from mock import Mock

class MockQuerySet(Mock):

    def __init__(self):
        super(MockQuerySet, self).__init__()
        self.chainable_attrs = {'filter':Mock()}
        for x in self.chainable_attrs:
            self.chainable_attrs[x].return_value = self

    def __getattr__(self, attr):
        if attr in self.chainable_attrs:
            return self
        return super(MockQuerySet, self).__getattr__(attr)


    def __iter__(self):
        for x in self.iter_list:
            yield x

    def __getitem__(self, index):
        return self.iter_list[index]

