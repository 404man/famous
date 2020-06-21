### Build and install packages
FROM python:3.8 as build-python
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

### Final image
FROM python:3.8-slim

# biuld evn variable
ARG STATIC_URL
#dynamic ENV Values from ARG
ENV STATIC_URL ${STATIC_URL:-/static/}

RUN groupadd -r famous && useradd -r -g famous famous

RUN apt-get update \
  && apt-get install -y \
    libxml2 \
    libssl1.1 \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    shared-mime-info \
    mime-support \
  && apt-get clean \
  && rm -rf /var/lib/apt/list/*

COPY . /app
COPY --from=build-python /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
WORKDIR /app
#RUN SECRET_KEY=dummy STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input
RUN STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input
RUN mkdir -p /app/media /app/static \
  && chown -R famous:famous /app/

EXPOSE 8000
ENV PORT 8000
ENV PYTHONUNBUFFERED 1
CMD ["uwsgi", "--ini", "/app/famous/wsgi/uwsgi.ini"]