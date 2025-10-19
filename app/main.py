from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

# Start FastAPI
app = FastAPI()




# Scalar API DOCS
@app.get("/scalar", include_in_schema=False)
async def get_scalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="API DOCs")
