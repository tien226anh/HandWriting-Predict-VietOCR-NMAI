from fastapi import FastAPI, UploadFile, File
import shutil
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # Import the necessary module

from process import ImageProcessor

app = FastAPI()
processor = ImageProcessor()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    # Save the uploaded file to the "static" folder
    file_location = f"static/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the uploaded image using the ImageProcessor
    result = processor.process_image(file_location)

    return {"result": result, "filename": file.filename}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
