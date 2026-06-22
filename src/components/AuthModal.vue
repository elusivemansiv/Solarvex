<script setup>
import { inject, ref } from 'vue'
import { useRouter } from 'vue-router'

const { isAuthModalActive, closeAuthModal } = inject('authModalControl')
const activeTab = ref('login')
const router = useRouter()

const switchForm = (tab) => {
  activeTab.value = tab
}

const handleLoginSubmit = (e) => {
  e.preventDefault();
  alert('Welcome to Solar Vex! Login successful.');
  closeAuthModal();
  router.push('/dashboard');
}

const handleRegisterSubmit = (e) => {
  e.preventDefault();
  alert('Registration successful! Please check your email.');
  closeAuthModal();
  router.push('/dashboard');
}
</script>

<template>
  <div class="modal" :class="{ active: isAuthModalActive }" @click.self="closeAuthModal">
    <div class="modal-content">
      <button class="modal-close" @click="closeAuthModal">&times;</button>
      
      <div class="login-tabs" style="margin-bottom: 24px;">
        <button :class="['login-tab-btn', { active: activeTab === 'login' }]" @click="switchForm('login')">Sign In</button>
        <button :class="['login-tab-btn', { active: activeTab === 'register' }]" @click="switchForm('register')">Register</button>
      </div>

      <!-- Login Form -->
      <div v-show="activeTab === 'login'">
        <h3 style="font-size: 24px; color: var(--dark-blue); margin-bottom: 8px; font-weight: 800;">Welcome Back</h3>
        <p style="color: var(--text-gray); font-size: 13px; margin-bottom: 24px;">Sign in to access your Solar Vex dashboards.</p>
        <form @submit="handleLoginSubmit">
          <div class="form-group">
            <label>Email Address</label>
            <input type="email" class="form-control" placeholder="john@example.com" required>
          </div>
          <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" placeholder="••••••••" required>
          </div>
          <a href="#" class="forgot-link" @click.prevent="alert('Password reset link sent.')">Forgot Password?</a>
          <button type="submit" class="btn-solid" style="width: 100%; padding: 12px; margin-top: 10px;">Sign In</button>
        </form>
      </div>

      <!-- Register Form -->
      <div v-show="activeTab === 'register'">
        <h3 style="font-size: 24px; color: var(--dark-blue); margin-bottom: 8px; font-weight: 800;">Create Account</h3>
        <p style="color: var(--text-gray); font-size: 13px; margin-bottom: 24px;">Register to configure your solar arrays.</p>
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
            <input type="checkbox" id="modalTermsAgree" required>
            <label for="modalTermsAgree" style="margin-bottom: 0;">I agree to the Terms of Service</label>
          </div>
          <button type="submit" class="btn-solid" style="width: 100%; padding: 12px; margin-top: 10px;">Register</button>
        </form>
      </div>

    </div>
  </div>
</template>
