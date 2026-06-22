<script setup>
import { onMounted, inject } from 'vue'

const { openAuthModal } = inject('authModalControl')

window.openLogin = function() {
  openAuthModal();
}

onMounted(() => {
  const fadeElements = document.querySelectorAll('.fade-in')
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible')
      }
    })
  }, { threshold: 0.1 })
  fadeElements.forEach(el => observer.observe(el))
})
</script>

<template>
  <main>
<!-- Hero -->
  <!-- Hero -->
  <section class="inner-hero">
    <div class="inner-hero-bg" style="background: url('/images/hero-bg.jpg') center/cover no-repeat;"></div>
    <div class="inner-hero-overlay"></div>
    <div class="inner-hero-content">
      <h1 class="inner-hero-title">Solar Vex Community</h1>
      <p class="inner-hero-desc">Connect with solar installers, exchange DIY ideas, get direct expert Q&A, and read technical articles.</p>
    </div>
  </section>

  <!-- Community Section -->
  <section class="section-padding">
    <div class="community-layout">
      <!-- Forums Left Column -->
      <div class="forums-list fade-in">
        <h3 style="font-size: 20px; color: var(--dark-blue); margin-bottom: 20px; font-weight: 800; text-transform: uppercase;">Discussion Forums</h3>
        
        <!-- Forum Cat 1 -->
        <div class="forum-category-card">
          <div class="forum-cat-info">
            <h4><a href="#" style="text-decoration: none; color: inherit; font-weight: 700;">Installers Corner</a></h4>
            <p>Wiring standards, grounding requirements, local inverter permits, and utility approvals.</p>
          </div>
          <div class="forum-cat-stats">
            <div class="forum-stat">
              <div class="forum-stat-num">1.4k</div>
              <div class="forum-stat-lbl">Topics</div>
            </div>
            <div class="forum-stat">
              <div class="forum-stat-num">12k</div>
              <div class="forum-stat-lbl">Posts</div>
            </div>
          </div>
        </div>

        <!-- Forum Cat 2 -->
        <div class="forum-category-card">
          <div class="forum-cat-info">
            <h4><a href="#" style="text-decoration: none; color: inherit; font-weight: 700;">Storage & Battery Systems</a></h4>
            <p>Tips on configuring modular lithium battery storage, managing battery cycles, and backup gateway wiring.</p>
          </div>
          <div class="forum-cat-stats">
            <div class="forum-stat">
              <div class="forum-stat-num">980</div>
              <div class="forum-stat-lbl">Topics</div>
            </div>
            <div class="forum-stat">
              <div class="forum-stat-num">8.4k</div>
              <div class="forum-stat-lbl">Posts</div>
            </div>
          </div>
        </div>

        <!-- Forum Cat 3 -->
        <div class="forum-category-card">
          <div class="forum-cat-info">
            <h4><a href="#" style="text-decoration: none; color: inherit; font-weight: 700;">GroHome Automation & Smart Plugs</a></h4>
            <p>Smart load balancing, EV Charger solar matching mode configs, and smart home IoT automation logs.</p>
          </div>
          <div class="forum-cat-stats">
            <div class="forum-stat">
              <div class="forum-stat-num">520</div>
              <div class="forum-stat-lbl">Topics</div>
            </div>
            <div class="forum-stat">
              <div class="forum-stat-num">3.9k</div>
              <div class="forum-stat-lbl">Posts</div>
            </div>
          </div>
        </div>

        <!-- Forum Cat 4 -->
        <div class="forum-category-card">
          <div class="forum-cat-info">
            <h4><a href="#" style="text-decoration: none; color: inherit; font-weight: 700;">DIY Solar Projects</a></h4>
            <p>Share your off-grid setups, custom RV builds, and balcony solar installations with other DIY creators.</p>
          </div>
          <div class="forum-cat-stats">
            <div class="forum-stat">
              <div class="forum-stat-num">2.1k</div>
              <div class="forum-stat-lbl">Topics</div>
            </div>
            <div class="forum-stat">
              <div class="forum-stat-num">18.5k</div>
              <div class="forum-stat-lbl">Posts</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column Sidebar Widgets -->
      <div class="community-sidebar fade-in">
        <!-- Join Community Card -->
        <div class="sidebar-widget" style="background: linear-gradient(135deg, var(--dark-blue) 0%, #0d1e30 100%); color: white; border: none;">
          <h4 style="color: white; border-color: rgba(255,255,255,0.1);">Join Our Network</h4>
          <p style="font-size: 13px; color: rgba(255,255,255,0.8); margin-bottom: 20px; line-height: 1.5;">Access manuals, post queries on support threads, track certifications, and connect with global installers.</p>
          <button class="btn-solid" onclick="openLogin()" style="width: 100%; text-align: center; border: none;">Sign Up / Login</button>
        </div>

        <!-- Blog Posts Widget -->
        <div class="sidebar-widget">
          <h4>Latest Tech Blog</h4>
          <ul class="community-sidebar-list">
            <li class="community-sidebar-item">
              <img src="/images/energy-storage.jpg" alt="Battery System">
              <div class="community-sidebar-item-info">
                <h5><a href="#" style="text-decoration: none; color: inherit;" onclick="alert('Navigating to full article...')">Understanding Lithium Storage Cycles</a></h5>
                <span>June 08, 2026 &bull; 5 min read</span>
              </div>
            </li>
            <li class="community-sidebar-item">
              <img src="/images/ev-charger.jpg" alt="EV Charger charging">
              <div class="community-sidebar-item-info">
                <h5><a href="#" style="text-decoration: none; color: inherit;" onclick="alert('Navigating to full article...')">Configuring Smart EV Solar Charging</a></h5>
                <span>May 25, 2026 &bull; 8 min read</span>
              </div>
            </li>
            <li class="community-sidebar-item">
              <img src="/images/smart-energy.jpg" alt="Smart Home Control Screen">
              <div class="community-sidebar-item-info">
                <h5><a href="#" style="text-decoration: none; color: inherit;" onclick="alert('Navigating to full article...')">GroHome Load Balancing Guidelines</a></h5>
                <span>May 14, 2026 &bull; 6 min read</span>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>





<!-- Footer -->
  </main>
</template>
