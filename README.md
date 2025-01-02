# Towed vehicles Search backend

Backend for towed (vehicle[https://github.com/fegbewunmi/search-ui])
Search bar ui using Flask and Elasticsearch

The data is gotten from dataset of towed vehicles in Chicago
https://dev.socrata.com/foundry/data.cityofchicago.org/ygr5-vcbg

# Local development

The commands in Makefile are used to build, start and stop the application

To build the application:

```
make build
```

To start the application:

```
make start
```

Once the flask container is running the api can be accessed using SwaggerUI - http://0.0.0.0:5002/apidocs

To stop the application:

```
make stop
```
