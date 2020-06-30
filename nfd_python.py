import ctypes
import sys

sOS=sys.platform

if sOS=="win32":
    if ctypes.sizeof(ctypes.c_voidp)==4:
        hllDll=ctypes.CDLL("win32/nfd.dll")
    elif ctypes.sizeof(ctypes.c_voidp)==8:
        hllDll=ctypes.CDLL("win64/nfd.dll")

NFD_CreateScanHandle=hllDll.NFD_CreateScanHandle
NFD_CreateScanHandle.restype=ctypes.c_int

NFD_ScanFileA=hllDll.NFD_ScanFileA
NFD_ScanFileA.restype=ctypes.c_char_p
NFD_ScanFileA.argtypes=[ctypes.c_int,ctypes.c_char_p,ctypes.c_int]

NFD_CloseScanHandle=hllDll.NFD_CloseScanHandle
NFD_CloseScanHandle.argtypes=[ctypes.c_int]

##SF_RECURSIVE        =0x00000001,
##SF_DEEPSCAN         =0x00000002,
##SF_RESULTASXML      =0x00000004,
##SF_RESULTASJSON     =0x00000008,
##SF_HEURISTICSCAN    =0x00000010,

nFlags=(ctypes.c_int)(1|2)

sFileName="C:/Windows/regedit.exe"

b_sFileName=sFileName.encode('utf-8')

hHandle=(ctypes.c_int)(NFD_CreateScanHandle())
sResult=NFD_ScanFileA(hHandle,b_sFileName,nFlags)

print (sResult.decode("utf-8"))

NFD_CloseScanHandle(hHandle)


