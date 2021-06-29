FROM customnginx
RUN rm -rf /var/lib/apt/lists/*
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]