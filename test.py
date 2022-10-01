import time
import win32com.client

auraSdk = win32com.client.Dispatch("aura.sdk.1")
print('SwitchMode...')
auraSdk.SwitchMode()
print('Enumerate...')
devices = auraSdk.Enumerate(0)

#['AddRef', 'Apply', 'GetIDsOfNames', 'GetTypeInfo', 'GetTypeInfoCount',
# 'Height', 'Invoke', 'Lights', 'Name', 'QueryInterface', 'Release', 'Type',
# 'Width', '_ApplyTypes_', '_FlagAsMethod', '_LazyAddAttr_', '_NewEnum',
# '_Release_', '_UpdateWithITypeInfo_', '__AttrToID__', '__LazyMap__',
# '__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattr__',
# '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__int__', '__le__', '__len__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', '_builtMethods_', '_dir_ole_', '_enum_',
# '_find_dispatch_type_', '_get_good_object_', '_get_good_single_object_',
# '_lazydata_', '_make_method_', '_mapCachedItems_', '_oleobj_', '_olerepr_',
# '_print_details_', '_proc_', '_unicode_to_string_', '_username_',
# '_wrap_dispatch_']

'''
[ENE_RGB_For_ASUS0] 8
[ENE_RGB_For_ASUS1] 8
[ENE_RGB_For_ASUS2] 8
[ENE_RGB_For_ASUS3] 8
[WaterCooler] 4
[Mainboard_Master] 8
[AddressableStrip 1] 120
[AddressableStrip 2] 120
'''


mem = [devices[1], devices[3], devices[0], devices[2]]
water = devices[4]
board = devices[5]
top = devices[6]


def mem4(l: list(), slp: int = 0.1) -> None:
    assert(len(l) == 4)
    for i in l:
        assert(type(i) == int)
        assert(0 <= i <= 8)
    for i in range(4):
        for j in range(l[i]):
            mem[i].Lights(j).color = 0xff0000
        for j in range(l[i], 8):
            mem[i].Lights(j).color = 0x0000ff
        mem[i].Apply()
    time.sleep(slp)


def mem32(l: list(), slp: int = 0.1) -> None:
    assert(len(l) == 4)
    for i in l:
        assert(type(i) == list)
        assert(len(i) == 8)
        for j in i:
            assert(type(j) == int)
            assert(0 <= j <= 0xffffff)
    for i in range(4):
        for j in range(8):
            mem[i].Lights(j).color = l[i][j]
        mem[i].Apply()
    time.sleep(slp)

print('Begin...')

mem4([0, 0, 0, 0])

l = [3, 2, 1, 0]
r = [1]*8 + [-1]*8

for i in range(2147483647):
    mem4(l)
    l = l[1:]
    l.append(l[-1]+r[i & 15])

print('End...')
input()
