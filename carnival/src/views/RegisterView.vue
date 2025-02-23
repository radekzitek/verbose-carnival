<template>
  <MDBContainer class="d-flex justify-content-center mt-5">
    <MDBCol md="6">
      <MDBCard class="border-primary border">
        <MDBCardHeader class="border-primary">
          <h5 class="mb-0 text-center">Register</h5>
        </MDBCardHeader>
        <MDBCardBody>
          <form @submit.prevent="handleSubmit">
            <MDBRow>
              <MDBCol md="6">
                <MDBInput
                  label="First Name"
                  type="text"
                  v-model="firstName"
                  required
                  class="mb-4"
                  autocomplete="given-name"
                />
              </MDBCol>
              <MDBCol md="6">
                <MDBInput
                  label="Last Name"
                  type="text"
                  v-model="lastName"
                  required
                  class="mb-4"
                  autocomplete="family-name"
                />
              </MDBCol>
            </MDBRow>
            <MDBInput
              label="Email"
              type="email"
              v-model="email"
              required
              class="mb-4"
              autocomplete="email"
            />
            <MDBRow>
              <MDBCol md="6">
                <MDBInput
                  label="Password"
                  type="password"
                  v-model="password"
                  required
                  class="mb-4"
                  autocomplete="new-password"
                />
              </MDBCol>
              <MDBCol md="6">
                <MDBInput
                  label="Verify Password"
                  type="password"
                  v-model="verifyPassword"
                  required
                  class="mb-4"
                  autocomplete="new-password"
              /></MDBCol>
            </MDBRow>
            <MDBBtn color="primary" block class="mb-4" type="submit">Register</MDBBtn>
          </form>
          <MDBBtn color="secondary" block @click="cancelRegistration">Cancel</MDBBtn>
          <p v-if="error" class="text-danger text-center">{{ error }}</p>
        </MDBCardBody>
      </MDBCard>
    </MDBCol>
  </MDBContainer>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {
  MDBContainer,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBInput,
  MDBBtn,
  MDBCardHeader,
  MDBRow,
} from 'mdb-vue-ui-kit'

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
