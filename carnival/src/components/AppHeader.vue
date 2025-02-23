<template>
  <MDBContainer class="p-3">
    <MDBRow class="align-items-center">
      <MDBCol md="2" class="d-flex justify-content-left">
        <img src="../assets/carnival.png" />
      </MDBCol>
      <MDBCol md="6" class="d-flex justify-content-left">
        <MDBBtn tag="a" color="secondary" rounded href="/">
          <MDBIcon iconStyle="fas" icon="home"></MDBIcon> Home
        </MDBBtn>
        <MDBBtn tag="a" color="secondary" rounded href="/">
          <MDBIcon iconStyle="fas" icon="info-circle"></MDBIcon> About
        </MDBBtn>
      </MDBCol>
      <MDBCol md="4" class="d-flex justify-content-end">
        <MDBBtn tag="a" color="secondary" rounded href="/settings">
          <MDBIcon iconStyle="fas" icon="cogs"></MDBIcon>
        </MDBBtn>
        <MDBBtn tag="a" color="secondary" rounded href="/profile">
          <MDBIcon iconStyle="fas" icon="user-circle"></MDBIcon>
        </MDBBtn>
        <MDBBtn tag="a" color="secondary" rounded href="/login">
          <MDBIcon iconStyle="fas" icon="sign-in-alt"></MDBIcon> Login
        </MDBBtn>
        <MDBBtn tag="a" color="secondary" rounded href="/logout">
          <MDBIcon iconStyle="fas" icon="sign-out-alt"></MDBIcon> Logout
        </MDBBtn>
        <MDBBtn tag="a" color="secondary" rounded href="/register">
          <MDBIcon iconStyle="fas" icon="user-plus"></MDBIcon> Register
        </MDBBtn>
      </MDBCol>
    </MDBRow>
  </MDBContainer>
</template>

<script setup>
import { MDBCol, MDBRow, MDBContainer, MDBBtn, MDBIcon } from 'mdb-vue-ui-kit'
</script>

<style scoped></style>
