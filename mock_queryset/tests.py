from mock_queryset import MockQuerySet

class TestQuerySet(object):

    def test_it_iterates(self):
        qs = MockQuerySet()
        qs.iter_list = [1,2]
        qslist = list(qs)
        assert qslist == [1,2]

    def test_it_indexes(self):
        qs = MockQuerySet()
        qs.iter_list = [1,2]
        assert qs[0] == 1

    def test_chainable(self):
        qs = MockQuerySet()
        assert qs is qs.filter()
