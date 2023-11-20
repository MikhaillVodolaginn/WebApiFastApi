from fastapi import FastAPI, Request


tags_metadata = [
    {
        "name": "HTTP Methods",
        "description": "Testing different HTTP verbs",
    },
    {
        "name": "Request Inspection",
        "description": "Inspect the request data",
    },
]

app = FastAPI(openapi_tags=tags_metadata)


def fill_response(request: Request):
    response = {"args": {}, "data": "", "files": {}, "form": {}, 'headers': request.headers,
                'json': None, 'origin': request.client.host, 'url': request.url._url}

    return response


@app.delete("/delete", tags=['HTTP Methods'])
async def the_requests_delete_parameters(request: Request):
    response = fill_response(request)
    return response


@app.get("/get", tags=['HTTP Methods'])
async def the_requests_query_parameters(request: Request):
    return {'args': {}, 'headers': request.headers, 'origin': request.client.host, 'url': request.url._url}


@app.patch("/patch", tags=['HTTP Methods'])
async def the_requests_patch_parameters(request: Request):
    response = fill_response(request)
    return response


@app.post("/post", tags=['HTTP Methods'])
async def the_requests_post_parameters(request: Request):
    response = fill_response(request)
    return response


@app.put("/put", tags=['HTTP Methods'])
async def the_requests_put_parameters(request: Request):
    response = fill_response(request)
    return response


@app.get("/headers", tags=['Request Inspection'])
async def return_the_incoming_requests_HTTP_headers(request: Request):
    return {'headers': request.headers}


@app.get("/ip", tags=['Request Inspection'])
async def Returns_the_requesters_IP_Address(request: Request):
    return {'origin': request.client.host}


@app.get("/user-agent", tags=['Request Inspection'])
async def return_the_incoming_requests_UserAgent_header(request: Request):
    return {'user-agent': request.headers['user-agent']}
