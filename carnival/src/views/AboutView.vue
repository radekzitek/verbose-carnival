<template>
  <MDBContainer className="mt-5">
    <MDBRow>
      <MDBCol lg="8" offset-lg="2">
        <h1 class="mb-4">About Us</h1>
        <p class="lead">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt
          ut labore et dolore magna aliqua.
        </p>
        <p>
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt
          ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
          ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <router-link to="/contact" class="btn btn-primary">Contact Us</router-link>
      </MDBCol>
    </MDBRow>
  </MDBContainer>
</template>

<script setup>
import { MDBContainer, MDBRow, MDBCol } from 'mdb-vue-ui-kit'
</script>
