FROM ramadhani892/ramubot:master
# ======================
#    ZX-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
RUN git clone -b master https://github.com/zxcal/ZX-UBOT /home/ramagans/
WORKDIR /home/ramagans/
CMD ["python3", "-m", "userbot"]
