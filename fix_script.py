with open('index.html', 'r') as f:
    content = f.read()

# We know the duplicate starts at line 32. We can find the exact text and replace the first occurrence.
bad_text = """
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
            
            // Elements to animate
            const selectors = [
                'h1', '.max-w-7xl > p', '.max-w-3xl', 
                '#work .group', '.bg-dark-card', '.text-center'
            ];
            
            document.querySelectorAll(selectors.join(', ')).forEach((el, index) => {
                // Avoid animating modals
                if(el.tagName === 'DIALOG' || el.closest('dialog')) return;
                
                el.classList.add('reveal');
                if (index % 3 === 1) el.classList.add('reveal-delay-1');
                if (index % 3 === 2) el.classList.add('reveal-delay-2');
                observer.observe(el);
            });
        });"""

# Remove the first occurrence only
content = content.replace(bad_text, "", 1)

with open('index.html', 'w') as f:
    f.write(content)

