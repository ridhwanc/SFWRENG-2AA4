import pytest
from SeqADT import *
from DCapALst import *
from SALst import *


class TestSeqADT:
    def test_init(self):
        test = SeqADT(['hello', 'goodbye'])
        assert test.s == ['hello', 'goodbye']

    def test_start(self):
        test = SeqADT(['hello', 'goodbye'])
        test.start()
        assert not (test.i == 2)

    def test_start2(self):
        test = SeqADT(['hello', 'goodbye'])
        test.start()
        assert (test.i == 0)

    def test_next(self):
        test = SeqADT([])
        test.start()
        i = test.i
        test.next()
        assert (i < test.i)

    def test_end(self):
        test = SeqADT(['test'])
        test.start()
        test.next()
        assert (test.end() is True)


class TestDCapALst:
    def test_init2(self):
        DCapALst.init()
        assert DCapALst.s == []

    def test_add(self):
        DCapALst.init()
        DCapALst.add(DeptT.chemical, 100)
        assert DCapALst.s == [(DeptT.chemical, 100)]

    def test_remove(self):
        DCapALst.init()
        DCapALst.add(DeptT.chemical, 100)
        assert DCapALst.remove(DeptT.software) is False

    def test_elm(self):
        DCapALst.init()
        DCapALst.add(DeptT.software, 70)
        assert DCapALst.elm(DeptT.chemical) is True

    def test_capacity(self):
        DCapALst.init()
        DCapALst.add(DeptT.materials, 20)
        assert DCapALst.capacity(DeptT.engphys) == 15


class TestSALst:
    def test_init(self):
        SALst.init()
        assert SALst.s == []

    def test_add(self):
        SALst.init()
        sinfo_1 = SInfoT('first', 'last', GenT.male, 10.0,
                         SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add('ayyeee', sinfo_1)
        assert SALst.s == [('ayeee', sinfo_1)]

    def test_remove(self):
        SALst.init()
        sinfo_1 = SinfoT('first', 'last', GenT.male, 11.0,
                         SeqADT([DeptT.engphys, DeptT.materials]), True)
        SALst.add('hey', sinfo_1)
        SALst.remove('hey')
        assert SALst.s == []

    def test_elm(self):
        SALst.init()
        sinfo_1 = SInfoT('first', 'last', GenT.male, 11.5,
                         SeqADT([DeptT.chemical, DeptT.civil]), True)
        SALst.add('test', sinfo_1)
        assert SALst.info('test2') == sinfo_1

    def test_info(self):
        SALst.init()
        sinfo_1 = SInfoT('first', 'last', GenT.male, 11.5,
                         SeqADT([DeptT.chemical, DeptT.civil]), True)
        SALst.add('test1', sinfo_1)
        assert SALst.info('test1') == sinfo_1

    def test_sort(self):
        SALst.init()
        sinfo_1 = SInfoT('first', 'last', GenT.male, 11.5,
                         SeqADT([DeptT.software, DeptT.civil]), True)
        SALst.add('hey', sinfo_1)
        sinfo_2 = SInfoT('first', 'last', GenT.male, 11.5,
                         SeqADT([DeptT.software, DeptT.civil]), True)
        SALst.add('hi', sinfo_2)
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ['hey', 'hi']

    def test_average(self):
        SALst.init()
        sinfo_1 = SInfoT('first', 'last', GenT.male, 8.0,
                         SeqADT([DeptT.chemical, DeptT.civil]), True)
        SALst.add('ridhwan', sinfo_1)
        sinfo_2 = SInfoT('first', 'last', GenT.male, 8.5,
                         SeqADT([DeptT.chemical, DeptT.civil]), True)
        SALst.add('youngboy', sinfo_2)
        assert SALst.average(lambda x: x.gender == GenT.male) == 8.25

    def test_allocate(self):
        SALst.init()
        sinfo_1 = SInfoT('first', 'last', GenT.male, 8.0,
                         SeqADT([DeptT.chemical, DeptT.civil]), True)
        SALst.add('riddy', sinfo_1)
        assert AALst.lst_alloc(DeptT.chemical) == ['riddy']
