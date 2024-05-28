from fastapi import FastAPI, Depends
from fastsupabased_acl import FastSupabasedACL

acl = FastSupabasedACL(role=["admin"])


app = FastAPI()

@app.get("/open-route")
def open_route():
    return {"message": "Hello, world! This is an open route!"}


@app.get("/admin", dependencies=[Depends(acl)])
def admin():
    return {"message": "Hello, admin!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)