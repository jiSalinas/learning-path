import os

# Define the current and total tasks for each subject
tasks = {
    "Courses": {"completed": 3, "total": 6},
    "Books": {"completed": 2, "total": 5},
    "Projects": {"completed": 1, "total": 3},
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
markdown_content = "# Learning Path Progress Tracker\n\n"
markdown_content += "| Task       | Progress  |\n|------------|-----------|\n"

for task, values in tasks.items():
    bar, percent = generate_progress_bar(values["completed"], values["total"])
    markdown_content += f"| {task} | {bar} {percent} |\n"

# Display the generated Markdown content
markdown_content

# Define the path for the ProgressStatus.md file
readme_path = "ProgressStatus.md"

# Write the generated content to the ProgressStatus.md file
with open(readme_path, "w") as f:
    f.write(markdown_content)

# Confirm that the README.md file has been updated
os.path.exists(readme_path), markdown_content

