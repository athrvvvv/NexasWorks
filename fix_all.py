import glob
import re

good_footer = """    <footer class="bg-dark-bg border-t border-dark-border pt-16 pb-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
                <div>
                    <a href="index.html" class="text-3xl font-extrabold text-white tracking-tight block mb-4">Nexas<span class="text-brand-400">Works</span></a>
                    <p class="text-slate-400 mb-6">Your dedicated partner in architecting robust, scalable, and beautiful web experiences.</p>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="index.html#services" class="text-slate-400 hover:text-brand-400 transition-colors">Services & Pricing</a></li>
                        <li><a href="contact.html" class="text-slate-400 hover:text-brand-400 transition-colors">Contact Us</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-4">Legal Policies</h4>
                    <ul class="space-y-2">
                        <li><a href="terms.html" class="text-slate-400 hover:text-brand-400 transition-colors">Terms & Conditions</a></li>
                        <li><a href="privacy.html" class="text-slate-400 hover:text-brand-400 transition-colors">Privacy Policy</a></li>
                        <li><a href="refund.html" class="text-slate-400 hover:text-brand-400 transition-colors">Refund & Cancellation Policy</a></li>
                        <li><a href="shipping.html" class="text-slate-400 hover:text-brand-400 transition-colors">Shipping & Delivery Policy</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-dark-border pt-8 flex flex-col md:flex-row justify-between items-center text-slate-500 text-sm">
                <p>&copy; 2026 NexasWorks. All rights reserved.</p>
                <p class="mt-2 md:mt-0">Khopoli, Maharashtra, India</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

contact_content = """            <p>Get in touch with NexasWorks to discuss your next big project. Our team is ready to assist you.</p>
            
            <div class="flex items-center mt-6">
                <div class="bg-brand-900/50 p-3 rounded-full mr-4 text-brand-400 border border-brand-900">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                </div>
                <div>
                    <p class="text-sm text-slate-400">Email us at</p>
                    <a href="mailto:atharvchaulkar2005@gmail.com" class="text-white font-medium hover:text-brand-400 transition-colors">atharvchaulkar2005@gmail.com</a>
                </div>
            </div>
            
            <div class="flex items-center mt-6">
                <div class="bg-brand-900/50 p-3 rounded-full mr-4 text-brand-400 border border-brand-900">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                </div>
                <div>
                    <p class="text-sm text-slate-400">Call us directly (Required for KYC)</p>
                    <a href="tel:+919999999999" class="text-white font-medium hover:text-brand-400 transition-colors">+91 99999 99999</a>
                </div>
            </div>

            <div class="flex items-center mt-6">
                <div class="bg-brand-900/50 p-3 rounded-full mr-4 text-brand-400 border border-brand-900">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                </div>
                <div>
                    <p class="text-sm text-slate-400">Headquarters</p>
                    <p class="text-white font-medium">Khopoli, Maharashtra, India</p>
                </div>
            </div>"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        html = f.read()
    
    # Fix the footer for all files
    html = re.sub(r'<footer.*?</html>', good_footer, html, flags=re.DOTALL)

    # Specific fix for contact.html content
    if filepath == 'contact.html':
        html = re.sub(r'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">.*?</main>', 
                      f'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">{contact_content}\n            </div>\n        </div>\n    </main>', 
                      html, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(html)

print("Fixed all files")
