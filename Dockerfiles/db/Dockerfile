FROM alpine:3.10
MAINTAINER My Name "royerleandroroblesvega.com"
RUN apk add --update sqlite
ADD DBAUDITORIA /
ENTRYPOINT ["sqlite3"]
CMD ["DBAUDITORIA"]