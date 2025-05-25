from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load marks from JSON file
with open("marks.json", "r") as f:
    student_data = json.load(f)

# Build a dictionary for quick lookup
marks_lookup = {entry["name"]: entry["marks"] for entry in student_data}

@app.get("/")
def get_marks(name: list[str] = []):
    result = [marks_lookup.get(n, None) for n in name]
    return {"marks": result}
