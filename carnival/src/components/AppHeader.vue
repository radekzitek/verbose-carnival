<template>
  <div class="container p-3">
    <div class="row align-items-center">
      <div class="col-md-2 d-flex justify-content-start">
        <img src="../assets/carnival.png" alt="Carnival Logo" class="img-fluid" />
      </div>
      <div class="col-md-6 d-flex justify-content-start">
        <router-link to="/" class="btn btn-primary me-2">
          <i class="fas fa-home"></i> Home
        </router-link>
        <router-link to="/about" class="btn btn-primary me-2">
          <i class="fas fa-info-circle"></i> About
        </router-link>
      </div>
      <div class="col-md-4 d-flex justify-content-end">
        <router-link to="/settings" class="btn btn-primary me-2">
          <i class="fas fa-cogs"></i>
        </router-link>
        <router-link v-if="authStore.isAuthenticated" to="/profile" class="btn btn-primary me-2">
          <i class="fas fa-user-circle"></i>
        </router-link>
        <router-link v-if="!authStore.isAuthenticated" to="/login" class="btn btn-primary me-2">
          <i class="fas fa-sign-in-alt"></i> Login
        </router-link>
        <button v-if="authStore.isAuthenticated" class="btn btn-primary me-2" @click="logout">
          <i class="fas fa-sign-out-alt"></i> Logout
        </button>
        <router-link v-if="!authStore.isAuthenticated" to="/register" class="btn btn-primary">
          <i class="fas fa-user-plus"></i> Register
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/authStore'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const logout = () => {
  authStore.clearAuthentication()
  router.push('/login')
}
</script>

<style scoped lang="scss">
@use '../assets/styles/main.scss';
</style>
