<script setup>
import { onMounted, inject } from 'vue'

const { openModal } = inject('modalControl')

const solutionData = {
  pv: {
    title: "Residential & Commercial PV System",
    subtitle: "SOLAR VEX ENERGY GENERATION",
    image: "/images/pv-system.jpg",
    description: "Generate clean, renewable electricity directly from sunlight to power your home or business. Our high-efficiency string and microinverter setups ensure maximum energy yield even in partial shade, dramatically lowering electricity bills.",
    specs: [
      "3kW to 250kW Scalable Power Capacity",
      "98.6% Maximum Inverter Efficiency",
      "Robust IP66 Weatherproof Enclosures",
      "Real-time Cloud Monitoring & AFCI Fire Prevention"
    ]
  },
  storage: {
    title: "Battery Energy Storage System",
    subtitle: "SOLAR VEX ENERGY STORAGE",
    image: "/images/energy-storage.jpg",
    description: "Maximize energy independence by storing excess solar power generated during peak sunlight hours. Power your home or facility during the night, off-peak times, or during grid disruptions with our modular, smart lithium storage packs.",
    specs: [
      "5kWh to 30kWh Modular Expandability",
      "<10ms Seamless UPS-level Backup Switch",
      "Ultra-safe Cobalt-free LiFePO4 Chemistry",
      "Smart Application-Based Control & 10-Year Warranty"
    ]
  },
  ev: {
    title: "Smart EV Charger System",
    subtitle: "SOLAR VEX SMART TRANSPORTATION",
    image: "/images/ev-charger.jpg",
    description: "Charge your electric vehicle using clean solar energy directly from your system. Equipped with smart scheduling, dynamic load balancing to protect household appliances, and solar-only green charging modes.",
    specs: [
      "7kW Single-Phase to 22kW Three-Phase Power",
      "Solar-Only Echo Charging Mode",
      "Dynamic Home Load Balancing Protection",
      "RFID Access & Remote Mobile App Controls"
    ]
  },
  smart: {
    title: "Smart Energy Management",
    subtitle: "SOLAR VEX DIGITAL ENERGY ECOSYSTEM",
    image: "/images/smart-energy.jpg",
    description: "Take absolute charge of your entire energy infrastructure. Our unified IoT ecosystem intelligently directs, monitors, and optimizes energy flow between your solar panels, home batteries, EV charger, and household loads in real time.",
    specs: [
      "AI-Driven Real-time Energy Flow Optimization",
      "Seamless iOS & Android Mobile Dashboard",
      "Automatic Shift of High-Load Appliances to Solar Hours",
      "Integrated Grid-Export Limits & Cost Analysis"
    ]
  }
}

const showSubscribe = () => {
  alert('Thank you for your interest! Newsletter subscription coming soon.')
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

  const counters = document.querySelectorAll('.stat-num')
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.dataset.target)
        let current = 0
        const increment = target / 60
        const timer = setInterval(() => {
          current += increment
          if (current >= target) {
            entry.target.textContent = target + (target === 6 ? 'M+' : '+')
            clearInterval(timer)
          } else {
            entry.target.textContent = Math.floor(current) + (target === 6 ? 'M+' : '+')
          }
        }, 30)
        counterObserver.unobserve(entry.target)
      }
    })
  }, { threshold: 0.5 })

  counters.forEach(counter => counterObserver.observe(counter))
})
</script>

