<script setup>
import { inject } from 'vue'

const { isModalActive, closeModal, modalData } = inject('modalControl')
</script>

<template>
  <div class="modal" :class="{ active: isModalActive }" @click.self="closeModal">
    <div class="modal-content" style="max-width: 500px;" v-if="modalData">
      <button class="modal-close" @click="closeModal">&times;</button>
      <h3 style="font-size: 20px; color: var(--dark-blue); margin-bottom: 6px;">{{ modalData.title }}</h3>
      <p style="font-size: 13px; color: var(--primary-green-dark); font-weight: 600; margin-bottom: 16px;">{{ modalData.subtitle }}</p>
      
      <img :src="modalData.image" alt="Solution Image" style="width: 100%; height: 180px; object-fit: cover; border-radius: 12px; margin-bottom: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
      
      <p style="color: var(--text-gray); font-size: 13px; line-height: 1.5; margin-bottom: 16px;">{{ modalData.description }}</p>
      
      <div style="margin-bottom: 20px;">
        <h4 style="font-size: 13px; font-weight: 700; color: var(--dark-blue); margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.5px;">Key Specifications & Features</h4>
        <ul style="list-style: none; display: grid; grid-template-columns: 1fr; gap: 10px;">
          <li v-for="spec in modalData.specs" :key="spec" style="font-size: 12px; color: var(--text-dark); font-weight: 500; display: flex; align-items: center; gap: 8px;">
            <i class="fas fa-check-circle" style="color: var(--primary-green);"></i> {{ spec }}
          </li>
        </ul>
      </div>
      
      <div style="display: flex; gap: 12px; justify-content: flex-end; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px;">
        <router-link to="/solutions" class="btn-solid" style="padding: 10px 24px; font-size: 13px; text-decoration: none;" @click="closeModal">Learn More Solutions</router-link>
        <button class="btn-outline" @click="closeModal" style="padding: 10px 24px; font-size: 13px;">Close</button>
      </div>
    </div>
  </div>
</template>
