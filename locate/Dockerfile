FROM debian:11

COPY *.for /opt/locate/

WORKDIR /opt/locate/

RUN apt update && apt install gfortran -y

RUN gfortran locate.for mapll.for mapxy.for -o locatefor

CMD ["./locatefor"]