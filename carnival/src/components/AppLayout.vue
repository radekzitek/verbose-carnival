<template>
  <MDBContainer fluid>
    <MDBRow>
      <AppHeader />
    </MDBRow>

    <MDBRow>
      <MDBCol md="2">
        <AppSidebar />
      </MDBCol>
      <MDBCol md="10">
        <AppMain />
      </MDBCol>
    </MDBRow>

    <MDBRow>
      <AppFooter />
    </MDBRow>
  </MDBContainer>
</template>

<script setup>
import { MDBCol, MDBRow, MDBContainer } from 'mdb-vue-ui-kit'
import AppHeader from './AppHeader.vue'
import AppSidebar from './AppSidebar.vue'
import AppFooter from './AppFooter.vue'
import AppMain from './AppMain.vue'
</script>

<style scoped></style>
