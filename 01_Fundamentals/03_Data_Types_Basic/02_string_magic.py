"""
Problem: Demonstrate multiline strings, f-strings, and basic escape characters.
"""

# Multiline String (good for descriptions or SQL queries later)
bio = """
Hello, I am a Software Engineering student.
I am learning Python to build strong logic.
"""

# Using escape characters (\n for new line, \t for tab)
repo_path = "Folder:\n\t01_Fundamentals\n\t\t03_Data_Types_Basic"

# f-strings for dynamic formatting
username = "web_coder_essa"
platform = "Fiverr"
profile_link = f"Freelancer {username} works on {platform}."

print(bio)
print("-" * 20)
print(repo_path)
print("-" * 20)
print(profile_link)
print(f"Length of profile text: {len(profile_link)} characters")