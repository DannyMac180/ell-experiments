from langchain.document_loaders import ObsidianLoader
from datetime import datetime, timedelta

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
print(recent_documents[0].page_content)
