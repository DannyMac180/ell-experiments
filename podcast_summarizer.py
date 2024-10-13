from llama_index.readers.obsidian import ObsidianReader
from datetime import datetime, timedelta

# Initialize the ObsidianReader with the specified directory
obsidian_reader = ObsidianReader(
    "/Users/danielmcateer/Library/Mobile Documents/iCloud~md~obsidian/Documents/Ideaverse/Readwise/Podcasts"
)

# Load the documents from the Obsidian vault
documents = obsidian_reader.load_data()
# Print the metadata of the loaded Obsidian documents
print("Metadata of loaded Obsidian documents:")
for i, doc in enumerate(documents, 1):
    print(f"\nDocument {i}:")
    for key, value in doc.metadata.items():
        print(f"  {key}: {value}")


# Get the current date
current_date = datetime.now().date()

# Calculate the date 7 days ago
seven_days_ago = current_date - timedelta(days=7)

# Filter documents updated within the last 7 days
recent_documents = []
for doc in documents:
    if 'Updated' in doc.metadata:
        try:
            updated_date = datetime.strptime(doc.metadata['Updated'], '%Y-%m-%d').date()
            if updated_date > seven_days_ago:
                recent_documents.append(doc)
        except ValueError:
            print(f"Invalid date format for document: {doc.metadata}")
    else:
        print(f"'Updated' field missing for document: {doc.metadata}")

print(f"Number of documents updated in the last 7 days: {len(recent_documents)}")
