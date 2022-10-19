#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    from khayyam import JalaliDatetime

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    if len(data) > 1:
        try:
            JalaliDatetime.strptime(fdp.ConsumeUnicode(len(data)//2), fdp.ConsumeUnicode(len(data)//2))
        except ValueError:
            pass


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()