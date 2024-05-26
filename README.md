# FastSupabased ACL

This is a simple ACL (Access Control List) implementation for Supabase. It is based on the [FastAPI](https://fastapi.tiangolo.com/) framework.

## Installation

```bash
pip install fastsupabased-acl
```

## Usage

Set the environment variables `SUPABASE_URL` and `SUPABASE_KEY` to your Supabase URL and key.

```bash
export SUPABASE_URL=https://your-supabase-url.com
export SUPABASE_KEY=your-supabase-key
```

Then, on your source code:

```python
from fastapi import FastAPI, Depends
from fastsupabased_acl import FastSupabasedACL

app = FastAPI()

authenticated_acl = FastSupabasedACL(role=["authenticated"])

@app.get("/test", dependencies=[Depends(authenticated_acl)]
def simple_authenticated_route():
    return {"message": "Hello, authenticated user!"}
```