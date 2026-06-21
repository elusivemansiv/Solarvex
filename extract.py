import os

pages = ['about', 'solutions', 'products', 'cases', 'community', 'support', 'login']

for page in pages:
    html_path = f'../{page}.html'
    if not os.path.exists(html_path):
        continue
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    header_end = content.find('</header>')
    if header_end != -1:
        start_idx = header_end + 9
    else:
        start_idx = content.find('<body>') + 6
        
    footer_start = content.find('<footer class="footer">')
    if footer_start == -1:
        footer_start = content.find('</body>')
        
    main_content = content[start_idx:footer_start].strip()
    
    # Fix image paths
    main_content = main_content.replace('src="images/', 'src="/images/')
    
    # Fix links
    for p in pages + ['index']:
        main_content = main_content.replace(f'href="{p}.html"', f'href="/{p if p != "index" else ""}"')
    
    vue_content = f'''<script setup>
import {{ onMounted }} from 'vue'

onMounted(() => {{
  const fadeElements = document.querySelectorAll('.fade-in')
  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.classList.add('visible')
      }}
    }})
  }}, {{ threshold: 0.1 }})
  fadeElements.forEach(el => observer.observe(el))
}})
</script>

<template>
  <main>
{main_content}
  </main>
</template>
'''
    with open(f'src/views/{page.capitalize()}.vue', 'w', encoding='utf-8') as f:
        f.write(vue_content)
