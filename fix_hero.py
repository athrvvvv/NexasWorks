import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace Hero section HTML
old_hero = """            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
                <h1 class="text-5xl md:text-7xl font-extrabold text-white tracking-tight mb-8">
                    Crafting Digital <br/> <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-600">Masterpieces</span>
                </h1>
                <p class="mt-4 text-xl md:text-2xl text-slate-400 max-w-3xl mx-auto mb-10">
                    NexasWorks is your premier agency for stunning, high-performance web solutions. We transform ideas into impactful digital realities.
                </p>
                <div class="flex flex-col sm:flex-row justify-center gap-4">"""

new_hero = """            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
                <h1 class="reveal text-5xl md:text-7xl font-extrabold text-white tracking-tight mb-8">
                    Crafting Digital <br/> <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-600">Masterpieces</span>
                </h1>
                <p class="reveal reveal-delay-1 mt-4 text-xl md:text-2xl text-slate-400 max-w-3xl mx-auto mb-10">
                    NexasWorks is your premier agency for stunning, high-performance web solutions. We transform ideas into impactful digital realities.
                </p>
                <div class="reveal reveal-delay-2 flex flex-col sm:flex-row justify-center gap-4">"""

content = content.replace(old_hero, new_hero)

# Replace JS logic
old_js = """            // Elements to animate
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
            });"""

new_js = """            // Automatically add reveal classes to other main elements
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
            document.querySelectorAll('.reveal').forEach(el => observer.observe(el));"""

content = content.replace(old_js, new_js)

with open('index.html', 'w') as f:
    f.write(content)

print("Hero patch applied")
