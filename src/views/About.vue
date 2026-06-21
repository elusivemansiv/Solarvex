<script setup>
import { onMounted } from 'vue'

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
  <section class="inner-hero">
    <div class="inner-hero-bg" style="background: url('images/hero-bg.jpg') center/cover no-repeat;"></div>
    <div class="inner-hero-overlay"></div>
    <div class="inner-hero-content">
      <h1 class="inner-hero-title">About Solar Vex</h1>
      <p class="inner-hero-desc">Leading the transition to a sustainable future with innovative solar, storage, and smart energy solutions.</p>
    </div>
  </section>

  <!-- Our Story Section -->
  <section class="section-padding">
    <div class="section-title fade-in">
      <h2>Our Story</h2>
    </div>
    <div style="max-width: 800px; margin: 0 auto 50px; text-align: center;" class="fade-in">
      <p style="color: var(--text-gray); font-size: 16px;">Founded with a vision to make clean energy accessible to everyone, Solar Vex has grown from a local solar technology pioneer into a global leading provider of distributed energy solutions. We design, manufacture, and deliver smart PV systems, battery storage, and EV chargers for residential, commercial, and utility-scale projects.</p>
    </div>
    
    <div class="timeline">
      <div class="timeline-item left fade-in">
        <div class="timeline-content">
          <div class="timeline-year">2016</div>
          <h3>Company Founded</h3>
          <p>Solar Vex was established with a focus on developing high-efficiency string inverters for residential solar systems.</p>
        </div>
      </div>
      <div class="timeline-item right fade-in">
        <div class="timeline-content">
          <div class="timeline-year">2018</div>
          <h3>Global Expansion</h3>
          <p>Launched our first international branches in Europe and South America. Introduced battery-ready inverters to the market.</p>
        </div>
      </div>
      <div class="timeline-item left fade-in">
        <div class="timeline-content">
          <div class="timeline-year">2021</div>
          <h3>Smart Storage Solutions</h3>
          <p>Released our modular battery storage systems and fully integrated smart energy management solutions for homes (GroHome).</p>
        </div>
      </div>
      <div class="timeline-item right fade-in">
        <div class="timeline-content">
          <div class="timeline-year">2024</div>
          <h3>EV Charger Integration</h3>
          <p>Expanded our portfolio with smart EV Chargers, enabling complete synergy between solar generation, battery storage, and electric mobility.</p>
        </div>
      </div>
      <div class="timeline-item left fade-in">
        <div class="timeline-content">
          <div class="timeline-year">2026</div>
          <h3>6 Million+ Users</h3>
          <p>Serving millions of users worldwide with reliable distributed energy solutions, contributing to global carbon neutrality goals.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Core Values Section -->
  <section style="background: var(--bg-light);" class="section-padding">
    <div class="section-title fade-in">
      <h2>Our Core Values</h2>
    </div>
    <div class="values-grid">
      <div class="glass-card value-card fade-in">
        <div class="value-icon"><i class="fas fa-lightbulb"></i></div>
        <h3>Innovation First</h3>
        <p>Continuous research and development to bring the most advanced, efficient, and reliable energy tech to the market.</p>
      </div>
      <div class="glass-card value-card fade-in">
        <div class="value-icon"><i class="fas fa-shield-halved"></i></div>
        <h3>Uncompromising Quality</h3>
        <p>Rigorous quality controls and manufacturing standards ensuring long-term product durability and client trust.</p>
      </div>
      <div class="glass-card value-card fade-in">
        <div class="value-icon"><i class="fas fa-handshake"></i></div>
        <h3>Customer Centric</h3>
        <p>Delivering comprehensive support, training, and warranties to optimize consumer returns on investment.</p>
      </div>
      <div class="glass-card value-card fade-in">
        <div class="value-icon"><i class="fas fa-seedling"></i></div>
        <h3>Sustainability</h3>
        <p>Dedicated to enabling a net-zero future by reducing carbon emissions through scalable green energy adoption.</p>
      </div>
    </div>
  </section>

  <!-- R&D Section -->
  <section class="section-padding">
    <div class="about-rd-grid">
      <div class="fade-in">
        <h2 class="rd-title">Advanced R&D & Manufacturing</h2>
        <p style="color: var(--text-gray); margin-bottom: 20px; font-size: 15px;">With over 60% of our team dedicated to technological research and development, Solar Vex holds more than 150 patents globally. Our state-of-the-art manufacturing facilities are automated to ensure every product conforms to strict quality benchmarks.</p>
        <p style="color: var(--text-gray); font-size: 15px;">We test every inverter and battery module under extreme environment chambers, simulating thermal shock, humidity, dust, and electrical overload to guarantee maximum lifespan.</p>
      </div>
      <div class="about-stats-grid">
        <div class="glass-card fade-in" style="text-align: center; padding: 24px;">
          <h3 style="font-size: 36px; color: var(--primary-green); margin-bottom: 8px; font-weight: 800;">500+</h3>
          <p style="font-size: 12px; color: var(--text-light); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">R&D Engineers</p>
        </div>
        <div class="glass-card fade-in" style="text-align: center; padding: 24px;">
          <h3 style="font-size: 36px; color: var(--primary-green); margin-bottom: 8px; font-weight: 800;">20GW</h3>
          <p style="font-size: 12px; color: var(--text-light); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Annual Capacity</p>
        </div>
        <div class="glass-card fade-in" style="text-align: center; padding: 24px;">
          <h3 style="font-size: 36px; color: var(--primary-green); margin-bottom: 8px; font-weight: 800;">150+</h3>
          <p style="font-size: 12px; color: var(--text-light); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Patents Filed</p>
        </div>
        <div class="glass-card fade-in" style="text-align: center; padding: 24px;">
          <h3 style="font-size: 36px; color: var(--primary-green); margin-bottom: 8px; font-weight: 800;">180+</h3>
          <p style="font-size: 12px; color: var(--text-light); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Global Markets</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Partners Section -->
  <section style="background: var(--bg-light);" class="section-padding">
    <div class="section-title fade-in">
      <h2>Our Partners</h2>
    </div>
    <div class="partner-grid fade-in">
      <div class="partner-logo">TUV SUD</div>
      <div class="partner-logo">Intertek</div>
      <div class="partner-logo">BloombergNEF</div>
      <div class="partner-logo">DNV GL</div>
      <div class="partner-logo">SGS</div>
      <div class="partner-logo">EuPD Research</div>
    </div>
  </section>


<!-- Footer -->
  </main>
</template>
