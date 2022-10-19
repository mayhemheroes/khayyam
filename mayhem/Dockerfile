FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /khayyam
WORKDIR /khayyam
RUN python3 -m pip install . && chmod +x fuzz/khayyam_fuzz.py

ENTRYPOINT [ ]
CMD ["/mrtparse/fuzz/khayyam_fuzz.py"]