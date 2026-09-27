# -*- coding: utf-8 -*-
# CodeShield Encrypted Python — Powered by Repp76
import base64, sys, os

_cs_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in dir() else os.getcwd()
for _cs_p in (_cs_dir, os.getcwd()):
    if _cs_p not in sys.path:
        sys.path.insert(0, _cs_p)

_cs_parts = [
    "aW1wb3J0IG9zCmZyb20gZGF0YWNsYXNzZXMgaW1wb3J0IGRhdGFjbGFzcwpmcm9tIGRvdGVudiBp",
    "bXBvcnQgbG9hZF9kb3RlbnYKCmZyb20gdXRpbHMuc2VjdXJpdHkgaW1wb3J0IG1hc2tfc2VjcmV0",
    "Cgpsb2FkX2RvdGVudigpCgpQUk9WSURFUl9LRVlTID0gewogICAgIm9wZW5haSI6ICJPUEVOQUlf",
    "QVBJX0tFWSIsCiAgICAiZ2VtaW5pIjogIkdFTUlOSV9BUElfS0VZIiwKICAgICJhbnRocm9waWMi",
    "OiAiQU5USFJPUElDX0FQSV9LRVkiLAogICAgImRlZXBzZWVrIjogIkRFRVBTRUVLX0FQSV9LRVki",
    "LAogICAgIm9wZW5yb3V0ZXIiOiAiT1BFTlJPVVRFUl9BUElfS0VZIiwKfQoKCkBkYXRhY2xhc3MK",
    "Y2xhc3MgVGVsZWdyYW1Db25maWc6CiAgICBib3RfdG9rZW46IHN0ciB8IE5vbmUKICAgIHN1cGVy",
    "X2FkbWluX2lkOiBzdHIgfCBOb25lICAjIG93bmVyL2RldmVsb3BlciAtLSByZWNlaXZlcyBhZG1p",
    "biBub3RpZmljYXRpb25zCiAgICB1c2VyX2lkOiBzdHIgfCBOb25lICAgICAgICAgIyB0aGUgbGlu",
    "a2VkIHVzZXIgLS0gcmVjZWl2ZXMgZ2VuZXJhdGVkIGZpbGVzL2NvbnRlbnQKICAgIGF1dG9fc2Vu",
    "ZF9maWxlczogYm9vbAogICAgYXV0b19zZW5kX3Byb2plY3RzOiBib29sCiAgICBhdXRvX3NlbmRf",
    "Y2hhdDogYm9vbAoKICAgIEBwcm9wZXJ0eQogICAgZGVmIGVuYWJsZWQoc2VsZikgLT4gYm9vbDoK",
    "ICAgICAgICByZXR1cm4gYm9vbChzZWxmLmJvdF90b2tlbikKCgpkZWYgX3BhcnNlX2Jvb2wodmFs",
    "dWU6IHN0ciB8IE5vbmUsIGRlZmF1bHQ6IGJvb2wpIC0+IGJvb2w6CiAgICBpZiB2YWx1ZSBpcyBO",
    "b25lIG9yIHZhbHVlID09ICIiOgogICAgICAgIHJldHVybiBkZWZhdWx0CiAgICByZXR1cm4gdmFs",
    "dWUuc3RyaXAoKS5sb3dlcigpIGluICgiMSIsICJ0cnVlIiwgInllcyIsICJvbiIpCgoKY2xhc3Mg",
    "Q29uZmlnOgogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIHNlbGYuZGVmYXVsdF9wcm92",
    "aWRlciA9IG9zLmdldGVudigiREVGQVVMVF9QUk9WSURFUiIsICJvcGVuYWkiKS5sb3dlcigpCiAg",
    "ICAgICAgc2VsZi5kZWZhdWx0X21vZGVsID0gb3MuZ2V0ZW52KCJERUZBVUxUX01PREVMIiwgIiIp",
    "CgogICAgICAgICMgVEVMRUdSQU1fQ0hBVF9JRCBpcyB0aGUgb2xkIHZhcmlhYmxlIG5hbWUgc29t",
    "ZSB1c2VycyBtYXkgc3RpbGwgaGF2ZSBzZXQ7CiAgICAgICAgIyBURUxFR1JBTV9VU0VSX0lEIHRh",
    "a2VzIHByaW9yaXR5IHdoZW4gYm90aCBhcmUgcHJlc2VudC4KICAgICAgICB1c2VyX2lkID0gb3Mu",
    "Z2V0ZW52KCJURUxFR1JBTV9VU0VSX0lEIikgb3Igb3MuZ2V0ZW52KCJURUxFR1JBTV9DSEFUX0lE",
    "Iikgb3IgTm9uZQoKICAgICAgICBzZWxmLnRlbGVncmFtID0gVGVsZWdyYW1Db25maWcoCiAgICAg",
    "ICAgICAgIGJvdF90b2tlbj1vcy5nZXRlbnYoIlRFTEVHUkFNX0JPVF9UT0tFTiIpIG9yIE5vbmUs",
    "CiAgICAgICAgICAgIHN1cGVyX2FkbWluX2lkPW9zLmdldGVudigiVEVMRUdSQU1fU1VQRVJfQURN",
    "SU5fSUQiKSBvciBOb25lLAogICAgICAgICAgICB1c2VyX2lkPXVzZXJfaWQsCiAgICAgICAgICAg",
    "IGF1dG9fc2VuZF9maWxlcz1fcGFyc2VfYm9vbChvcy5nZXRlbnYoIlRFTEVHUkFNX0FVVE9fU0VO",
    "RF9GSUxFUyIpLCBkZWZhdWx0PVRydWUpLAogICAgICAgICAgICBhdXRvX3NlbmRfcHJvamVjdHM9",
    "X3BhcnNlX2Jvb2wob3MuZ2V0ZW52KCJURUxFR1JBTV9BVVRPX1NFTkRfUFJPSkVDVFMiKSwgZGVm",
    "YXVsdD1UcnVlKSwKICAgICAgICAgICAgYXV0b19zZW5kX2NoYXQ9X3BhcnNlX2Jvb2wob3MuZ2V0",
    "ZW52KCJURUxFR1JBTV9BVVRPX1NFTkRfQ0hBVCIpLCBkZWZhdWx0PUZhbHNlKSwKICAgICAgICAp",
    "CiAgICAgICAgc2VsZi5fa2V5cyA9IHtuYW1lOiBvcy5nZXRlbnYoZW52X3Zhcikgb3IgTm9uZSBm",
    "b3IgbmFtZSwgZW52X3ZhciBpbiBQUk9WSURFUl9LRVlTLml0ZW1zKCl9CgogICAgZGVmIGtleV9m",
    "b3Ioc2VsZiwgcHJvdmlkZXI6IHN0cikgLT4gc3RyIHwgTm9uZToKICAgICAgICByZXR1cm4gc2Vs",
    "Zi5fa2V5cy5nZXQocHJvdmlkZXIpCgogICAgZGVmIGNvbmZpZ3VyZWRfcHJvdmlkZXJzKHNlbGYp",
    "IC0+IGxpc3Rbc3RyXToKICAgICAgICByZXR1cm4gW25hbWUgZm9yIG5hbWUsIGtleSBpbiBzZWxm",
    "Ll9rZXlzLml0ZW1zKCkgaWYga2V5XQoKICAgIGRlZiBzdGF0dXNfbGluZXMoc2VsZik6CiAgICAg",
    "ICAgcmV0dXJuIFsobmFtZSwgYm9vbChrZXkpLCBtYXNrX3NlY3JldChrZXkpIGlmIGtleSBlbHNl",
    "IE5vbmUpIGZvciBuYW1lLCBrZXkgaW4gc2VsZi5fa2V5cy5pdGVtcygpXQoKCmNvbmZpZyA9IENv",
    "bmZpZygpCg=="
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
