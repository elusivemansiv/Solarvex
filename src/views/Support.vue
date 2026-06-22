<script setup>
import { onMounted } from 'vue'

window.checkWarranty = function() {
  const input = document.getElementById('serialNumberInput').value.trim();
  const successBox = document.getElementById('warrantySuccess');
  const errorBox = document.getElementById('warrantyError');
  const text = document.getElementById('warrantySuccessText');

  successBox.style.display = 'none';
  errorBox.style.display = 'none';

  if (input === '') {
    alert('Please enter a valid serial number.');
    return;
  }

  if (input.toUpperCase() === 'VEX-2026-XYZ') {
    text.innerHTML = '<strong>Model:</strong> Solar Inverter X1 (VEX-S1-6000) <br> <strong>Expiration Date:</strong> June 11, 2036 <br> <strong>Warranty Status:</strong> Active (Full Replacement coverage)';
    successBox.style.display = 'block';
  } else if (input.toUpperCase().startsWith('VEX-')) {
    text.innerHTML = '<strong>Model:</strong> Registered Solar Vex Product <br> <strong>Expiration Date:</strong> Valid until 10 years from installation date <br> <strong>Warranty Status:</strong> Active';
    successBox.style.display = 'block';
  } else {
    errorBox.style.display = 'block';
  }
}
window.toggleFaq = function(e) {
  const item = e.currentTarget.parentNode;
  item.classList.toggle('active');
}
window.filterDownloads = function() {
  const search = document.getElementById('downloadSearch').value.toLowerCase();
  const type = document.getElementById('downloadType').value;
  const rows = document.querySelectorAll('#downloadsBody tr');

  rows.forEach(row => {
    const name = row.getAttribute('data-name');
    const rowType = row.getAttribute('data-type');
    const matchesSearch = name.includes(search);
    const matchesType = type === 'all' || rowType === type;
    if (matchesSearch && matchesType) {
      row.style.display = 'table-row';
    } else {
      row.style.display = 'none';
    }
  });
}
window.mockDownload = function(file) {
  event.preventDefault();
  alert('Your download for ' + file + ' has started successfully!');
}
window.submitTicket = function(e) {
  e.preventDefault();
  alert('Support ticket submitted successfully! A support engineer will respond to your email within 24 hours.');
  e.currentTarget.reset();
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
      <h1 class="inner-hero-title">Support & Contact</h1>
      <p class="inner-hero-desc">Find answers to technical issues, check product warranty statuses, download materials, or write to our support team.</p>
    </div>
  </section>

  <!-- Warranty Checker Section -->
  <section class="section-padding">
    <div class="warranty-box fade-in">
      <h3 style="font-size: 24px; color: var(--dark-blue); margin-bottom: 12px; font-weight: 800; text-transform: uppercase;">Check Product Warranty</h3>
      <p style="color: var(--text-gray); font-size: 14px;">Enter your product serial number below to verify warranty validation dates and registration status.</p>
      
      <div class="warranty-input-group">
        <input type="text" id="serialNumberInput" placeholder="Enter Serial Number (e.g. VEX-2026-XYZ)">
        <button onclick="checkWarranty()">Check Status</button>
      </div>

      <div class="warranty-result success" id="warrantySuccess">
        <h4 style="font-weight: 700; margin-bottom: 6px;"><i class="fas fa-circle-check"></i> Warranty Valid & Active</h4>
        <p style="font-size: 13px;" id="warrantySuccessText">Model: VEX-S1-6000 | Expire Date: Dec 12, 2031 | Coverage: Full Parts & Labor.</p>
      </div>
      <div class="warranty-result error" id="warrantyError">
        <h4 style="font-weight: 700; margin-bottom: 6px;"><i class="fas fa-circle-xmark"></i> Serial Number Not Found</h4>
        <p style="font-size: 13px;">Please verify your code or contact support to register your product warranty.</p>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section style="background: var(--bg-light);" class="section-padding">
    <div class="section-title fade-in">
      <h2>Frequently Asked Questions</h2>
    </div>
    
    <div class="faq-list">
      <!-- FAQ 1 -->
      <div class="faq-item fade-in">
        <button class="faq-trigger" onclick="toggleFaq(event)">
          How do I connect my Solar Vex inverter to WiFi?
          <i class="fas fa-chevron-down"></i>
        </button>
        <div class="faq-content">
          <p>To connect, plug the ShineLink WiFi dongle into the USB port under the inverter. Download the ShinePhone mobile app, register an account, scan the dongle QR code, select your local home router network, and enter the password. The indicator light should turn green once connected.</p>
        </div>
      </div>
      
      <!-- FAQ 2 -->
      <div class="faq-item fade-in">
        <button class="faq-trigger" onclick="toggleFaq(event)">
          What should I do if the inverter displays error "GRID FAULT"?
          <i class="fas fa-chevron-down"></i>
        </button>
        <div class="faq-content">
          <p>"GRID FAULT" indicates local grid voltage or frequency exceeds the standard range. This usually resolves automatically within a few minutes once local line conditions stabilize. If the warning persists, please contact your local solar installer or electrical contractor to measure the AC side line parameters.</p>
        </div>
      </div>

      <!-- FAQ 3 -->
      <div class="faq-item fade-in">
        <button class="faq-trigger" onclick="toggleFaq(event)">
          Can I add more battery modules to an existing storage pack later?
          <i class="fas fa-chevron-down"></i>
        </button>
        <div class="faq-content">
          <p>Yes, our Battery Storage L1 packs are modular. You can stack additional 5kWh modules together up to a maximum of 6 modules (30kWh capacity) per hybrid inverter. Ensure your inverter firmware is updated to support expanded battery cell configurations before adding them.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Download Center -->
  <section class="section-padding">
    <div class="section-title fade-in">
      <h2>Download Center</h2>
    </div>

    <div class="downloads-filter-bar fade-in">
      <input type="text" id="downloadSearch" placeholder="Search manuals..." onkeyup="filterDownloads()" style="flex-grow: 1;">
      <select id="downloadType" onchange="filterDownloads()">
        <option value="all">All Documents</option>
        <option value="manual">Manuals</option>
        <option value="datasheet">Datasheets</option>
        <option value="certificate">Certificates</option>
      </select>
    </div>

    <table class="downloads-table fade-in">
      <thead>
        <tr>
          <th>Document Name</th>
          <th>Type</th>
          <th>Language</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody id="downloadsBody">
        <tr data-type="datasheet" data-name="solar inverter x1 string inverter datasheet vex-s1-6000">
          <td>Solar Inverter X1 Datasheet</td>
          <td><span class="doc-type-badge datasheet">Datasheet</span></td>
          <td>English</td>
          <td><a href="#" onclick="mockDownload('Solar_Inverter_X1_Datasheet.pdf')"><i class="fas fa-file-pdf"></i> Download (1.2MB)</a></td>
        </tr>
        <tr data-type="manual" data-name="solar inverter x1 installation user manual guide">
          <td>Solar Inverter X1 User Manual</td>
          <td><span class="doc-type-badge manual">Manual</span></td>
          <td>English</td>
          <td><a href="#" onclick="mockDownload('Solar_Inverter_X1_User_Manual.pdf')"><i class="fas fa-file-pdf"></i> Download (4.5MB)</a></td>
        </tr>
        <tr data-type="datasheet" data-name="battery storage l1 modular pack battery cell datasheet">
          <td>Battery Storage L1 Datasheet</td>
          <td><span class="doc-type-badge datasheet">Datasheet</span></td>
          <td>English</td>
          <td><a href="#" onclick="mockDownload('Battery_Storage_L1_Datasheet.pdf')"><i class="fas fa-file-pdf"></i> Download (1.8MB)</a></td>
        </tr>
        <tr data-type="manual" data-name="ev charger pro smart 22kw manual installation guidelines">
          <td>EV Charger Pro User Manual</td>
          <td><span class="doc-type-badge manual">Manual</span></td>
          <td>English</td>
          <td><a href="#" onclick="mockDownload('EV_Charger_Pro_Manual.pdf')"><i class="fas fa-file-pdf"></i> Download (2.9MB)</a></td>
        </tr>
        <tr data-type="certificate" data-name="tuv certificate conformity standard grid solar vex inverters">
          <td>TUV Certificate of Conformity (IEC 62109)</td>
          <td><span class="doc-type-badge certificate">Certificate</span></td>
          <td>German</td>
          <td><a href="#" onclick="mockDownload('TUV_Certificate_IEC62109.pdf')"><i class="fas fa-file-pdf"></i> Download (920KB)</a></td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- Office & Contact Form -->
  <section style="background: var(--bg-light);" class="section-padding">
    <div class="section-title fade-in">
      <h2>Contact Us</h2>
    </div>

    <div class="support-contact-grid">
      <!-- Contact Form -->
      <div class="glass-card fade-in" style="background: white;">
        <h3 style="font-size: 20px; color: var(--dark-blue); margin-bottom: 20px; font-weight: 700;">Submit a Support Ticket</h3>
        <form onsubmit="submitTicket(event)">
          <div class="form-group">
            <label>Name</label>
            <input type="text" class="form-control" placeholder="Jane Smith" required>
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="email" class="form-control" placeholder="jane@example.com" required>
          </div>
          <div class="form-group">
            <label>Inquiry Category</label>
            <select class="form-control" required>
              <option value="tech">Technical Support</option>
              <option value="sales">Sales Inquiry</option>
              <option value="warranty">Warranty Claim</option>
            </select>
          </div>
          <div class="form-group">
            <label>Detailed Message</label>
            <textarea class="form-control" style="height: 120px; resize: none;" placeholder="Explain your inquiry in detail..." required></textarea>
          </div>
          <button type="submit" class="btn-solid" style="width: 100%; padding: 12px; margin-top: 10px;">Submit Ticket</button>
        </form>
      </div>

      <!-- Offices -->
      <div class="fade-in">
        <h3 style="font-size: 20px; color: var(--dark-blue); margin-bottom: 20px; font-weight: 700;">Global Offices</h3>
        
        <div class="offices-grid">
          <!-- Office 1 -->
          <div class="office-card">
            <h4><i class="fas fa-building"></i> Headquarters Office</h4>
            <p><i class="fas fa-location-dot"></i> 456 Energy Blvd, Tech District, City</p>
            <p><i class="fas fa-phone"></i> +1 (555) 019-2834</p>
            <p><i class="fas fa-envelope"></i> contact@solarvex.com</p>
          </div>
          <!-- Office 2 -->
          <div class="office-card">
            <h4><i class="fas fa-earth-europe"></i> Europe Support Center</h4>
            <p><i class="fas fa-location-dot"></i> Frankfurt Innovation Park, Frankfurt, Germany</p>
            <p><i class="fas fa-phone"></i> +49 (0) 69 987654</p>
            <p><i class="fas fa-envelope"></i> eu.support@solarvex.com</p>
          </div>
        </div>
      </div>
    </div>
  </section>



<!-- Footer -->
  </main>
</template>
