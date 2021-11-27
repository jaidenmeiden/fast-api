### Activate environment
```
source venv/bin/activate
```
### Deactivate environment
```
deactivate
```
### Install tools
```
pip install fastapi uvicorn 
```

### Launch application
```
uvicorn main:app --reload
```

# Specification fastAPI

[Path Operation](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/?h=path+operation)

[Path parameters](https://fastapi.tiangolo.com/tutorial/path-params/)

[Query parameters](https://fastapi.tiangolo.com/tutorial/query-params/?h=query+parameters)

[Request Body](https://fastapi.tiangolo.com/tutorial/body/)

[Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)

[Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/)

# Tools

### [fastAPI](https://fastapi.tiangolo.com/)

Source Code: https://github.com/tiangolo/fastapi

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).

Fast to code: Increase the speed to develop features by about 200% to 300%. *

Fewer bugs: Reduce about 40% of human (developer) induced errors. *
Intuitive: Great editor support. Completion everywhere. Less time debugging.
Easy: Designed to be easy to use and learn. Less time reading docs.
Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
Robust: Get production-ready code. With automatic interactive documentation.
Standards-based: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).

## Documentation Tools

### [Swagger](https://swagger.io/)

Tools: https://swagger.io/tools/

Relation: https://swagger.io/resources/open-api/

Source Code: https://github.com/swagger-api

Simplify API development for users, teams, and enterprises with the Swagger open source and professional toolset. Find out how Swagger can help you design and document your APIs at scale.

### [Redoc](https://redoc.ly/redoc)

Source Code: https://github.com/Redocly/redoc

Let us help you transform your OpenAPI definition into comprehensive and interactive documentation.

### [OpenAPI](https://www.openapis.org/)

The OpenAPI Specification: https://github.com/OAI/OpenAPI-Specification

Source Code: https://github.com/oai

The OpenAPI Initiative (OAI) was created by a consortium of forward-looking industry experts who recognize the immense value of standardizing on how APIs are described. As an open governance structure under the Linux Foundation, the OAI is focused on creating, evolving and promoting a vendor neutral description format. The OpenAPI Specification was originally based on the Swagger Specification, donated by SmartBear Software.

## Technical Tools

### [Uvicorn](https://www.uvicorn.org/)

Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

Until recently Python has lacked a minimal low-level server/application interface for asyncio frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all asyncio frameworks.

ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.

Uvicorn currently supports HTTP/1.1 and WebSockets. Support for HTTP/2 is planned


### [Pydantic](https://pydantic-docs.helpmanual.io/)

Data validation and settings management using python type annotations.

Pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.

Define how data should be in pure, canonical python; validate it with pydantic.


### [Starlette](https://www.starlette.io/)

Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.

It is production-ready, and gives you the following:

* Seriously impressive performance.
* WebSocket support.
* In-process background tasks.
* Startup and shutdown events.
* Test client built on requests.
* CORS, GZip, Static Files, Streaming responses.
* Session and Cookie support.
* 100% test coverage.
* 100% type annotated codebase.
* Few hard dependencies.

