import nbformat
from nbformat import v4 as nbf
# Create a new Jupyter notebook
nb = nbf.new_notebook()
# Define the notebook cells
cells = [
    nbf.new_markdown_cell("# :wrench: Data Pipeline Debug Notebook\n"
                          "This notebook demonstrates a failing data pipeline transformation. "
                          "The goal is to debug it using a sandboxed Jupyter server and the in-page Python CLI."),
    nbf.new_code_cell("# Step 1: Import pipeline function\n"
                      "from pipeline import transform_pipeline\n"
                      "import pandas as pd"),
    nbf.new_code_cell("# Step 2: Create input DataFrame\n"
                      "df_input = pd.DataFrame([\n"
                      "    {'id': 1, 'name': 'Alice', 'date': '15/08/2022'},\n"
                      "    {'id': 2, 'name': 'Bob', 'date': '32/01/2023'},  # Invalid date\n"
                      "    {'id': 3, 'name': 'Charlie', 'date': '12/12/2021'}\n"
                      "])\n"
                      "df_input"),
    nbf.new_code_cell("# Step 3: Run the transformation pipeline\n"
                      "# This will fail due to an invalid date format\n"
                      "df_transformed = transform_pipeline(df_input)\n"
                      "df_transformed"),
    nbf.new_markdown_cell("## :x: Issue: ValueError Expected\n"
                          "`32/01/2023` is not a valid date. Your task is to:\n"
                          "- Connect to the sandboxed Jupyter environment\n"
                          "- Open `pipeline.py`\n"
                          "- Fix the `clean_dates()` function to handle invalid dates\n"
                          "- Save and re-run the notebook to confirm the fix."),
    nbf.new_markdown_cell("## :white_check_mark: Follow-up: Use the in-page Python CLI\n"
                          "Once the fix is made, use the embedded Python CLI to test stateful interactions:\n"
                          "```python\n"
                          "from pipeline import clean_dates\n"
                          "sample = {'date': '32/01/2023'}\n"
                          "clean_dates(sample)\n"
                          "\n"
                          "# Redefine function to handle errors\n"
                          "def clean_dates(entry):\n"
                          "    from datetime import datetime\n"
                          "    try:\n"
                          "        entry['date'] = datetime.strptime(entry['date'], '%d/%m/%Y').date()\n"
                          "    except Exception:\n"
                          "        entry['date'] = None\n"
                          "    return entry\n"
                          "\n"
                          "clean_dates(sample)\n"
                          "```")
]
# Add cells to the notebook
nb['cells'] = cells
# Save it to a file
with open("demo_debug_pipeline.ipynb", "w") as f:
    nbformat.write(nb, f)