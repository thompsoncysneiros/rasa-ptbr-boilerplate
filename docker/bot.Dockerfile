FROM rasa/rasa:2.8.31-full

USER root
RUN apt install make

WORKDIR /bot
COPY ./bot /bot
COPY ./modules /modules

ENTRYPOINT []
CMD []
