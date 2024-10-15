from llama_index.readers.obsidian import ObsidianReader
from pprint import pprint

# Initialize the ObsidianReader with the specified directory
obsidian_reader = ObsidianReader(
    "/Users/danielmcateer/Library/Mobile Documents/iCloud~md~obsidian/Documents/Ideaverse/Readwise/Podcasts"
)

# Load the documents from the Obsidian vault
documents = obsidian_reader.load_data()

# Get the first document (if available)
if documents:
    doc = documents[4]
    
    print(doc.text)
else:
    print("No documents found in the specified Obsidian vault.")
