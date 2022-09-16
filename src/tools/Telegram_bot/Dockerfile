FROM python:latest
COPY bot.py .
COPY mnf.yaml .
COPY img0.jpg .
COPY img1.jpg .
RUN pip3 install pyTelegramBotAPI
RUN pip3 install numpy
ENTRYPOINT [ "python3" ]
CMD ["bot.py"]