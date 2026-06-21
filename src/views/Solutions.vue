<script setup>
import { onMounted } from 'vue'

window.filterSolutions = function(category) {
  const buttons = document.querySelectorAll('.tab-btn');
  buttons.forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');

  const blocks = document.querySelectorAll('.solution-block');
  blocks.forEach(block => {
    if (category === 'all' || block.getAttribute('data-category') === category) {
      block.style.display = 'grid';
      block.classList.remove('visible');
      setTimeout(() => block.classList.add('visible'), 50);
    } else {
      block.style.display = 'none';
    }
  });
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
    <div class="inner-hero-bg" style="background: url('images/hero-bg.jpg') center/cover no-repeat;"></div>
    <div class="inner-hero-overlay"></div>
    <div class="inner-hero-content">
      <h1 class="inner-hero-title">Energy Solutions</h1>
      <p class="inner-hero-desc">Smart solutions for green energy generation, storage, EV charging, and energy digitalization.</p>
    </div>
  </section>

  <!-- Solutions Section -->
  <section class="section-padding">
    <div class="filter-tabs fade-in">
      <button class="tab-btn active" onclick="filterSolutions('all')">All Solutions</button>
      <button class="tab-btn" onclick="filterSolutions('residential')">Residential</button>
      <button class="tab-btn" onclick="filterSolutions('commercial')">Commercial & Industrial (C&I)</button>
      <button class="tab-btn" onclick="filterSolutions('utility')">Utility Scale</button>
      <button class="tab-btn" onclick="filterSolutions('smart')">Smart GroHome & EV</button>
    </div>
    
    <div class="solutions-list-grid">
      <!-- Res PV Block -->
      <div class="solution-block fade-in" data-category="residential">
        <div class="solution-text-col">
          <h3>Residential PV System</h3>
          <p>Generate your own clean electricity directly from your rooftop. Our high-efficiency string and microinverter systems ensure maximum energy output, even in partial shade, while reducing your monthly utility bills to near zero.</p>
          <ul class="solution-specs">
            <li><i class="fas fa-check-circle"></i> 3kW to 15kW Capacity</li>
            <li><i class="fas fa-check-circle"></i> 98.4% Maximum Efficiency</li>
            <li><i class="fas fa-check-circle"></i> Real-time Module Monitoring</li>
            <li><i class="fas fa-check-circle"></i> Quick Plug-and-Play Install</li>
          </ul>
          <a href="/products" class="btn-solid">View Residential Products</a>
        </div>
        <div class="solution-graphic-col">
          <div class="diagram-flow">
            <div class="diagram-node">
              <i class="fas fa-solar-panel"></i>
              <span>Solar PV</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-bolt"></i>
              <span>Inverter</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-home"></i>
              <span>Home Load</span>
            </div>
          </div>
          <div class="diagram-label">Standard On-Grid Residential Setup</div>
        </div>
      </div>
      
      <!-- Res Storage Block -->
      <div class="solution-block reverse fade-in" data-category="residential">
        <div class="solution-text-col">
          <h3>Residential Storage System</h3>
          <p>Maximize your energy independence. By storing excess solar energy generated during the day, our battery storage solutions ensure your home stays powered during the night or during grid blackouts. Our modular design lets you scale your storage as your needs grow.</p>
          <ul class="solution-specs">
            <li><i class="fas fa-check-circle"></i> 5kWh to 30kWh Modular Capacity</li>
            <li><i class="fas fa-check-circle"></i> &lt;10ms UPS-level Backup Switch</li>
            <li><i class="fas fa-check-circle"></i> Cobalt-free LiFePO4 Safety</li>
            <li><i class="fas fa-check-circle"></i> 10-Year Product Warranty</li>
          </ul>
          <a href="/products" class="btn-solid">View Battery Systems</a>
        </div>
        <div class="solution-graphic-col">
          <div class="diagram-flow">
            <div class="diagram-node">
              <i class="fas fa-solar-panel"></i>
              <span>PV Array</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-shuffle"></i>
              <span>Hybrid Inv</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-battery-three-quarters"></i>
              <span>Battery Pack</span>
            </div>
          </div>
          <div class="diagram-label">Hybrid Solar + Storage Battery-Ready Setup</div>
        </div>
      </div>

      <!-- Commercial Block -->
      <div class="solution-block fade-in" data-category="commercial">
        <div class="solution-text-col">
          <h3>Commercial & Industrial (C&I)</h3>
          <p>Lower operating costs and meet corporate sustainability goals. Our solutions for factories, warehouses, and offices support peak-shaving, load scheduling, and smart power export limits to comply with local utility grids.</p>
          <ul class="solution-specs">
            <li><i class="fas fa-check-circle"></i> 50kW to 250kW string inverters</li>
            <li><i class="fas fa-check-circle"></i> Multi-MPPT for varied roofs</li>
            <li><i class="fas fa-check-circle"></i> String monitoring & I-V scan</li>
            <li><i class="fas fa-check-circle"></i> Active AFCI fire prevention</li>
          </ul>
          <a href="/products" class="btn-solid">Explore C&I Products</a>
        </div>
        <div class="solution-graphic-col">
          <div class="diagram-flow">
            <div class="diagram-node">
              <i class="fas fa-industry"></i>
              <span>Factory Load</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-bolt"></i>
              <span>C&I Inverter</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-tower-broadcast"></i>
              <span>Utility Grid</span>
            </div>
          </div>
          <div class="diagram-label">Grid-Interactive Commercial Grid Setup</div>
        </div>
      </div>

      <!-- Utility Block -->
      <div class="solution-block reverse fade-in" data-category="utility">
        <div class="solution-text-col">
          <h3>Utility-Scale PV Plants</h3>
          <p>Engineered for high yields and grid stability, our utility solutions offer high DC/AC ratios, compatibility with bifacial panels, tracking system compatibility, and advanced grid support features (VAR/reactive power at night).</p>
          <ul class="solution-specs">
            <li><i class="fas fa-check-circle"></i> 300kW+ central & string units</li>
            <li><i class="fas fa-check-circle"></i> IP66 dust & water protection</li>
            <li><i class="fas fa-check-circle"></i> Smart PID recovery function</li>
            <li><i class="fas fa-check-circle"></i> SCADA integration protocols</li>
          </ul>
          <a href="/products" class="btn-solid">View Utility Solutions</a>
        </div>
        <div class="solution-graphic-col">
          <div class="diagram-flow">
            <div class="diagram-node">
              <i class="fas fa-solar-panel"></i>
              <span>PV Arrays</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-box"></i>
              <span>Megawatt Station</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-network-wired"></i>
              <span>Substation</span>
            </div>
          </div>
          <div class="diagram-label">Large Scale PV Power Generation Grid Diagram</div>
        </div>
      </div>

      <!-- Smart Block -->
      <div class="solution-block fade-in" data-category="smart">
        <div class="solution-text-col">
          <h3>GroHome Smart Ecosystem</h3>
          <p>Take charge of your entire energy flow. GroHome integrates your solar inverter, battery storage, smart EV charger, heat pump, and IoT smart plugs into one automated system that shifts loads to times of high solar generation.</p>
          <ul class="solution-specs">
            <li><i class="fas fa-check-circle"></i> Dynamic load balancing</li>
            <li><i class="fas fa-check-circle"></i> Solar-only EV charging modes</li>
            <li><i class="fas fa-check-circle"></i> Custom automation profiles</li>
            <li><i class="fas fa-check-circle"></i> iOS & Android app controls</li>
          </ul>
          <a href="/products" class="btn-solid">Discover GroHome</a>
        </div>
        <div class="solution-graphic-col">
          <div class="diagram-flow">
            <div class="diagram-node">
              <i class="fas fa-mobile-screen-button"></i>
              <span>App Manager</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-charging-station"></i>
              <span>EV Charger</span>
            </div>
            <div class="diagram-node">
              <i class="fas fa-plug-circle-check"></i>
              <span>IoT Plugs</span>
            </div>
          </div>
          <div class="diagram-label">Fully Integrated Home IoT & EV Setup</div>
        </div>
      </div>

    </div>
  </section>
  


<!-- Footer -->
  </main>
</template>