<template>
  <main>
    <!-- Hero -->
    <section class="hero">
      <div class="hero-bg"></div>
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="hero-tag">Innovative Technology</div>
        <h1 class="hero-title">
          <span>FUTURE PROOF</span>
          <span>BATTERY READY PV SOLUTION</span>
        </h1>
        <p class="hero-desc">Empowering homes and businesses with cutting-edge solar technology. Our battery-ready inverters ensure you're prepared for tomorrow's energy needs.</p>
        <a href="#solutions" class="hero-btn">
          Explore Solutions
          <i class="fas fa-arrow-right"></i>
        </a>
      </div>
      <div class="hero-products">
        <div class="product-card">
          <div class="product-icon"><i class="fas fa-bolt"></i></div>
          <div class="product-info">
            <h4>Solar Inverter X1</h4>
            <p>3-6kW Single Phase</p>
          </div>
        </div>
        <div class="product-card">
          <div class="product-icon"><i class="fas fa-battery-full"></i></div>
          <div class="product-info">
            <h4>Battery Storage</h4>
            <p>5-20kWh Capacity</p>
          </div>
        </div>
        <div class="product-card">
          <div class="product-icon"><i class="fas fa-charging-station"></i></div>
          <div class="product-info">
            <h4>EV Charger Pro</h4>
            <p>7-22kW Smart Charging</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Solutions -->
    <section class="solutions" id="solutions">
      <div class="section-title fade-in">
        <h2>Solutions</h2>
      </div>
      <div class="solutions-grid">
        <div class="solution-card fade-in" @click="openModal(solutionData.pv)">
          <img src="/images/pv-system.jpg" alt="PV System">
          <div class="solution-overlay">
            <div class="solution-num">01</div>
            <div class="solution-name">PV SYSTEM</div>
          </div>
          <div class="solution-arrow"><i class="fas fa-arrow-right"></i></div>
        </div>
        <div class="solution-card fade-in" @click="openModal(solutionData.storage)">
          <img src="/images/energy-storage.jpg" alt="Energy Storage">
          <div class="solution-overlay">
            <div class="solution-num">02</div>
            <div class="solution-name">ENERGY STORAGE</div>
          </div>
          <div class="solution-arrow"><i class="fas fa-arrow-right"></i></div>
        </div>
        <div class="solution-card fade-in" @click="openModal(solutionData.ev)">
          <img src="/images/ev-charger.jpg" alt="EV Charger">
          <div class="solution-overlay">
            <div class="solution-num">03</div>
            <div class="solution-name">EV CHARGER</div>
          </div>
          <div class="solution-arrow"><i class="fas fa-arrow-right"></i></div>
        </div>
        <div class="solution-card fade-in" @click="openModal(solutionData.smart)">
          <img src="/images/smart-energy.jpg" alt="Smart Energy Management">
          <div class="solution-overlay">
            <div class="solution-num">04</div>
            <div class="solution-name">SMART ENERGY MANAGEMENT</div>
          </div>
          <div class="solution-arrow"><i class="fas fa-arrow-right"></i></div>
        </div>
      </div>
    </section>

    <!-- Support -->
    <section class="support" id="support">
      <div class="support-inner">
        <div class="section-title fade-in">
          <h2>Support</h2>
        </div>
        <div class="support-grid">
          <div class="support-item fade-in">
            <div class="support-icon"><i class="fas fa-graduation-cap"></i></div>
            <h3>Training</h3>
            <p>Training sessions for installers, EPCs and distributors</p>
          </div>
          <div class="support-item fade-in">
            <div class="support-icon"><i class="fas fa-shield-alt"></i></div>
            <h3>Warranty</h3>
            <p>Check and claim your product warranty</p>
          </div>
          <div class="support-item fade-in">
            <div class="support-icon"><i class="fas fa-question-circle"></i></div>
            <h3>FAQ</h3>
            <p>Find troubleshooting tips for common problems</p>
          </div>
          <div class="support-item fade-in">
            <div class="support-icon"><i class="fas fa-download"></i></div>
            <h3>Download</h3>
            <p>Download helpful resources for your Solar Vex products</p>
          </div>
          <div class="support-item fade-in">
            <div class="support-icon"><i class="fas fa-solar-panel"></i></div>
            <h3>ShineDesign</h3>
            <p>A modern design tool to build your PV systems</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Global Stats -->
    <section class="global-stats">
      <div class="global-stats-bg"></div>
      <div class="global-stats-overlay"></div>
      <div class="global-stats-inner">
        <h2 class="fade-in">Global Leading Distributed Energy Solution Provider</h2>
        <p class="global-stats-sub fade-in">Solar Vex Global Footprint</p>
        <div class="stats-grid">
          <div class="stat-item fade-in">
            <div class="stat-icon"><i class="fas fa-globe-americas"></i></div>
            <div class="stat-num" data-target="180">0</div>
            <div class="stat-label">Countries with systems installed</div>
          </div>
          <div class="stat-item fade-in">
            <div class="stat-icon"><i class="fas fa-users"></i></div>
            <div class="stat-num" data-target="6">0</div>
            <div class="stat-label">Million+ End users connected to cloud platform</div>
          </div>
          <div class="stat-item fade-in">
            <div class="stat-icon"><i class="fas fa-building"></i></div>
            <div class="stat-num" data-target="63">0</div>
            <div class="stat-label">Representative sites worldwide</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Media -->
    <section class="media" id="cases">
      <div class="media-header fade-in">
        <h2>Media</h2>
        <a href="#" class="media-more">More <i class="fas fa-arrow-right"></i></a>
      </div>
      <div class="media-grid">
        <div class="media-featured fade-in">
          <img src="/images/solar-farm.jpg" alt="Solar Farm">
          <div class="media-featured-content">
            <div class="media-date">May 06, 2026</div>
            <h3>Guidelines - Identifying unofficial Channel Products</h3>
          </div>
        </div>
        <div class="media-list">
          <div class="media-item fade-in">
            <div class="media-date">May 06, 2026</div>
            <h3>Guidelines - Identifying unofficial Channel Products</h3>
          </div>
          <div class="media-item fade-in">
            <div class="media-date">Apr 22, 2026</div>
            <h3>How Solar + Storage Increases PV Self-Consumption and Maximizes ROI</h3>
          </div>
          <div class="media-item fade-in">
            <div class="media-date">Mar 30, 2026</div>
            <h3>Solar Vex Wraps Up a Strong March Exhibition Season Across Europe, Japan, and Africa, with More Global Events Ahead</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- Newsletter -->
    <section class="newsletter">
      <div class="newsletter-inner fade-in">
        <h3><i class="fas fa-envelope-open-text"></i> SUBSCRIBE TO OUR NEWSLETTER</h3>
        <button class="newsletter-btn" @click="showSubscribe">
          Subscribe Now!
          <i class="fas fa-paper-plane"></i>
        </button>
      </div>
    </section>
  </main>
</template>
