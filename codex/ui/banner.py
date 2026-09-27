# -*- coding: utf-8 -*-
# CodeShield Encrypted Python — Powered by Repp76
import base64, sys, os

_cs_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in dir() else os.getcwd()
for _cs_p in (_cs_dir, os.getcwd()):
    if _cs_p not in sys.path:
        sys.path.insert(0, _cs_p)

_cs_parts = [
    "aW1wb3J0IG9zCmltcG9ydCBwbGF0Zm9ybQppbXBvcnQgc3lzCmZyb20gcGF0aGxpYiBpbXBvcnQg",
    "UGF0aAoKZnJvbSBjb25zdGFudHMgaW1wb3J0IFZFUlNJT04sIERFVkVMT1BFUgpmcm9tIC50aGVt",
    "ZSBpbXBvcnQgY29uc29sZQoKQkFOTkVSID0gciIiIgog4paI4paI4paI4paI4paI4paI4pWXIOKW",
    "iOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI",
    "4paI4paI4pWX4paI4paI4pWXICDilojilojilZcK4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI",
    "4paI4pWU4pWQ4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU",
    "4pWQ4pWQ4pWQ4pWQ4pWd4pWa4paI4paI4pWX4paI4paI4pWU4pWdCuKWiOKWiOKVkSAgICAg4paI",
    "4paI4pWRICAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilojilojilojilZcg",
    "ICDilZrilojilojilojilZTilZ0K4paI4paI4pWRICAgICDilojilojilZEgICDilojilojilZHi",
    "lojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVnSAgIOKWiOKWiOKVlOKWiOKWiOKV",
    "lwrilZrilojilojilojilojilojilojilZfilZrilojilojilojilojilojilojilZTilZ3iloji",
    "lojilojilojilojilojilZTilZ3ilojilojilojilojilojilojilojilZfilojilojilZTilZ0g",
    "4paI4paI4pWXCiDilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOKV",
    "muKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZ0gIOKV",
    "muKVkOKVnQoiIiIKCgpkZWYgY2xlYXJfc2NyZWVuKCk6CiAgICAiIiJDbGVhciB0aGUgdGVybWlu",
    "YWwgcmVsaWFibHkgYWNyb3NzIExpbnV4LCBUZXJtdXgsIG1hY09TIGFuZCBXaW5kb3dzLgoKICAg",
    "IE5laXRoZXIgb3Muc3lzdGVtKCJjbGVhciIvImNscyIpIGFsb25lIG5vciBSaWNoJ3Mgb3duIENv",
    "bnNvbGUuY2xlYXIoKQogICAgaXMgZW5vdWdoIGV2ZXJ5d2hlcmUgLS0gb3Muc3lzdGVtIGRvZXMg",
    "bm90aGluZyB3aGVuIHN0ZG91dCBpc24ndCBhCiAgICByZWFsIHR0eSAoY29tbW9uIG92ZXIgVGVy",
    "bXV4L1NTSCBzZXNzaW9ucyksIGFuZCBhIHBsYWluIEFOU0kgY2xlYXIgY2FuCiAgICBsZWF2ZSBz",
    "Y3JvbGxiYWNrIGJlaGluZCBvbiBzb21lIHRlcm1pbmFscy4gU3RhY2tpbmcgYm90aCwgdGhlbgog",
    "ICAgZXhwbGljaXRseSByZXNldHRpbmcgY3Vyc29yICsgc2NyZWVuICsgc2Nyb2xsYmFjaywgaXMg",
    "d2hhdCBhY3R1YWxseQogICAgbWFrZXMgb2xkIG91dHB1dCBkaXNhcHBlYXIgYmVmb3JlIHRoZSBi",
    "YW5uZXIgcHJpbnRzLgogICAgIiIiCiAgICBpZiBwbGF0Zm9ybS5zeXN0ZW0oKSA9PSAiV2luZG93",
    "cyI6CiAgICAgICAgb3Muc3lzdGVtKCJjbHMiKQogICAgZWxzZToKICAgICAgICBvcy5zeXN0ZW0o",
    "ImNsZWFyIikKCiAgICBzeXMuc3Rkb3V0LndyaXRlKCJcMDMzW0hcMDMzWzJKXDAzM1szSiIpCiAg",
    "ICBzeXMuc3Rkb3V0LmZsdXNoKCkKCgpkZWYgc2hvd19zdGFydHVwKGNvbmZpZyk6CiAgICAjIE5v",
    "dGhpbmcgLS0gbm8gbG9nZ2luZywgbm8gcHJvdmlkZXIgY2hlY2tzLCBubyBUZWxlZ3JhbSBpbml0",
    "IC0tIG1heQogICAgIyBwcmludCBhbnl0aGluZyBiZWZvcmUgdGhpcyBjYWxsLiBjbGVhcl9zY3Jl",
    "ZW4oKSBtdXN0IGJlIHRoZSB2ZXJ5CiAgICAjIGZpcnN0IHZpc2libGUgdGhpbmcgdGhhdCBoYXBw",
    "ZW5zLgogICAgY2xlYXJfc2NyZWVuKCkKCiAgICBjb25zb2xlLnByaW50KEJBTk5FUiwgc3R5bGU9",
    "ImNvZGV4LnJlZCIpCiAgICBjb25zb2xlLnByaW50KCJBSSBDT0RFIEVOR0lORSIsIHN0eWxlPSJj",
    "b2RleC5kaW0iLCBqdXN0aWZ5PSJjZW50ZXIiKQogICAgY29uc29sZS5wcmludCgpCiAgICBjb25z",
    "b2xlLnByaW50KGYiRGV2ZWxvcGVyOiB7REVWRUxPUEVSfSIsIHN0eWxlPSJjb2RleC5kaW0iKQog",
    "ICAgY29uc29sZS5wcmludChmIlZlcnNpb246IHtWRVJTSU9OfSIsIHN0eWxlPSJjb2RleC5kaW0i",
    "KQogICAgY29uc29sZS5wcmludCgiTW9kZTogQUkgQ29kaW5nIEFzc2lzdGFudCIsIHN0eWxlPSJj",
    "b2RleC5kaW0iKQogICAgY29uc29sZS5wcmludCgpCgogICAgY29uc29sZS5wcmludCgiWyBTWVNU",
    "RU0gXSIsIHN0eWxlPSJjb2RleC5yZWQiKQogICAgY29uc29sZS5wcmludChmIiAgUHl0aG9uOiB7",
    "cGxhdGZvcm0ucHl0aG9uX3ZlcnNpb24oKX0gT0siLCBzdHlsZT0iY29kZXguZGltIikKICAgIGNv",
    "bnNvbGUucHJpbnQoZiIgIE9TOiB7cGxhdGZvcm0uc3lzdGVtKCl9Iiwgc3R5bGU9ImNvZGV4LmRp",
    "bSIpCiAgICBjb25zb2xlLnByaW50KGYiICBEaXJlY3Rvcnk6IHtQYXRoLmN3ZCgpfSIsIHN0eWxl",
    "PSJjb2RleC5kaW0iKQogICAgY29uc29sZS5wcmludCgpCgogICAgY29uc29sZS5wcmludCgiWyBQ",
    "Uk9WSURFUlMgXSIsIHN0eWxlPSJjb2RleC5yZWQiKQogICAgZm9yIG5hbWUsIG9rLCBtYXNrZWQg",
    "aW4gY29uZmlnLnN0YXR1c19saW5lcygpOgogICAgICAgIHN0YXR1cyA9ICJbY29kZXgub2tdQ29u",
    "ZmlndXJlZFsvXSIgaWYgb2sgZWxzZSAiW2NvZGV4LmVycl1Ob3QgY29uZmlndXJlZFsvXSIKICAg",
    "ICAgICBzdWZmaXggPSBmIiAoe21hc2tlZH0pIiBpZiBvayBlbHNlICIiCiAgICAgICAgY29uc29s",
    "ZS5wcmludChmIiAge25hbWV9OiB7c3RhdHVzfXtzdWZmaXh9IikKICAgIGNvbnNvbGUucHJpbnQo",
    "KQoKICAgIGNvbnNvbGUucHJpbnQoIlsgVEVMRUdSQU0gXSIsIHN0eWxlPSJjb2RleC5yZWQiKQog",
    "ICAgaWYgY29uZmlnLnRlbGVncmFtLmVuYWJsZWQ6CiAgICAgICAgY29uc29sZS5wcmludCgiICBC",
    "b3Q6IFtjb2RleC5va11Db25uZWN0ZWRbL10iKQogICAgICAgIHVzZXJfc3RhdHVzID0gIltjb2Rl",
    "eC5va11Db25maWd1cmVkWy9dIiBpZiBjb25maWcudGVsZWdyYW0udXNlcl9pZCBlbHNlICJbY29k",
    "ZXguZGltXU5vdCBsaW5rZWQgeWV0Wy9dIgogICAgICAgIGFkbWluX3N0YXR1cyA9ICJbY29kZXgu",
    "b2tdQ29uZmlndXJlZFsvXSIgaWYgY29uZmlnLnRlbGVncmFtLnN1cGVyX2FkbWluX2lkIGVsc2Ug",
    "Iltjb2RleC5kaW1dTm90IGNvbmZpZ3VyZWRbL10iCiAgICAgICAgY29uc29sZS5wcmludChmIiAg",
    "VXNlciBJRDoge3VzZXJfc3RhdHVzfSIpCiAgICAgICAgY29uc29sZS5wcmludChmIiAgU3VwZXIg",
    "QWRtaW46IHthZG1pbl9zdGF0dXN9IikKICAgIGVsc2U6CiAgICAgICAgY29uc29sZS5wcmludCgi",
    "ICBCb3Q6IFtjb2RleC5kaW1dTm90IGNvbmZpZ3VyZWRbL10iKQogICAgY29uc29sZS5wcmludCgp",
    "CgogICAgaWYgbm90IGNvbmZpZy5jb25maWd1cmVkX3Byb3ZpZGVycygpOgogICAgICAgIGNvbnNv",
    "bGUucHJpbnQoIk5vIHByb3ZpZGVyIGNvbmZpZ3VyZWQuIEFkZCBhbiBBUEkga2V5IHRvIC5lbnYg",
    "YmVmb3JlIGNoYXR0aW5nLiIsIHN0eWxlPSJjb2RleC53YXJuIikKICAgIGNvbnNvbGUucHJpbnQo",
    "IlR5cGUgL2hlbHAgZm9yIGNvbW1hbmRzLiIsIHN0eWxlPSJjb2RleC5kaW0iKQogICAgY29uc29s",
    "ZS5wcmludCgpCg=="
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
