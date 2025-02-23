<template>
  <div class="d-flex justify-content-center container mt-5">
    <div class="col-md-4">
      <div class="card border-primary border">
        <div class="card-header border-primary">
          <h5 class="card-title fs-5 fw-bold mb-0 text-center">Login</h5>
        </div>
        <div class="card-body">
          <form @submit.prevent="handleSubmit">
            <div class="mb-4">
              <label for="email" class="form-label">Email</label>
              <input
                type="email"
                class="form-control form-control-lg"
                id="email"
                v-model="email"
                required
              />
            </div>
            <div class="mb-4">
              <label for="password" class="form-label">Password</label>
              <input
                type="password"
                class="form-control form-control-lg"
                id="password"
                v-model="password"
                required
              />
            </div>
            <div class="mb-4">
              <router-link to="/forgot-password">Forgot Password?</router-link>
            </div>
            <button type="submit" class="btn btn-primary btn-block mb-4">Login</button>
          </form>
          <button type="button" class="btn btn-secondary btn-block" @click="cancelLogin">
            Cancel
          </button>
          <p v-if="error" class="text-danger text-center">{{ error }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/authStore'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const authStore = useAuthStore()

const handleSubmit = async () => {
  try {
    // Simulate API call
    if (email.value === 'test@example.com' && password.value === 'password') {
      authStore.setIsAuthenticated(true)
      router.push('/') // Redirect to home page
    } else {
      error.value = 'Invalid credentials'
    }
  } catch (err) {
    error.value = 'An error occurred: ' + err.message
  }
}

const cancelLogin = () => {
  router.push('/') // Redirect to home page
}
</script>

<style scoped></style>
