<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const handleLogout = () => {
  // In a real app, clear auth tokens here
  alert('You have been logged out.')
  router.push('/')
}

onMounted(() => {
  // Animation for the fake chart bars
  setTimeout(() => {
    const bars = document.querySelectorAll('.chart-bar-fill')
    bars.forEach(bar => {
      bar.style.height = bar.dataset.height + '%'
    })
  }, 100)
})
</script>

<template>
  <main class="dashboard-page">
    <div class="dashboard-header">
      <div class="dashboard-inner">
        <h1>Welcome Back, User</h1>
        <button class="logout-btn" @click="handleLogout">
          <i class="fas fa-sign-out-alt"></i> Logout
        </button>
      </div>
    </div>

    <div class="dashboard-content dashboard-inner">
      <!-- Status Cards -->
      <div class="status-grid">
        <div class="status-card">
          <div class="status-icon" style="color: var(--primary-green); background: rgba(139,195,74,0.1);"><i class="fas fa-sun"></i></div>
          <div class="status-info">
            <p>Current Solar Generation</p>
            <h3>4.2 kW</h3>
          </div>
        </div>
        <div class="status-card">
          <div class="status-icon" style="color: #2196F3; background: rgba(33,150,243,0.1);"><i class="fas fa-battery-three-quarters"></i></div>
          <div class="status-info">
            <p>Battery Level</p>
            <h3>82%</h3>
          </div>
        </div>
        <div class="status-card">
          <div class="status-icon" style="color: #FF9800; background: rgba(255,152,0,0.1);"><i class="fas fa-bolt"></i></div>
          <div class="status-info">
            <p>Home Consumption</p>
            <h3>1.8 kW</h3>
          </div>
        </div>
        <div class="status-card">
          <div class="status-icon" style="color: #9C27B0; background: rgba(156,39,176,0.1);"><i class="fas fa-network-wired"></i></div>
          <div class="status-info">
            <p>Grid Status</p>
            <h3>Exporting 2.4 kW</h3>
          </div>
        </div>
      </div>

      <!-- Main Panels -->
      <div class="panels-grid">
        <!-- Energy Flow Chart (Mock) -->
        <div class="panel">
          <h2>Energy Production (Last 7 Days)</h2>
          <div class="mock-chart">
            <div class="chart-col">
              <div class="chart-bar"><div class="chart-bar-fill" data-height="60"></div></div>
              <span class="chart-label">Mon</span>
            </div>
            <div class="chart-col">
              <div class="chart-bar"><div class="chart-bar-fill" data-height="85"></div></div>
              <span class="chart-label">Tue</span>
            </div>
            <div class="chart-col">
              <div class="chart-bar"><div class="chart-bar-fill" data-height="40"></div></div>
              <span class="chart-label">Wed</span>
            </div>
            <div class="chart-col">
              <div class="chart-bar"><div class="chart-bar-fill" data-height="90"></div></div>
              <span class="chart-label">Thu</span>
            </div>
            <div class="chart-col">
              <div class="chart-bar"><div class="chart-bar-fill" data-height="100"></div></div>
              <span class="chart-label">Fri</span>
            </div>
            <div class="chart-col">
              <div class="chart-bar"><div class="chart-bar-fill" data-height="75"></div></div>
              <span class="chart-label">Sat</span>
            </div>
            <div class="chart-col">
              <div class="chart-bar"><div class="chart-bar-fill" data-height="80"></div></div>
              <span class="chart-label">Sun</span>
            </div>
          </div>
        </div>

        <!-- System Details & Alerts -->
        <div class="panel side-panel">
          <h2>System Alerts</h2>
          <div class="alert-item success">
            <i class="fas fa-check-circle"></i>
            <div>
              <strong>System Operating Normally</strong>
              <p>All inverters are online.</p>
            </div>
          </div>
          <div class="alert-item info">
            <i class="fas fa-info-circle"></i>
            <div>
              <strong>Firmware Update Available</strong>
              <p>Update to version 2.4.1 for better battery optimization.</p>
            </div>
          </div>
          
          <h2 style="margin-top: 32px;">Quick Actions</h2>
          <button class="quick-action-btn"><i class="fas fa-download"></i> Download Monthly Report</button>
          <button class="quick-action-btn"><i class="fas fa-cog"></i> Adjust Battery Profile</button>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
.dashboard-page {
  padding-top: 70px;
  min-height: calc(100vh - 70px);
  background: var(--bg-light);
  padding-bottom: 60px;
}

.dashboard-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 40px;
}

.dashboard-header {
  background: white;
  padding: 30px 0;
  border-bottom: 1px solid rgba(0,0,0,0.05);
  margin-bottom: 40px;
}

.dashboard-header .dashboard-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dashboard-header h1 {
  font-size: 28px;
  font-weight: 800;
  color: var(--dark-blue);
}

.logout-btn {
  background: white;
  border: 1px solid #e0e0e0;
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-dark);
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.logout-btn:hover {
  background: #fff0f0;
  color: #d32f2f;
  border-color: #ffcdd2;
}

/* Status Cards */
.status-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-bottom: 32px;
}

.status-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.03);
  transition: transform 0.3s;
}

.status-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}

.status-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

.status-info p {
  font-size: 13px;
  color: var(--text-gray);
  margin-bottom: 4px;
  font-weight: 600;
}

.status-info h3 {
  font-size: 24px;
  font-weight: 800;
  color: var(--text-dark);
}

/* Panels */
.panels-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
}

.panel {
  background: white;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.03);
}

.panel h2 {
  font-size: 18px;
  font-weight: 700;
  color: var(--dark-blue);
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

/* Mock Chart */
.mock-chart {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  height: 300px;
  padding-top: 20px;
}

.chart-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  width: 10%;
}

.chart-bar {
  width: 100%;
  height: 240px;
  background: var(--bg-light);
  border-radius: 6px;
  position: relative;
  overflow: hidden;
}

.chart-bar-fill {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0%; /* Animates on mount */
  background: linear-gradient(180deg, var(--primary-green) 0%, var(--primary-green-dark) 100%);
  border-radius: 6px;
  transition: height 1s cubic-bezier(0.4, 0, 0.2, 1);
}

.chart-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-gray);
}

/* Alerts */
.alert-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 16px;
}

.alert-item.success {
  background: rgba(139,195,74,0.05);
  border: 1px solid rgba(139,195,74,0.2);
}

.alert-item.success i {
  color: var(--primary-green);
  font-size: 20px;
}

.alert-item.info {
  background: rgba(33,150,243,0.05);
  border: 1px solid rgba(33,150,243,0.2);
}

.alert-item.info i {
  color: #2196F3;
  font-size: 20px;
}

.alert-item strong {
  display: block;
  font-size: 14px;
  color: var(--text-dark);
  margin-bottom: 4px;
}

.alert-item p {
  font-size: 13px;
  color: var(--text-gray);
  line-height: 1.4;
}

.quick-action-btn {
  width: 100%;
  padding: 14px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-dark);
  cursor: pointer;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  transition: all 0.2s;
}

.quick-action-btn:hover {
  background: var(--bg-light);
  border-color: #ccc;
}

@media (max-width: 1024px) {
  .status-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .panels-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .status-grid {
    grid-template-columns: 1fr;
  }
  .dashboard-header .dashboard-inner {
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
  }
}
</style>
