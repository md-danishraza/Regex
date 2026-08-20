# 0. Introduction to Regex

# Regular Expressions (Regex) are patterns used to:

# Search text
# Validate input
# Extract data
# Replace text
# Parse logs
# Web scraping
# Data cleaning

import re

# re.search

import re

text = "My age is 25"

match = re.search(r"\d+", text)

print(match.group())