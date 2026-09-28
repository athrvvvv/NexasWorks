import re
import os

with open('index.html', 'r') as f:
    html = f.read()

# Extract header and footer
header_match = re.search(r'(<header.*?</header>)', html, re.DOTALL)
header = header_match.group(1)

footer_match = re.search(r'(<footer.*?</footer>)', html, re.DOTALL)
footer = footer_match.group(1)

# Extract modals
def get_modal_content(modal_id):
    pattern = rf'<dialog id="{modal_id}".*?</dialog>'
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        return "", ""
    modal_html = match.group(0)
    title = re.search(r'<h2.*?>(.*?)</h2>', modal_html, re.DOTALL).group(1)
    divs = re.findall(r'<div class="p-6[^>]*>(.*?)</div>', modal_html, re.DOTALL)
    content = divs[1] if len(divs) >= 2 else ""
    return title, content

pages = {
    'contact.html': 'contact-modal',
    'terms.html': 'terms-modal',
    'privacy.html': 'privacy-modal',
    'refund.html': 'refund-modal'
}

base_layout = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__ - NexasWorks</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: { 50: '#f0f9ff', 100: '#e0f2fe', 400: '#38bdf8', 500: '#0ea5e9', 600: '#0284c7', 900: '#0c4a6e' },
                        dark: { bg: '#020617', card: '#0f172a', border: '#1e293b' }
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-dark-bg text-slate-300 font-sans antialiased flex flex-col min-h-screen selection:bg-brand-500 selection:text-white">
    __HEADER__
    
    <main class="flex-grow pt-32 pb-24">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-4xl font-bold text-white mb-8 border-b border-dark-border pb-4">__TITLE__</h1>
            <div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">
                __CONTENT__
            </div>
        </div>
    </main>

    __FOOTER__
</body>
</html>
"""

# Modify footer links in the base html
new_footer = footer
new_footer = re.sub(r'<button onclick="document.getElementById\(\'contact-modal\'\)\.showModal\(\)".*?>Contact Us</button>', r'<a href="contact.html" class="text-slate-400 hover:text-brand-400 transition-colors">Contact Us</a>', new_footer)
new_footer = re.sub(r'<button onclick="document.getElementById\(\'terms-modal\'\)\.showModal\(\)".*?>Terms & Conditions</button>', r'<a href="terms.html" class="text-slate-400 hover:text-brand-400 transition-colors">Terms & Conditions</a>', new_footer)
new_footer = re.sub(r'<button onclick="document.getElementById\(\'privacy-modal\'\)\.showModal\(\)".*?>Privacy Policy</button>', r'<a href="privacy.html" class="text-slate-400 hover:text-brand-400 transition-colors">Privacy Policy</a>', new_footer)
new_footer = re.sub(r'<button onclick="document.getElementById\(\'refund-modal\'\)\.showModal\(\)".*?>Refund & Cancellation Policy</button>', r'<a href="refund.html" class="text-slate-400 hover:text-brand-400 transition-colors">Refund & Cancellation Policy</a>', new_footer)

# Header modification
new_header = header
new_header = re.sub(r'<button onclick="document.getElementById\(\'contact-modal\'\)\.showModal\(\)".*?>Contact</button>', r'<a href="contact.html" class="text-slate-300 hover:text-white transition-colors">Contact</a>', new_header)
new_header = re.sub(r'<button onclick="document.getElementById\(\'contact-modal\'\)\.showModal\(\)".*?>Get Started</button>', r'<a href="contact.html" class="bg-brand-500 hover:bg-brand-600 text-white px-6 py-2.5 rounded-full font-medium transition-all shadow-lg shadow-brand-500/30">Get Started</a>', new_header)

# Ensure header logo links back to index
new_header = re.sub(r'<a href="#" class="text-3xl', r'<a href="index.html" class="text-3xl', new_header)

for filename, modal_id in pages.items():
    title, content = get_modal_content(modal_id)
    page_html = base_layout.replace('__TITLE__', title).replace('__CONTENT__', content).replace('__HEADER__', new_header).replace('__FOOTER__', new_footer)
    with open(filename, 'w') as f:
        f.write(page_html)

# Update index.html
html = html.replace(footer, new_footer)
html = html.replace(header, new_header)

# Replace other contact buttons in index
html = re.sub(r'<button onclick="document.getElementById\(\'contact-modal\'\)\.showModal\(\)" class="([^"]*)">Book a Consultation</button>', r'<a href="contact.html" class="\1">Book a Consultation</a>', html)
html = re.sub(r'<button onclick="document.getElementById\(\'contact-modal\'\)\.showModal\(\)" class="([^"]*)">Select Package</button>', r'<a href="contact.html" class="\1">Select Package</a>', html)
html = re.sub(r'<button onclick="document.getElementById\(\'contact-modal\'\)\.showModal\(\)" class="([^"]*)">Start Your Project Today</button>', r'<a href="contact.html" class="\1">Start Your Project Today</a>', html)

# Fix Logo link in index
html = re.sub(r'<a href="#" class="text-3xl', r'<a href="index.html" class="text-3xl', html)

# Remove all modals entirely from index.html
html = re.sub(r'<!-- Modals -->.*?</dialog>', '', html, flags=re.DOTALL)
html = re.sub(r'<dialog.*?</dialog>', '', html, flags=re.DOTALL)
html = re.sub(r'// Fallback for browsers without closedby support.*?}\n', '', html, flags=re.DOTALL)
html = re.sub(r'<!-- Contact Us Modal -->.*?</dialog>', '', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("Split pages successfully.")
