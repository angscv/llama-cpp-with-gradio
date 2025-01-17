import os
from dotenv import load_dotenv

load_dotenv()


SYSTEM_PROMPT = os.getenv('SYSTEM_PROMPT', "Ты Сайга - дружелюбный и болтливый ассистент.")
MODEL_PATH = os.getenv('MODEL_PATH', 'weights/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf')
N_CTX = int(os.getenv('N_CTX', 8192))
TOP_K = int(os.getenv('TOP_K', 30))
TOP_P = float(os.getenv('TOP_P', 0.9))
TEMPERATURE = float(os.getenv('TEMPERATURE', 0.6))
REPEAT_PENALTY = float(os.getenv('REPEAT_PENALTY', 1.1))
N_THREADS = int(os.getenv('N_THREADS', 7))

DEFAULT_JSON = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "Shelf": {
        "type": "integer",
        "description": "The shelf where the book is located."
      },
      "Level": {
        "type": "integer",
        "description": "The level of the shelf where the book is located."
      },
      "Author": {
        "type": "string",
        "description": "The author of the book."
      },
      "Title": {
        "type": "string",
        "description": "The title of the book."
      }
    },
    "required": [
      "Shelf",
      "Level",
      "Author",
      "Title"
    ]
  },
  "required": ["items"]
}

EXAMPLES = [
    "The first book I read was written by George Orwell and was titled 1984."
    "The second book in my collection is The Master and Margarita by Mikhail Bulgakov."
    "The first shelf, first level, contains a book by Ivanov Ivan Ivanovich titled My Journey Through the Archive. The next book is by Petrov Petr Petrovich titled A New Journey Through the Archive. On the second level, there is a book by Sidorov Sidor Sidorovich titled My Journey Through the Shelves. The next book is by Vladimir Vladimirovich Vladimirov titled How These Shelves Are Driving Me Crazy. On the second shelf, first level, there is a book by Ustalov Ustal Ustalovich titled How Did I End Up Here?. The next book is by Ubegaev Ubegai Ubegaevich titled Screw This, Put It Over There."
]
