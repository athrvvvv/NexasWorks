import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Ensure there's a very clear, plain-text mention of the business owner name in the footer
    # We will change the copyright line to explicitly state the Business Owner Name
    old_copyright = r'<p>&copy; 2026 NexasWorks\. All rights reserved\.</p>'
    new_copyright = '<p>&copy; 2026 NexasWorks. All rights reserved.</p>\n                <p class="mt-1">Business Owner Name: Atharv Prakash Chaulkar</p>'
    html = re.sub(old_copyright, new_copyright, html)
    
    with open(filepath, 'w') as f:
        f.write(html)

print("Added explicit Business Owner Name to footers.")
