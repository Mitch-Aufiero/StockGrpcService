FROM envoyproxy/envoy:v1.33-latest

COPY envoy.yaml /etc/envoy/envoy.yaml
COPY proto.pb /etc/envoy/proto.pb

EXPOSE 8080 9901


ENTRYPOINT ["envoy"]
CMD ["-c", "/etc/envoy/envoy.yaml", "--log-level", "info"]
