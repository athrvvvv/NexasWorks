import re

# Update Terms
with open('terms.html', 'r') as f:
    html = f.read()

new_content = """
            <p>Welcome to NexasWorks. By engaging with our digital web agency services, you agree to comply with and be bound by the following terms and conditions of use.</p>
            <h3 class="text-lg font-semibold text-white mt-4">1. Scope of Services</h3>
            <p>NexasWorks provides custom web design, development, and digital marketing services. The specific scope, deliverables, and timelines will be detailed in a separate project proposal or statement of work.</p>
            <h3 class="text-lg font-semibold text-white mt-4">2. Client Obligations & Usage Restrictions</h3>
            <p>The client agrees to provide all necessary assets, content, and feedback in a timely manner. Delays in providing materials may result in project timeline extensions. Furthermore, clients are strictly prohibited from using our services to host or distribute illegal, malicious, or highly objectionable content. We reserve the right to suspend services if usage restrictions are violated.</p>
            <h3 class="text-lg font-semibold text-white mt-4">3. Payment Terms & Intellectual Property</h3>
            <p>Payments are structured into milestones. All invoices must be paid within 7 days of receipt. Upon final payment, the intellectual property rights of the custom-developed website will transfer to the client, excluding any third-party tools, plugins, or pre-existing proprietary code used by NexasWorks.</p>
            <h3 class="text-lg font-semibold text-white mt-4">4. Limitation of Liability</h3>
            <p>NexasWorks shall not be liable for any indirect, special, or consequential damages arising out of the use or inability to use the delivered digital products.</p>
            <h3 class="text-lg font-semibold text-white mt-4">5. Dispute Resolution</h3>
            <p>Any disputes arising from these terms or our services shall be resolved through binding arbitration in Khopoli, Maharashtra, India, under the jurisdiction of local courts.</p>"""

html = re.sub(r'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">.*?</div>', 
              f'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">{new_content}\n            </div>', 
              html, flags=re.DOTALL)

with open('terms.html', 'w') as f:
    f.write(html)

# Update Privacy
with open('privacy.html', 'r') as f:
    html = f.read()

new_content = """
            <p>At NexasWorks, we are committed to protecting your privacy and ensuring the security of your personal data.</p>
            <h3 class="text-lg font-semibold text-white mt-4">1. Information We Collect</h3>
            <p>We may collect personal information such as your name, email address (e.g., when contacting atharvchaulkar2005@gmail.com), and business details when you request our services or communicate with us.</p>
            <h3 class="text-lg font-semibold text-white mt-4">2. How We Use & Store Your Data</h3>
            <p>Your information is used strictly to provide and improve our web development services, process payments, and communicate project updates. All collected data is securely stored on encrypted cloud servers with restricted access. We do not sell your data to third parties.</p>
            <h3 class="text-lg font-semibold text-white mt-4">3. Data Security</h3>
            <p>We implement industry-standard security measures to protect against unauthorized access, alteration, disclosure, or destruction of your personal information.</p>
            <h3 class="text-lg font-semibold text-white mt-4">4. Third-Party Services</h3>
            <p>We may employ third-party companies and individuals to facilitate our services (e.g., hosting, analytics). These third parties have access to your Personal Data only to perform these tasks on our behalf.</p>
            <h3 class="text-lg font-semibold text-white mt-4">5. Use of Cookies</h3>
            <p>Our website utilizes cookies to enhance user experience, track site performance, and remember your preferences. These small text files are stored on your device. You can manage or disable cookies through your browser settings, though some site functionalities may be limited without them.</p>"""

html = re.sub(r'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">.*?</div>', 
              f'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">{new_content}\n            </div>', 
              html, flags=re.DOTALL)

with open('privacy.html', 'w') as f:
    f.write(html)

# Update Refund
with open('refund.html', 'r') as f:
    html = f.read()

new_content = """
            <div class="bg-brand-900/30 border-l-4 border-brand-500 p-4 rounded mb-6 text-white font-medium">
                Refunds are only processed before the project commences, and no refunds are issued for completed web development milestones.
            </div>
            <p>NexasWorks strives to deliver the highest quality web solutions. Due to the custom nature of our digital services, our refund policy is strictly structured as follows:</p>
            <h3 class="text-lg font-semibold text-white mt-4">1. Project Cancellation & Procedures</h3>
            <p>To initiate a cancellation, the client must submit a formal written request via email to atharvchaulkar2005@gmail.com. If you choose to cancel your project before any actual design or development work has commenced, we will issue a full refund of any deposits paid, minus a 5% transaction processing fee.</p>
            <h3 class="text-lg font-semibold text-white mt-4">2. Milestone Completions (Non-Refundable)</h3>
            <p>Web development projects are often divided into milestones. Once a milestone has been completed and approved by the client, the payment for that milestone becomes strictly non-refundable and non-cancellable.</p>
            <h3 class="text-lg font-semibold text-white mt-4">3. Terminated Projects & Timeframes</h3>
            <p>In the event that a project is terminated midway, NexasWorks retains the right to bill for the hours worked or milestones completed up to the point of cancellation. Eligible refunds will be processed and credited back to the original payment method within 7-10 business days after the cancellation request is approved.</p>
            <h3 class="text-lg font-semibold text-white mt-4">4. Return & Replace Policy</h3>
            <p>As we provide digital services, there are no physical products to return. However, if a delivered digital milestone contains significant technical defects deviating from the agreed scope, we will replace or fix the defective code at no extra cost if reported within 14 days of delivery.</p>"""

html = re.sub(r'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">.*?</div>', 
              f'<div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-lg">{new_content}\n            </div>', 
              html, flags=re.DOTALL)

with open('refund.html', 'w') as f:
    f.write(html)

print("Updated policies successfully.")
