<script setup>
import { onMounted } from 'vue'

window.updateCounts = function() {
  const cards = document.querySelectorAll('.product-catalog-card');
  const counts = { all: cards.length, inverter: 0, battery: 0, ev: 0, monitoring: 0 };
  cards.forEach(card => {
    const cat = card.getAttribute('data-category');
    if (counts[cat] !== undefined) counts[cat]++;
  });
  for (let key in counts) {
    const el = document.getElementById('count-' + key);
    if (el) el.textContent = counts[key];
  }
}

let activeCategory = 'all';

window.switchCategory = function(cat) {
  activeCategory = cat;
  const links = document.querySelectorAll('.sidebar-link');
  links.forEach(l => l.classList.remove('active'));
  event.currentTarget.classList.add('active');
  window.filterProducts();
}

window.filterProducts = function() {
  const search = document.getElementById('productSearch').value.toLowerCase();
  const cards = document.querySelectorAll('.product-catalog-card');
  
  cards.forEach(card => {
    const title = card.querySelector('h3').textContent.toLowerCase();
    const model = card.querySelector('.model-num').textContent.toLowerCase();
    const cat = card.getAttribute('data-category');
    
    const matchesSearch = title.includes(search) || model.includes(search);
    const matchesCat = activeCategory === 'all' || cat === activeCategory;
    
    if (matchesSearch && matchesCat) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
}

window.openInquiry = function(product) {
  document.getElementById('inquiryProduct').value = product;
  document.getElementById('inquiryModal').classList.add('active');
}

window.closeInquiry = function() {
  document.getElementById('inquiryModal').classList.remove('active');
}

window.submitInquiry = function(e) {
  e.preventDefault();
  alert('Your inquiry for ' + document.getElementById('inquiryProduct').value + ' has been sent successfully! Our sales team will contact you shortly.');
  window.closeInquiry();
}

window.viewDatasheet = function(name, model) {
  alert('Opening technical datasheet for ' + name + ' (' + model + ')...');
}

onMounted(() => {
  window.updateCounts();
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
      <h1 class="inner-hero-title">Product Catalog</h1>
      <p class="inner-hero-desc">Explore our full line of advanced solar inverters, energy storage, smart EV chargers, and accessories.</p>
    </div>
  </section>

  <!-- Products Section -->
  <section class="section-padding">
    <div class="products-layout">
      <!-- Sidebar Filters -->
      <aside class="products-sidebar fade-in">
        <div class="sidebar-search">
          <i class="fas fa-search"></i>
          <input type="text" id="productSearch" placeholder="Search products..." onkeyup="filterProducts()">
        </div>
        <div class="sidebar-menu-title">Categories</div>
        <ul class="sidebar-menu">
          <li class="sidebar-item"><a class="sidebar-link active" onclick="switchCategory('all')">All Products <span class="count" id="count-all">0</span></a></li>
          <li class="sidebar-item"><a class="sidebar-link" onclick="switchCategory('inverter')">PV Inverters <span class="count" id="count-inverter">0</span></a></li>
          <li class="sidebar-item"><a class="sidebar-link" onclick="switchCategory('battery')">Battery Systems <span class="count" id="count-battery">0</span></a></li>
          <li class="sidebar-item"><a class="sidebar-link" onclick="switchCategory('ev')">EV Chargers <span class="count" id="count-ev">0</span></a></li>
          <li class="sidebar-item"><a class="sidebar-link" onclick="switchCategory('monitoring')">Smart Monitoring <span class="count" id="count-monitoring">0</span></a></li>
        </ul>
      </aside>

      <!-- Products Grid -->
      <main class="products-catalog-grid-wrapper">
        <div class="products-catalog" id="productsGrid">
          <!-- Card 1 -->
          <div class="product-catalog-card fade-in" data-category="inverter">
            <div class="product-img-box">
              <span class="prod-badge">Hot</span>
              <div class="prod-icon"><i class="fas fa-bolt"></i></div>
            </div>
            <div class="product-details">
              <h3>Solar Inverter X1</h3>
              <div class="model-num">VEX-S1-6000</div>
              <ul class="product-features">
                <li><i class="fas fa-check"></i> 3kW - 6kW Single Phase</li>
                <li><i class="fas fa-check"></i> Dual MPPT trackers</li>
                <li><i class="fas fa-check"></i> Battery Ready architecture</li>
                <li><i class="fas fa-check"></i> Integrated AFCI protection</li>
              </ul>
              <div class="product-actions">
                <button class="btn-outline" onclick="viewDatasheet('Solar Inverter X1', 'VEX-S1-6000')">Datasheet</button>
                <button class="btn-solid" onclick="openInquiry('Solar Inverter X1')">Inquire</button>
              </div>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="product-catalog-card fade-in" data-category="inverter">
            <div class="product-img-box">
              <span class="prod-badge">C&I</span>
              <div class="prod-icon"><i class="fas fa-industry"></i></div>
            </div>
            <div class="product-details">
              <h3>Industrial Inverter X3</h3>
              <div class="model-num">VEX-T3-100K</div>
              <ul class="product-features">
                <li><i class="fas fa-check"></i> 100kW Three Phase Inverter</li>
                <li><i class="fas fa-check"></i> Up to 10 MPPT trackers</li>
                <li><i class="fas fa-check"></i> 99.0% Peak Efficiency</li>
                <li><i class="fas fa-check"></i> Smart I-V diagnosis scans</li>
              </ul>
              <div class="product-actions">
                <button class="btn-outline" onclick="viewDatasheet('Industrial Inverter X3', 'VEX-T3-100K')">Datasheet</button>
                <button class="btn-solid" onclick="openInquiry('Industrial Inverter X3')">Inquire</button>
              </div>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="product-catalog-card fade-in" data-category="battery">
            <div class="product-img-box">
              <span class="prod-badge">Modular</span>
              <div class="prod-icon"><i class="fas fa-battery-full"></i></div>
            </div>
            <div class="product-details">
              <h3>Battery Storage L1</h3>
              <div class="model-num">VEX-BAT-5K</div>
              <ul class="product-features">
                <li><i class="fas fa-check"></i> 5kWh LiFePO4 base module</li>
                <li><i class="fas fa-check"></i> Scalable up to 30kWh capacity</li>
                <li><i class="fas fa-check"></i> Cobalt-free safety design</li>
                <li><i class="fas fa-check"></i> 6000+ lifecycle guarantees</li>
              </ul>
              <div class="product-actions">
                <button class="btn-outline" onclick="viewDatasheet('Battery Storage L1', 'VEX-BAT-5K')">Datasheet</button>
                <button class="btn-solid" onclick="openInquiry('Battery Storage L1')">Inquire</button>
              </div>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="product-catalog-card fade-in" data-category="ev">
            <div class="product-img-box">
              <span class="prod-badge">Smart</span>
              <div class="prod-icon"><i class="fas fa-charging-station"></i></div>
            </div>
            <div class="product-details">
              <h3>EV Charger Pro</h3>
              <div class="model-num">VEX-EV-22K</div>
              <ul class="product-features">
                <li><i class="fas fa-check"></i> 7kW - 22kW charging speed</li>
                <li><i class="fas fa-check"></i> Dynamic load balance limits</li>
                <li><i class="fas fa-check"></i> Solar integration charge modes</li>
                <li><i class="fas fa-check"></i> RFID & Mobile App access</li>
              </ul>
              <div class="product-actions">
                <button class="btn-outline" onclick="viewDatasheet('EV Charger Pro', 'VEX-EV-22K')">Datasheet</button>
                <button class="btn-solid" onclick="openInquiry('EV Charger Pro')">Inquire</button>
              </div>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="product-catalog-card fade-in" data-category="monitoring">
            <div class="product-img-box">
              <span class="prod-badge">Plug & Play</span>
              <div class="prod-icon"><i class="fas fa-wifi"></i></div>
            </div>
            <div class="product-details">
              <h3>ShineLink WiFi Dongle</h3>
              <div class="model-num">VEX-WIFI-X</div>
              <ul class="product-features">
                <li><i class="fas fa-check"></i> Wireless RF communication</li>
                <li><i class="fas fa-check"></i> Direct USB Plug-and-Play</li>
                <li><i class="fas fa-check"></i> Local server data buffering</li>
                <li><i class="fas fa-check"></i> Auto network updates</li>
              </ul>
              <div class="product-actions">
                <button class="btn-outline" onclick="viewDatasheet('ShineLink WiFi Dongle', 'VEX-WIFI-X')">Datasheet</button>
                <button class="btn-solid" onclick="openInquiry('ShineLink WiFi Dongle')">Inquire</button>
              </div>
            </div>
          </div>

          <!-- Card 6 -->
          <div class="product-catalog-card fade-in" data-category="monitoring">
            <div class="product-img-box">
              <span class="prod-badge">Smart IoT</span>
              <div class="prod-icon"><i class="fas fa-plug-circle-check"></i></div>
            </div>
            <div class="product-details">
              <h3>Smart plug IoT</h3>
              <div class="model-num">VEX-PLUG-16A</div>
              <ul class="product-features">
                <li><i class="fas fa-check"></i> 16A smart load switcher</li>
                <li><i class="fas fa-check"></i> Real-time power statistics</li>
                <li><i class="fas fa-check"></i> Automated timer scheduling</li>
                <li><i class="fas fa-check"></i> GroHome network compatible</li>
              </ul>
              <div class="product-actions">
                <button class="btn-outline" onclick="viewDatasheet('Smart plug IoT', 'VEX-PLUG-16A')">Datasheet</button>
                <button class="btn-solid" onclick="openInquiry('Smart plug IoT')">Inquire</button>
              </div>
            </div>
          </div>

        </div>
      </main>
    </div>
  </section>

  <!-- Inquiry Modal -->
  <div class="modal" id="inquiryModal">
    <div class="modal-content">
      <button class="modal-close" onclick="closeInquiry()">&times;</button>
      <h3 style="font-size: 20px; color: var(--dark-blue); margin-bottom: 20px;">Request Product Information</h3>
      <form onsubmit="submitInquiry(event)">
        <div class="form-group">
          <label>Product Selected</label>
          <input type="text" id="inquiryProduct" class="form-control" readonly>
        </div>
        <div class="form-group">
          <label>Your Name</label>
          <input type="text" class="form-control" placeholder="John Doe" required>
        </div>
        <div class="form-group">
          <label>Email Address</label>
          <input type="email" class="form-control" placeholder="john@example.com" required>
        </div>
        <div class="form-group">
          <label>Message/Inquiry Details</label>
          <textarea class="form-control" style="height: 100px; resize: none;" placeholder="Tell us about your project requirements..." required></textarea>
        </div>
        <button type="submit" class="btn-solid" style="width: 100%; padding: 12px; margin-top: 10px;">Send Inquiry</button>
      </form>
    </div>
  </div>



<!-- Footer -->
  </main>
</template>
