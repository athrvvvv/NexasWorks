with open('index.html', 'r') as f:
    html = f.read()

js_code = """
    <script>
        // Scroll Reveal Animations
        document.addEventListener("DOMContentLoaded", () => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.15, rootMargin: "0px 0px -50px 0px" });
            
            // Automatically add reveal classes to other main elements
            const selectors = [
                '#work .text-center', '#work .group',
                '#services .text-center', '#services .group',
                '.bg-brand-900 .max-w-4xl'
            ];
            
            document.querySelectorAll(selectors.join(', ')).forEach((el, index) => {
                if(el.tagName === 'DIALOG' || el.closest('dialog')) return;
                if (!el.classList.contains('reveal')) {
                    el.classList.add('reveal');
                    // Stagger grids
                    if (el.closest('.grid')) {
                        let i = Array.from(el.parentNode.children).indexOf(el);
                        if (i % 3 === 1) el.classList.add('reveal-delay-1');
                        if (i % 3 === 2) el.classList.add('reveal-delay-2');
                    }
                }
            });

            // Make sure Hero triggers on load even if observer is slightly delayed
            setTimeout(() => {
                document.querySelectorAll('.reveal').forEach(el => {
                    const rect = el.getBoundingClientRect();
                    if(rect.top < window.innerHeight) el.classList.add('active');
                });
            }, 50);

            // Observe all elements with .reveal
            document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
        });
    </script>
</body>"""

html = html.replace('</body>', js_code)

with open('index.html', 'w') as f:
    f.write(html)
