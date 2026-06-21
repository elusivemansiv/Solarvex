<script setup>
import { ref, onMounted } from 'vue'

const activeTab = ref('login')

const switchForm = (tab) => {
  activeTab.value = tab
}

const handleLoginSubmit = (e) => {
  e.preventDefault();
  alert('Welcome to Solar Vex! Login successful.');
}

const handleRegisterSubmit = (e) => {
  e.preventDefault();
  alert('Registration successful! Please check your email.');
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
    <!-- Login/Register Card Wrapper -->
    <section class="login-wrapper">
      <div class="login-container glass-card fade-in visible">
        <div class="login-tabs">
          <button :class="['login-tab-btn', { active: activeTab === 'login' }]" @click="switchForm('login')">Sign In</button>
          <button :class="['login-tab-btn', { active: activeTab === 'register' }]" @click="switchForm('register')">Register</button>
        </div>

        <!-- Login Form -->
        <div class="login-form-panel" :class="{ active: activeTab === 'login' }" v-show="activeTab === 'login'">
          <h3 style="font-size: 24px; color: var(--dark-blue); margin-bottom: 8px; font-weight: 800;">Welcome Back</h3>
          <p style="color: var(--text-gray); font-size: 13px; margin-bottom: 24px;">Sign in to access your Solar Vex dashboards and system logs.</p>
          
          <form @submit="handleLoginSubmit">
            <div class="form-group">
              <label>Email Address</label>
              <input type="email" class="form-control" placeholder="john@example.com" required>
            </div>
            <div class="form-group">
              <label>Password</label>
              <input type="password" class="form-control" placeholder="••••••••" required>
            </div>
            <a href="#" class="forgot-link" @click.prevent="alert('Password reset link sent to your email.')">Forgot Password?</a>
            <button type="submit" class="btn-solid" style="width: 100%; padding: 12px;">Sign In</button>
          </form>
        </div>

        <!-- Register Form -->
        <div class="login-form-panel" :class="{ active: activeTab === 'register' }" v-show="activeTab === 'register'">
          <h3 style="font-size: 24px; color: var(--dark-blue); margin-bottom: 8px; font-weight: 800;">Create Account</h3>
          <p style="color: var(--text-gray); font-size: 13px; margin-bottom: 24px;">Register to configure your solar arrays and check system warranty logs.</p>
          
          <form @submit="handleRegisterSubmit">
            <div class="form-group">
              <label>Full Name</label>
              <input type="text" class="form-control" placeholder="John Doe" required>
            </div>
            <div class="form-group">
              <label>Email Address</label>
              <input type="email" class="form-control" placeholder="john@example.com" required>
            </div>
            <div class="form-group">
              <label>Password</label>
              <input type="password" class="form-control" placeholder="••••••••" required>
            </div>
            <div class="form-group" style="display: flex; align-items: center; gap: 8px;">
              <input type="checkbox" id="termsAgree" required>
              <label for="termsAgree" style="margin-bottom: 0;">I agree to the Terms of Service & Privacy Policy</label>
            </div>
            <button type="submit" class="btn-solid" style="width: 100%; padding: 12px;">Register</button>
          </form>
        </div>
      </div>
    </section>
  </main>
</template>
