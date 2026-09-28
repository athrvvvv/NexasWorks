import re

with open('index.html', 'r') as f:
    content = f.read()

# Add CSS
css_addition = """
        /* Smooth Scroll Reveal Animations */
        html { scroll-behavior: smooth; }
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s cubic-bezier(0.5, 0, 0, 1);
        }
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
        .reveal-delay-1 { transition-delay: 100ms; }
        .reveal-delay-2 { transition-delay: 200ms; }
        .reveal-delay-3 { transition-delay: 300ms; }
    </style>
"""
content = content.replace('    </style>', css_addition)

# Add JS
js_addition = """
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
        });
    </script>
"""
content = content.replace('    </script>', js_addition)

with open('index.html', 'w') as f:
    f.write(content)

print("Patch applied successfully.")
