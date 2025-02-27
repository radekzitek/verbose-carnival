<template>
  <MDBContainer class="d-flex justify-content-center align-items-center bg-light mt-5">
    <MDBCol md="8" lg="6" xl="5">
      <MDBCard>
        <MDBCardBody class="text-center">
          <h1 class="display-1 fw-bold text-primary">404</h1>
          <p class="lead">The page you’re looking for doesn’t exist.</p>
          <router-link to="/" class="btn btn-primary">Go Home</router-link>
        </MDBCardBody>
      </MDBCard>
    </MDBCol>
  </MDBContainer>
</template>

<script setup>
import { MDBContainer, MDBCol, MDBCard, MDBCardBody } from 'mdb-vue-ui-kit'
</script>

<style scoped>
/* Add any component-specific styles here */
.bg-light {
  background-color: #f8f9fa; /* Bootstrap's light background color */
}
</style>
