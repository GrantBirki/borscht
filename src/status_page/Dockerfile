FROM louislam/uptime-kuma:1.12.1-alpine

# Here we load a custom StatusPage image. If this ever updates a new one will need to be pulled from the source
# source: https://github.com/louislam/uptime-kuma
COPY custom/StatusPage.8e2492a0.js dist/assets/StatusPage.8e2492a0.js
COPY custom/index.html dist/index.html
COPY custom/index.html .
COPY custom/api-router.js server/routers/api-router.js

EXPOSE 3001
VOLUME ["/app/data"]
HEALTHCHECK --interval=60s --timeout=30s --start-period=180s --retries=5 CMD node extra/healthcheck.js
ENTRYPOINT ["/usr/bin/dumb-init", "--", "extra/entrypoint.sh"]
CMD ["node", "server/server.js"]
