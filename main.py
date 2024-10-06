from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Initialize the FastAPI app
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# List of words
words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Function to return words containing the given character
def words_with_char(char, words_list):
    # Ensure the input is a single character
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    
    # Find and return words containing the character
    result = [word for word in words_list if char in word]
    return result

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "words": []})

@app.post("/search")
async def search_words(request: Request):
    form = await request.form()
    char = form.get("char")
    words_containing_char = words_with_char(char, words_list)
    return templates.TemplateResponse("index.html", {"request": request, "words": words_containing_char})
