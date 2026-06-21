<script setup>
import { onMounted } from 'vue'

window.filterCases = function(category) {
  const buttons = document.querySelectorAll('.tab-btn');
  buttons.forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');

  const cards = document.querySelectorAll('.case-card');
  cards.forEach(card => {
    const cat = card.getAttribute('data-category');
    if (category === 'all' || cat === category) {
      card.style.display = 'flex';
      card.classList.remove('visible');
      setTimeout(() => card.classList.add('visible'), 50);
    } else {
      card.style.display = 'none';
    }
  });
}

window.openCaseModal = function(title, location, capacity, projectType, equipment, carbon, desc, img) {
  document.getElementById('modalCaseTitle').textContent = title;
  document.getElementById('modalCaseLocation').textContent = location;
  document.getElementById('modalCaseImg').src = img;
  document.getElementById('modalCaseCapacity').textContent = capacity;
  document.getElementById('modalCaseEquipment').textContent = equipment;
  document.getElementById('modalCaseCarbon').textContent = carbon;
  document.getElementById('modalCaseDesc').textContent = desc;

  document.getElementById('caseModal').classList.add('active');
}

window.closeCaseModal = function() {
  document.getElementById('caseModal').classList.remove('active');
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
  <section class="inner-hero">
    <div class="inner-hero-bg" style="background: url('images/hero-bg.jpg') center/cover no-repeat;"></div>
    <div class="inner-hero-overlay"></div>
    <div class="inner-hero-content">
      <h1 class="inner-hero-title">Success Cases</h1>
      <p class="inner-hero-desc">Explore our global solar installations delivering sustainable, clean power worldwide.</p>
    </div>
  </section>

  <!-- Cases Section -->
  <section class="section-padding">
    <div class="filter-tabs fade-in">
      <button class="tab-btn active" onclick="filterCases('all')">All Sectors</button>
      <button class="tab-btn" onclick="filterCases('residential')">Residential</button>
      <button class="tab-btn" onclick="filterCases('commercial')">Commercial & Industrial</button>
      <button class="tab-btn" onclick="filterCases('utility')">Utility Scale</button>
    </div>

    <div class="cases-grid">
      <!-- Case 1 -->
      <div class="case-card fade-in" data-category="commercial" onclick="openCaseModal('1.2MW C&I Solar Plant', 'Madrid, Spain', '1,200 kW', 'Solar Farm', 'X3 Industrial Inverters', '750 Tons/Year', 'Commissioned in April 2024, this industrial rooftop project provides 40% of the factory\'s electricity demands. Featuring a zero-export controller to comply with the local grid, the facility utilizes our high-efficiency string inverters and modular mounting to withstand high winds.', 'images/solar-farm.jpg')">
        <div class="case-img-box">
          <img src="/images/solar-farm.jpg" alt="Solar Farm Rooftop">
          <span class="case-badge">Commercial</span>
        </div>
        <div class="case-content">
          <div class="case-meta">
            <span><i class="fas fa-location-dot"></i> Madrid, Spain</span>
            <span><i class="fas fa-calendar"></i> 2024</span>
          </div>
          <h3>1.2MW C&I Solar Plant on Industrial Rooftops</h3>
          <div class="case-stats">
            <div>
              <div class="case-stat-val">1.2 MW</div>
              <div class="case-stat-lbl">Capacity</div>
            </div>
            <div>
              <div class="case-stat-val">750 T</div>
              <div class="case-stat-lbl">CO2 Saved</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Case 2 -->
      <div class="case-card fade-in" data-category="residential" onclick="openCaseModal('10kW Residential Solar + Storage', 'Munich, Germany', '10 kW PV / 15kWh Storage', 'Residential Home', 'X1 Hybrid Inverter + Battery Storage L1', '6.2 Tons/Year', 'This residential installation provides full self-sufficiency for a family of four. Excess energy generated during sunny hours is stored in our L1 battery packs. A smart backup gateway ensures that critical house loads (refrigerator, heating, lighting) remain operational during local utility disruptions.', 'images/pv-system.jpg')">
        <div class="case-img-box">
          <img src="/images/pv-system.jpg" alt="Residential Solar Panels">
          <span class="case-badge">Residential</span>
        </div>
        <div class="case-content">
          <div class="case-meta">
            <span><i class="fas fa-location-dot"></i> Munich, Germany</span>
            <span><i class="fas fa-calendar"></i> 2025</span>
          </div>
          <h3>10kW Residential Solar + Storage Home Solution</h3>
          <div class="case-stats">
            <div>
              <div class="case-stat-val">10 kW</div>
              <div class="case-stat-lbl">PV Capacity</div>
            </div>
            <div>
              <div class="case-stat-val">15 kWh</div>
              <div class="case-stat-lbl">Storage</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Case 3 -->
      <div class="case-card fade-in" data-category="utility" onclick="openCaseModal('50MW Utility Solar Farm', 'Arizona, USA', '50 MW', 'Utility Solar Farm', 'Smart Central Megawatt Station', '35,000 Tons/Year', 'A massive utility-scale grid-connected PV station in the Arizona desert. The system operates under harsh thermal fluctuations, boasting string level monitoring and smart anti-PID tracking structures to prevent degradation. Managed remotely via our enterprise SCADA connection.', 'images/solar-farm.jpg')">
        <div class="case-img-box">
          <img src="/images/solar-farm.jpg" alt="Utility Scale Solar Fields">
          <span class="case-badge">Utility</span>
        </div>
        <div class="case-content">
          <div class="case-meta">
            <span><i class="fas fa-location-dot"></i> Arizona, USA</span>
            <span><i class="fas fa-calendar"></i> 2023</span>
          </div>
          <h3>50MW Grid-Connected Desert Solar Field Project</h3>
          <div class="case-stats">
            <div>
              <div class="case-stat-val">50 MW</div>
              <div class="case-stat-lbl">Capacity</div>
            </div>
            <div>
              <div class="case-stat-val">35k T</div>
              <div class="case-stat-lbl">CO2 Saved</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Case 4 -->
      <div class="case-card fade-in" data-category="commercial" onclick="openCaseModal('350kW Solar + Smart EV Charging Hub', 'London, UK', '350 kW PV / 10 EV Ports', 'Fleet Depot Charging Station', 'X3 Inverters + EV Chargers Pro', '180 Tons/Year', 'An innovative logistics park project that charges local delivery vehicles using rooftop solar panels. A smart management controller dynamically routes power between solar arrays, high-capacity hybrid batteries, and smart EV chargers based on fleet schedules.', 'images/ev-charger.jpg')">
        <div class="case-img-box">
          <img src="/images/ev-charger.jpg" alt="EV charging station hubs">
          <span class="case-badge">Commercial</span>
        </div>
        <div class="case-content">
          <div class="case-meta">
            <span><i class="fas fa-location-dot"></i> London, UK</span>
            <span><i class="fas fa-calendar"></i> 2026</span>
          </div>
          <h3>350kW Solar + Smart EV Fleet Charging Facility</h3>
          <div class="case-stats">
            <div>
              <div class="case-stat-val">350 kW</div>
              <div class="case-stat-lbl">PV Capacity</div>
            </div>
            <div>
              <div class="case-stat-val">10 Ports</div>
              <div class="case-stat-lbl">EV Chargers</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Case Details Lightbox Modal -->
  <div class="modal" id="caseModal">
    <div class="modal-content" style="max-width: 700px;">
      <button class="modal-close" onclick="closeCaseModal()">&times;</button>
      <h3 style="font-size: 22px; color: var(--dark-blue); margin-bottom: 8px;" id="modalCaseTitle">Case Title</h3>
      <p style="font-size: 13px; color: var(--primary-green-dark); font-weight: 600; margin-bottom: 20px;" id="modalCaseLocation">Location</p>
      
      <img src="" alt="Case Image" class="case-modal-img" id="modalCaseImg">

      <div class="case-modal-specs">
        <div class="case-modal-spec-item">
          <span class="case-modal-spec-lbl">Capacity</span>
          <span class="case-modal-spec-val" id="modalCaseCapacity">-</span>
        </div>
        <div class="case-modal-spec-item">
          <span class="case-modal-spec-lbl">Inverter Equipment</span>
          <span class="case-modal-spec-val" id="modalCaseEquipment">-</span>
        </div>
        <div class="case-modal-spec-item">
          <span class="case-modal-spec-lbl">CO2 Offsets</span>
          <span class="case-modal-spec-val" id="modalCaseCarbon">-</span>
        </div>
      </div>

      <h4 style="font-size: 14px; color: var(--text-dark); margin-bottom: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Project Description</h4>
      <p style="color: var(--text-gray); font-size: 13px; line-height: 1.6; margin-bottom: 20px;" id="modalCaseDesc">Description</p>
      
      <button class="btn-solid" onclick="closeCaseModal()" style="padding: 10px 24px;">Close Case Details</button>
    </div>
  </div>



<!-- Footer -->
  </main>
</template>
