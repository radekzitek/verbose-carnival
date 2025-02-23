<template>
  <MDBContainer class="d-flex justify-content-center mt-5">
    <MDBCol md="4">
      <MDBCard class="border-primary border">
        <MDBCardHeader class="border-primary">
          <h5 class="card-title fs-5 fw-bold mb-0 text-center">Login</h5>
        </MDBCardHeader>
        <MDBCardBody>
          <form @submit.prevent="handleSubmit">
            <MDBInput label="Email" type="email" v-model="email" required class="mb-4" autocomplete="email" />
            <MDBInput
              label="Password"
              type="password"
              v-model="password"
              required
              class="mb-4"
              autocomplete="current-password"
            />
            <div class="text-center">
              <router-link to="/forgot-password">Forgot Password?</router-link>
            </div>

            <MDBBtn color="primary" class="mt-4" block type="submit">Login</MDBBtn>
          </form>
          <MDBBtn color="secondary" block @click="cancelLogin">Cancel</MDBBtn>
          <p v-if="error" class="text-danger mt-3 text-center">{{ error }}</p>
        </MDBCardBody>
      </MDBCard>
    </MDBCol>
  </MDBContainer>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/authStore'
import {
  MDBContainer,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBInput,
  MDBBtn,
  MDBCardHeader,
} from 'mdb-vue-ui-kit'

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
