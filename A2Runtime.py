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
DCapALst.add(DeptT.mechanical, 1)
DCapALst.add(DeptT.software, 3)
DCapALst.add(DeptT.materials, 2)
DCapALst.add(DeptT.engphys, 1)

sinfo1 = SInfoT(
    "first",
    "last",
    GenT.male,
    12.0,
    SeqADT([DeptT.mechanical, DeptT.mechanical]),
    False
)
sinfo2 = SInfoT(
    "John",
    "Smith",
    GenT.male,
    5.8,
    SeqADT([DeptT.mechanical]),
    False
)
sinfo3 = SInfoT(
    "Jane",
    "Smith",
    GenT.female,
    7.8,
    SeqADT([DeptT.mechanical]),
    False
)
sinfo4 = SInfoT(
    "Fred",
    "Smith",
    GenT.male,
    4.9,
    SeqADT([DeptT.mechanical]),
    False
)
sinfo5 = SInfoT(
    "Eve",
    "Smith",
    GenT.female,
    11.8,
    SeqADT([DeptT.mechanical]),
    False
)

SALst.init()
SALst.add("stdnt1", sinfo1)
SALst.add("stdnt2", sinfo2)
SALst.add("stdnt3", sinfo3)
SALst.add("stdnt4", sinfo4)
SALst.add("stdnt5", sinfo5)

AALst.init()
SALst.allocate()
print(AALst.lst_alloc(DeptT.mechanical))
print(AALst.lst_alloc(DeptT.chemical))
print(AALst.lst_alloc(DeptT.software))

load_stdnt_data('StdntData.txt')
load_dcap_data('DeptCap.txt')
