from fastapi import FastAPI

app = FastAPI()


response = {
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru",
    "Content-Length": "0",
    "Host": "httpbin.org",
    "Origin": "http://httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "X-Amzn-Trace-Id": "Root=1-655ba4d3-4283502f613f4d6545ef2801"
  },
  "json": None,
  "origin": "95.26.71.223",
  "url": "http://httpbin.org/get"
}


@app.delete("/delete")
async def the_requests_delete_parameters():
    response["url"] = "http://httpbin.org/delete"

    return response


@app.get("/get")
async def the_requests_query_parameters():
    return response


@app.patch("/patch")
async def the_requests_patch_parameters():
    response["url"] = "http://httpbin.org/patch"

    return response


@app.post("/post")
async def the_requests_post_parameters():
    response["url"] = "http://httpbin.org/post"

    return response


@app.put("/put")
async def the_requests_put_parameters():
    response["url"] = "http://httpbin.org/put"

    return response
