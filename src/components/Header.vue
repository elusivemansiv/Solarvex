<script setup>
import { ref, watch, inject } from 'vue'
import { useRoute } from 'vue-router'

const isMobileMenuOpen = ref(false)
const route = useRoute()
const { openAuthModal } = inject('authModalControl')

const toggleMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

// Close menu when route changes
watch(route, () => {
  isMobileMenuOpen.value = false
})
</script>

<template>
  <header class="header">
    <div class="header-inner">
      <router-link to="/" class="logo">
        <div class="logo-icon">
          <i class="fas fa-sun"></i>
        </div>
        SOLAR VEX
      </router-link>
      <nav 
        class="nav" 
        :style="isMobileMenuOpen ? {
          display: 'flex',
          position: 'absolute',
          top: '70px',
          left: '0',
          right: '0',
          background: 'white',
          flexDirection: 'column',
          padding: '20px',
          boxShadow: '0 10px 30px rgba(0,0,0,0.1)'
        } : {}"
      >
        <router-link to="/about">About Solar Vex</router-link>
        <router-link to="/solutions">Solutions</router-link>
        <router-link to="/products">Products</router-link>
        <router-link to="/cases">Cases</router-link>
        <router-link to="/community">Community</router-link>
        <router-link to="/support">Support & Contact</router-link>
      </nav>
      <div class="nav-icons">
        <a href="#" @click.prevent="openAuthModal"><i class="fas fa-user"></i></a>
      </div>
      <button class="mobile-menu-btn" @click="toggleMenu">
        <i class="fas fa-bars"></i>
      </button>
    </div>
  </header>
</template>
