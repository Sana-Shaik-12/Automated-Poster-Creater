import pandas as pd
from google.colab import drive
from jinja2 import Environment, FileSystemLoader

# Mount Google Drive
drive.mount('/content/drive')

# Step 1: Import CSV file as DataFrame with utf-8 encoding
df = pd.read_csv('path to your csv file', encoding="utf-8")

# Replace single quotes with HTML-safe equivalent in Title and Subheader
df['Title'] = df['Title'].str.replace("'", "&#39;")
df['Subheader'] = df['Subheader'].str.replace("'", "&#39;")

# Step 2: Set up Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('path to your folder'))
template = env.get_template('path to your html file')

# Step 3: Define a function to process and save each row as HTML
def process_and_save_row(index, content):
    left_column_background = content.get('left_column_background', 'linear-gradient(to bottom, #001f3f, #003366)')
    middle_section_background = content.get('middle_section_background', '#8564a4')

    # Get the processed title and subheader
    processed_title = content.get('Title', 'Default Title')
    processed_subheader = content.get('Subheader', 'Default Subheader')

    # Debugging: Print the row data
    print(f"Processing Row {index}: {content}")

    # Render the template with the content
    rendered_html = template.render(
        content=content,
        left_column_background=left_column_background,
        middle_section_background=middle_section_background,
        processed_title=processed_title,
        processed_subheader=processed_subheader
    )

    # Save the rendered HTML to Google Drive
    output_path = f'path to your html output files.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print(f"HTML file generated successfully and saved to {output_path}.")

# Step 4: Process a specific row or all rows based on `row_index_to_process`
row_index_to_process = None  # Change to None to process all rows

if row_index_to_process is None:
    # Process all rows
    for index, row in df.iterrows():
        content = row.to_dict()
        process_and_save_row(index, content)
else:
    # Process a specific row
    if 0 <= row_index_to_process < len(df):
        row = df.iloc[row_index_to_process]
        content = row.to_dict()
        process_and_save_row(row_index_to_process, content)
    else:
        print(f"Row index {row_index_to_process} is out of range. Please provide a valid index.")
