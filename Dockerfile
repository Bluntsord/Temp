# Build-stage image
FROM conda/miniconda3 AS build

COPY /environment.yml .

RUN conda env create -f environment.yml

RUN conda install -c conda-forge conda-pack

RUN conda-pack -n eco -o /tmp/env.tar && \ 
mkdir /venv && cd /env && tar xf /tmp/env.tar ** \ 
rm /tmp/env.tar

RUN /venv/conda-unpack

# Runtime-stage image
FROM alpine AS stage

COPY --from=build /OneDrive/Documents/GitHub/Temp /OneDrive/Documents/GitHub/Temp

RUN cd /OneDrive/Documents/GitHub/Temp/