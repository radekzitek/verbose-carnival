<template>
  <MDBContainer class="p-3">
    <MDBRow class="align-items-center">
      <MDBCol md="2" class="d-flex justify-content-start">
        <img src="../assets/carnival.png" alt="Carnival Logo" class="img-fluid" />
      </MDBCol>
      <MDBCol md="6" class="d-flex justify-content-start">
        <MDBBtn tag="router-link" color="primary" to="/" class="me-2">
          <MDBIcon icon="home" fas class="me-2" /> Home
        </MDBBtn>
        <MDBBtn tag="router-link" color="primary" to="/about" class="me-2">
          <MDBIcon icon="info-circle" fas class="me-2" /> About
        </MDBBtn>
      </MDBCol>
      <MDBCol md="4" class="d-flex justify-content-end">
        <MDBBtn tag="router-link" color="primary" to="/settings" class="me-2">
          <MDBIcon icon="cogs" fas />
        </MDBBtn>
        <MDBBtn
          v-if="authStore.isAuthenticated"
          tag="router-link"
          color="primary"
          to="/profile"
          class="me-2"
        >
          <MDBIcon icon="user-circle" fas />
        </MDBBtn>
        <MDBBtn
          v-if="!authStore.isAuthenticated"
          tag="router-link"
          color="primary"
          to="/login"
          class="me-2"
        >
          <MDBIcon icon="sign-in-alt" fas class="me-2" /> Login
        </MDBBtn>
        <MDBBtn v-if="authStore.isAuthenticated" color="primary" class="me-2" @click="logout">
          <MDBIcon icon="sign-out-alt" fas class="me-2" /> Logout
        </MDBBtn>
        <MDBBtn
          v-if="!authStore.isAuthenticated"
          tag="router-link"
          class="me-2"
          color="primary"
          to="/register"
        >
          <MDBIcon icon="user-plus" fas class="me-2" /> Register
        </MDBBtn>
      </MDBCol>
    </MDBRow>
  </MDBContainer>
</template>

<script setup>
import { useAuthStore } from '../stores/authStore'
import { useAuth } from '../composables/useAuth'
import { MDBContainer, MDBRow, MDBCol, MDBBtn, MDBIcon } from 'mdb-vue-ui-kit'

const authStore = useAuthStore()
const { logout } = useAuth()
</script>

<style scoped lang="scss"></style>
