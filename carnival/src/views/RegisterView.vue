<template>
  <div class="d-flex justify-content-center container mt-5">
    <div class="col-md-6">
      <div class="card border-primary border">
        <div class="card-header border-primary">
          <h5 class="mb-0 text-center">Register</h5>
        </div>
        <div class="card-body">
          <form @submit.prevent="handleSubmit">
            <div class="row">
              <div class="col-md-6">
                <div class="mb-4">
                  <label for="firstName" class="form-label">First Name</label>
                  <input
                    type="text"
                    class="form-control form-control-lg"
                    id="firstName"
                    v-model="firstName"
                    required
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="mb-4">
                  <label for="lastName" class="form-label">Last Name</label>
                  <input
                    type="text"
                    class="form-control form-control-lg"
                    id="lastName"
                    v-model="lastName"
                    required
                  />
                </div>
              </div>
            </div>
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
            <div class="row">
              <div class="col-md-6">
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
              </div>
              <div class="col-md-6">
                <div class="mb-4">
                  <label for="verifyPassword" class="form-label">Verify Password</label>
                  <input
                    type="password"
                    class="form-control form-control-lg"
                    id="verifyPassword"
                    v-model="verifyPassword"
                    required
                  />
                </div>
              </div>
            </div>
            <button type="submit" class="btn btn-primary btn-block mb-4">Register</button>
          </form>
          <button type="button" class="btn btn-secondary btn-block" @click="cancelRegistration">
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

const firstName = ref('')
const lastName = ref('')
const email = ref('')
const password = ref('')
const verifyPassword = ref('')
const error = ref('')
const router = useRouter()

const handleSubmit = async () => {
  if (password.value !== verifyPassword.value) {
    error.value = 'Passwords do not match'
    return
  }

  // Simulate API call
  try {
    // Registration logic here (e.g., API call)
    console.log('Registration data:', {
      firstName: firstName.value,
      lastName: lastName.value,
      email: email.value,
      password: password.value,
    })

    // Redirect to login page after successful registration
    router.push('/login')
  } catch (err) {
    error.value = 'Registration failed: ' + err.message
  }
}

const cancelRegistration = () => {
  router.push('/') // Redirect to home page
}
</script>
