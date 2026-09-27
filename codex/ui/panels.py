# -*- coding: utf-8 -*-
# CodeShield Encrypted Python — Powered by Repp76
import base64, sys, os

_cs_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in dir() else os.getcwd()
for _cs_p in (_cs_dir, os.getcwd()):
    if _cs_p not in sys.path:
        sys.path.insert(0, _cs_p)

_cs_parts = [
    "ZnJvbSBwYXRobGliIGltcG9ydCBQYXRoCgpmcm9tIHJpY2gucGFuZWwgaW1wb3J0IFBhbmVsCmZy",
    "b20gcmljaC5tYXJrZG93biBpbXBvcnQgTWFya2Rvd24KCmZyb20gLnRoZW1lIGltcG9ydCBjb25z",
    "b2xlCgoKZGVmIHNob3dfdXNlcih0ZXh0OiBzdHIpOgogICAgY29uc29sZS5wcmludChQYW5lbCh0",
    "ZXh0LCB0aXRsZT0iVVNFUiIsIGJvcmRlcl9zdHlsZT0id2hpdGUiLCB0aXRsZV9hbGlnbj0ibGVm",
    "dCIpKQoKCmRlZiBzaG93X2NvZGV4KHRleHQ6IHN0cik6CiAgICBjb25zb2xlLnByaW50KFBhbmVs",
    "KE1hcmtkb3duKHRleHQpLCB0aXRsZT0iQ09ERVgiLCBib3JkZXJfc3R5bGU9InJlZCIsIHRpdGxl",
    "X2FsaWduPSJsZWZ0IikpCgoKZGVmIHNob3dfZXJyb3IobWVzc2FnZTogc3RyLCBwcm92aWRlcjog",
    "c3RyID0gIiIsIHN1Z2dlc3Rpb246IHN0ciA9ICIiKToKICAgIGJvZHkgPSBtZXNzYWdlCiAgICBp",
    "ZiBzdWdnZXN0aW9uOgogICAgICAgIGJvZHkgKz0gZiJcblxuU3VnZ2VzdGVkIGFjdGlvbjoge3N1",
    "Z2dlc3Rpb259IgogICAgY29uc29sZS5wcmludChQYW5lbChib2R5LCB0aXRsZT0iQ09ERVggRVJS",
    "T1IiLCBib3JkZXJfc3R5bGU9ImJvbGQgcmVkIikpCgoKZGVmIHNob3dfdGVsZWdyYW1fZGVsaXZl",
    "cnkocmVzdWx0KToKICAgIGlmIHJlc3VsdC5vazoKICAgICAgICBuYW1lID0gUGF0aChyZXN1bHQu",
    "cGF0aCkubmFtZSBpZiByZXN1bHQucGF0aCBlbHNlICJ1bmtub3duIgogICAgICAgIGJvZHkgPSBm",
    "IkZpbGU6IHtuYW1lfVxuRGVzdGluYXRpb246IGNvbmZpZ3VyZWQgdXNlclxuU3RhdHVzOiBTRU5U",
    "IgogICAgICAgIGNvbnNvbGUucHJpbnQoUGFuZWwoYm9keSwgdGl0bGU9IlRFTEVHUkFNIERFTElW",
    "RVJZIiwgYm9yZGVyX3N0eWxlPSJib2xkIGdyZWVuIikpCiAgICBlbHNlOgogICAgICAgIGJvZHkg",
    "PSBmIlN0YXR1czogRkFJTEVEXG5SZWFzb246IHtyZXN1bHQucmVhc29uIG9yICd1bmtub3duIGVy",
    "cm9yJ30iCiAgICAgICAgaWYgcmVzdWx0LnJlYXNvbiBhbmQgInN0YXJ0ZWQgdGhlIGJvdCIgaW4g",
    "cmVzdWx0LnJlYXNvbjoKICAgICAgICAgICAgYm9keSArPSAiXG5cbk9wZW4gdGhlIENvZGV4IFRl",
    "bGVncmFtIGJvdCBhbmQgcHJlc3MgU3RhcnQsIHRoZW4gdHJ5IGFnYWluLiIKICAgICAgICBjb25z",
    "b2xlLnByaW50KFBhbmVsKGJvZHksIHRpdGxlPSJURUxFR1JBTSBERUxJVkVSWSBFUlJPUiIsIGJv",
    "cmRlcl9zdHlsZT0iYm9sZCByZWQiKSkKCgpkZWYgc2hvd19zdGF0dXMoc2Vzc2lvbiwgY29uZmln",
    "KToKICAgIHByb2plY3RfbmFtZSA9IHNlc3Npb24ucHJvamVjdC5yb290Lm5hbWUgaWYgc2Vzc2lv",
    "bi5wcm9qZWN0IGVsc2UgIm5vbmUiCiAgICBjb25zb2xlLnByaW50KAogICAgICAgIGYiW2NvZGV4",
    "LnJlZF1DT0RFWFsvXSAgfCAge3Nlc3Npb24ucHJvdmlkZXIudXBwZXIoKX0gIHwgIHtzZXNzaW9u",
    "Lm1vZGVsIG9yICdkZWZhdWx0J30gIHwgICIKICAgICAgICBmIlBST0pFQ1Q6IHtwcm9qZWN0X25h",
    "bWV9ICB8ICBSRUFEWSIKICAgICkK"
]
_cs_code = base64.b64decode("".join(_cs_parts)).decode("utf-8")
_cs_file = __file__ if "__file__" in dir() else "<codeshield>"
_cs_compiled = compile(_cs_code, _cs_file, "exec")

# Bersihkan helper vars supaya globals() yang exec() terima
# hampir sama dengan modul tulen — __name__/__package__/__spec__
# dikekalkan sebab ia sudah wujud betul dalam globals() ini,
# disediakan oleh Python sendiri sebelum baris ini jalan.
for _cs_name in ("base64", "_cs_dir", "_cs_p", "_cs_name"):
    globals().pop(_cs_name, None)

exec(_cs_compiled, globals())
