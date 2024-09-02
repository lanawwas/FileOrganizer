import os
import json
from datetime import datetime
import argparse

# Define the main directory and subdirectories
main_dir = r'C:\Users\lait.abu-nawwas\Documents\Resources'

subdirs = [
    'Articles/DataScience', 'Articles/Management', 'Articles/Technology', 'Articles/Marketing',
    'Books/DataScience', 'Books/Management', 'Books/Technology',
    'Reports/Annual', 'Reports/Quarterly', 'Reports/ProjectSpecific',
    'Tutorials/R', 'Tutorials/Python', 'Tutorials/SQL',
    'Presentations', 'ResearchPapers', 'Guidelines', 'Tools', 'Templates', 'References', 'MeetingNotes', 'Miscellaneous'
]

# Create directory structure
def create_directories():
    if not os.path.exists(main_dir):
        os.makedirs(main_dir)
    for subdir in subdirs:
        path = os.path.join(main_dir, subdir)
        if not os.path.exists(path):
            os.makedirs(path)
    print("Directory structure created/verified.")

# Update the index/catalog
def update_index():
    catalog = {}
    for root, dirs, files in os.walk(main_dir):
        for file in sorted(files):  # Sort files alphabetically
             if file not in ['index.json', 'index.md']:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, main_dir)
                file_info = {
                    'title': os.path.splitext(file)[0],
                    'type': os.path.basename(root),
                    'path': relative_path,
                    'last_modified': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                }
                catalog[relative_path] = file_info

    # Write to index.json
    with open(os.path.join(main_dir, 'index.json'), 'w') as json_file:
        json.dump(catalog, json_file, indent=4)
    
    # Write to index.md
    with open(os.path.join(main_dir, 'index.md'), 'w') as md_file:
        md_file.write('# Organizational Resources Index\n\n')
        for item in sorted(catalog.values(), key=lambda x: x['title']):
            md_file.write(f"## {item['title']}\n")
            md_file.write(f"- **Type:** {item['type']}\n")
            md_file.write(f"- **Path:** {item['path']}\n")
            md_file.write(f"- **Last Modified:** {item['last_modified']}\n\n")
    
    print("Index/catalog updated.")

# Main function
def main(create_structure=True, update_catalog=True):
    if create_structure:
        create_directories()
    if update_catalog:
        update_index()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Organize organizational resources and update index/catalog.")
    parser.add_argument("--create", action="store_true", help="Create directory structure")
    parser.add_argument("--update", action="store_true", help="Update index/catalog")
    args = parser.parse_args()

    main(create_structure=args.create, update_catalog=args.update)
