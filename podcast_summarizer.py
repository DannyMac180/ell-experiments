from langchain.document_loaders import ObsidianLoader
from datetime import datetime, timedelta
import ell

ell.init(store='./logdir', autocommit=True, verbose=True)

# Initialize the ObsidianLoader with the specified directory
obsidian_loader = ObsidianLoader(
    "/Users/danielmcateer/Library/Mobile Documents/iCloud~md~obsidian/Documents/Ideaverse/Readwise/Podcasts"
)

# Load the documents from the Obsidian vault
documents = obsidian_loader.load()

# Get the current date
current_date = datetime.now().date()

# Calculate the date 7 days ago
seven_days_ago = current_date - timedelta(days=7)

# Filter documents updated within the last 7 days
recent_documents = []
for doc in documents:
    if 'last_modified' in doc.metadata:
        try:
            updated_date = datetime.fromtimestamp(doc.metadata['last_modified']).date()
            if updated_date > seven_days_ago:
                recent_documents.append(doc)
        except (ValueError, TypeError):
            print(f"Invalid date format for document: {doc.metadata}")
    else:
        print(f"'last_modified' field missing for document: {doc.metadata}")

print(f"Number of documents updated in the last 7 days: {len(recent_documents)}")

@ell.simple(model="gpt-4o")
def extract_metadata_and_summarize(notes: list) -> dict:
    """
    Extract podcast metadata and summarize the notes.
    The notes are in the format of a podcast transcript with metadata at the top.
    The summaries should especially focus on the highlights and key ideas and insights.
    Return a dictionary containing the title, link, and summary.
    """
    
    # Extract metadata from the notes
    metadata = {}
    for line in notes.split('\n'):
        if line.startswith('Title:'):
            metadata['title'] = line.split(':')[1].strip()
        elif line.startswith('Source URL:'):
            metadata['source_url'] = line.split(':')[1].strip()
    
    summary = {f"Summarize the podcast notes here: {notes}"}
    
    # Your logic to extract metadata and summarize goes here
    # For now, we'll return a placeholder
    return {
        "title": metadata['title'],
        "source_url": metadata['source_url'],
        "summary": summary
    }

summaries = []

for doc in recent_documents:
    notes = doc.page_content
    result = extract_metadata_and_summarize(notes)
    summaries.append(f"Title: {result['title']}\nSource URL: {result['source_url']}\nSummary:\n{result['summary']}\n\n")

with open('summarized_podcasts.txt', 'w') as f:
    f.writelines(summaries)
    
    print("Summarized Podcasts:")
    with open('summarized_podcasts.txt', 'r') as f:
        print(f.read())
