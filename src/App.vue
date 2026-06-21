<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import ScrollToTop from './components/ScrollToTop.vue'
import SolutionModal from './components/SolutionModal.vue'
import AuthModal from './components/AuthModal.vue'
import { provide, ref } from 'vue'

const isModalActive = ref(false)
const modalData = ref(null)

const openModal = (data) => {
  modalData.value = data
  isModalActive.value = true
}

const closeModal = () => {
  isModalActive.value = false
}

provide('modalControl', {
  openModal,
  closeModal,
  isModalActive,
  modalData
})

const isAuthModalActive = ref(false)
const openAuthModal = () => { isAuthModalActive.value = true }
const closeAuthModal = () => { isAuthModalActive.value = false }
provide('authModalControl', {
  openAuthModal,
  closeAuthModal,
  isAuthModalActive
})
</script>

<template>
  <Header />
  <router-view />
  <Footer />
  <SolutionModal />
  <AuthModal />
  <ScrollToTop />
</template>
