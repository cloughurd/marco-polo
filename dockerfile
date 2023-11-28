FROM golang:latest

WORKDIR /src
ENV CGO_ENABLED=1

COPY . .

RUN go mod download
RUN go build

EXPOSE 8080

ENTRYPOINT [ "/bin/bash" ]
