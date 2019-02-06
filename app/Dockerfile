ARG AUTHOR
ARG PYTHON_VERSION
ARG CONTAINER_LOGFILE_PATH
ARG APP_CODE_PATH_CONTAINER

FROM python:${PYTHON_VERSION}
# Set label.
LABEL maintainer=${AUTHOR}
# Log folder for uwsgi
RUN mkdir /uwsgi_logs
# Source codes.
RUN mkdir /app
WORKDIR /app
COPY src/. .
# Install all applications.
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
# Run the flask app by uwsgi.
CMD ["uwsgi",  "--ini", "uwsgi_app.ini"]