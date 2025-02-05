import os

# Define the current and total tasks for each subject
tasks = {
    "Courses": {"completed": 0, "total": 1},
    "Books": {"completed": 0, "total": 1},
    "Projects": {"completed": 0, "total": 3},
}

# Function to generate a progress bar
def generate_progress_bar(current, total):
    if total == 0:
        return "No tasks defined", "0%"
    percentage = (current / total) * 100
    completed = int(percentage // 10)  # Number of filled blocks
    remaining = 10 - completed         # Number of empty blocks
    progress_bar = "█" * completed + "░" * remaining
    return progress_bar, f"{percentage:.0f}%"

# Generate Markdown content for the README
markdown_content = "# My Learning Journey\n\n"
markdown_content += "This repository is my personal learning path of Git, where I track courses, books, and resources I am currently using.\n\n"
markdown_content += "## Objectives\n\n"
markdown_content += "\t- Learn Git\n\n"
markdown_content += "## Timeline\n\n"
markdown_content += "\t- Complete Youtube course Learn Git - The Full Course <span style='color:red'>*09/01/2025*</span>.\n\n"
markdown_content += "\t- Read Pro Git <span style='color:red'>*01/03/2025*</span>.\n\n"
markdown_content += "### Current Status\n\n"
markdown_content += "\t- **Courses:** 0/1 completed\n\n"
markdown_content += "\t- **Books:** 0/1 read\n\n"
markdown_content += "\t- **Projects:** 0/1 completed\n\n"
markdown_content += "# Detailed Progress\n\n"
markdown_content += "| Task       | Progress  |\n|------------|-----------|\n"

for task, values in tasks.items():
    bar, percent = generate_progress_bar(values["completed"], values["total"])
    markdown_content += f"| {task} | {bar} {percent} |\n"

# Display the generated Markdown content
markdown_content

# Define the path for the ProgressStatus.md file
readme_path = "git/README.md"

# Write the generated content to the ProgressStatus.md file
with open(readme_path, "w") as f:
    f.write(markdown_content)

# Confirm that the README.md file has been updated
os.path.exists(readme_path), markdown_content

