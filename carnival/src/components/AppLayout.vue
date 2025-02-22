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

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
  /* Stack header, main, and footer vertically */
  min-height: 100vh;
  /* Ensure the layout takes up full viewport height */
}

.app-main {
  display: flex;
  flex-grow: 1;
  /* Allow main section to expand to fill available space */
}

.app-content {
  flex-grow: 1;
  /* Allow content to expand to fill remaining space */
  padding: 1rem;
}
</style>
