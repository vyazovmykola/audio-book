import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Open file dialog to select a PDF
book = askopenfilename()

# Read the PDF
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# Initialize the text-to-speech engine
player = pyttsx3.init()

# Loop through all pages and read aloud
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    if text:  # Make sure there's text on the page
        player.say(text)

# Run the speech engine
player.runAndWait()
