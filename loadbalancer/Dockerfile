ARG AUTHOR
ARG NGINX_VERSION

FROM nginx:${NGINX_VERSION}
# Set label.
LABEL maintainer=$AUTHOR
# Copy all configure's files.
COPY nginx.conf /etc/nginx/nginx.conf
COPY my_nginx.conf /etc/nginx/conf.d/
# COPY my_nginx.conf /etc/nginx/sites-available/
# COPY nginx.crt /etc/nginx/ssl/nginx.crt
# COPY nginx.key /etc/nginx/ssl/nginx.key
# Link the conf file.
# RUN mkdir -p /etc/nginx/sites-enabled/\
    # && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/

# Set upstream conf and remove the default conf
# RUN echo "upstream ${NGINX_UPSTREAM_CONTAINER} { server unix:///socket_app1/app.sock; server unix:///socket_app2/app.sock; }" > /etc/nginx/conf.d/upstream.conf \
    # && rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/conf.d/default.conf
# Expose the ports
EXPOSE 80 8080 443

CMD ["nginx", "-g", "daemon off;"]
# COPY ./startup.sh /opt/startup.sh
# RUN sed -i 's/\r//g' /opt/startup.sh
# Execute the command.
# CMD ["/bin/bash", "/opt/startup.sh"]