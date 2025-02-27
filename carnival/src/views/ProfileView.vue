<template>
  <MDBContainer class="d-flex justify-content-center mt-5">
    <MDBCol md="6">
      <MDBCard class="border-primary border">
        <MDBCardHeader class="border-primary">
          <h5 class="mb-0 text-center">Update Profile</h5>
        </MDBCardHeader>
        <MDBCardBody>
          <form @submit.prevent="handleSubmit">
            <MDBInput
              label="Username"
              type="text"
              v-model="username"
              required
              class="mb-4"
              autocomplete="username"
              disabled
            />
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
            <MDBBtn color="primary" block class="mb-4" type="submit">Update</MDBBtn>
          </form>
          <MDBBtn color="secondary" block @click="cancelUpdate">Cancel</MDBBtn>
          <p v-if="error" class="text-danger text-center">{{ error }}</p>
        </MDBCardBody>
      </MDBCard>
    </MDBCol>
  </MDBContainer>
</template>

<script setup>
import { ref, onMounted } from 'vue'
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
import { useUser } from '@/composables/useUser'

const username = ref('')
const firstName = ref('')
const lastName = ref('')
const email = ref('')
const error = ref('')
const router = useRouter()
const { getUserProfile, updateUserProfile } = useUser()

onMounted(async () => {
  try {
    const profile = await getUserProfile()
    username.value = profile.username
    firstName.value = profile.first_name
    lastName.value = profile.last_name
    email.value = profile.email
  } catch (err) {
    error.value = 'Failed to load profile: ' + err.message
  }
})

const handleSubmit = async () => {
  try {
    await updateUserProfile({
      first_name: firstName.value,
      last_name: lastName.value,
      email: email.value,
    })

    router.push('/profile')
  } catch (err) {
    error.value = 'Update failed: ' + err.message
  }
}

const cancelUpdate = () => {
  router.push('/') // Redirect to home page
}
</script>
