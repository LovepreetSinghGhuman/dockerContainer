# We can always see if this is still the latest version or not...
FROM nginx:1.25.3-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

# In this Dockerfile, we do not need to use a CMD option, because that will already be included in the official nginx image.