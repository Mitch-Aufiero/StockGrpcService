FROM envoyproxy/envoy-dev:e4955aed5694f9935d674419dbb364e744f697b4

COPY envoy.yaml /etc/envoy/envoy.yaml
COPY proto.pb /etc/envoy/proto.pb

EXPOSE 8080 9901


ENTRYPOINT ["envoy"]
CMD ["-c", "/etc/envoy/envoy.yaml", "--log-level", "info"]
