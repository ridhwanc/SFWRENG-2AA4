from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from AALst import *
from SALst import *
from Read import *

DCapALst.init()
DCapALst.add(DeptT.civil, 2)
DCapALst.add(DeptT.chemical, 2)
DCapALst.add(DeptT.electrical, 2)
DCapALst.add(DeptT.mechanical, 2)
DCapALst.add(DeptT.software, 3)
DCapALst.add(DeptT.materials, 2)
DCapALst.add(DeptT.engphys, 1)

sinfo1 = SInfoT(
    "first",
    "last",
    GenT.male,
    12.0,
    SeqADT([DeptT.civil, DeptT.chemical]),
    True
)
sinfo2 = SInfoT(
    "John",
    "Smith",
    GenT.male,
    2.8,
    SeqADT([DeptT.mechanical, DeptT.software, DeptT.engphys]),
    False
)
sinfo3 = SInfoT(
    "Jane",
    "Smith",
    GenT.female,
    7.8,
    SeqADT([DeptT.chemical, DeptT.software, DeptT.civil, DeptT.mechanical]),
    False
)
sinfo4 = SInfoT(
    "Fred",
    "Smith",
    GenT.male,
    4.9,
    SeqADT([DeptT.chemical, DeptT.software, DeptT.civil, DeptT.mechanical]),
    False
)
sinfo5 = SInfoT(
    "Eve",
    "Smith",
    GenT.female,
    11.8,
    SeqADT([DeptT.chemical, DeptT.software, DeptT.civil, DeptT.mechanical]),
    False
)

SALst.init()
SALst.add("stdnt1", sinfo1)
SALst.add("stdnt2", sinfo2)
SALst.add("stdnt3", sinfo3)
SALst.add("stdnt4", sinfo4)
SALst.add("stdnt5", sinfo5)

SALst.remove("stdnt3")

SALst.add("stdnt3", sinfo3)

print(SALst.elm("stdnt1"))

print(SALst.info("stdnt1"))

print(SALst.sort(lambda t: not(t.freechoice) and t.gpa >= 4.0))

print(SALst.average(lambda x: x.gender == GenT.male))

AALst.init()
SALst.allocate()
print(AALst.lst_alloc(DeptT.civil))
print(AALst.lst_alloc(DeptT.chemical))
print(AALst.lst_alloc(DeptT.software))

load_stdnt_data('StdntData.txt')
load_dcap_data('DeptCap.txt')
