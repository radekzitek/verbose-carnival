<template>
  <MDBContainer fluid>
    <MDBRow class="align-items-center m-2">
      <MDBCol md="2">
        <img src="../assets/carnival.png" />
      </MDBCol>
      <MDBCol md="8">
        <Menubar :model="items" />
      </MDBCol>
      <MDBCol md="2">
        <MDBBtn color="primary" rounded>Login</MDBBtn>
      </MDBCol>
    </MDBRow>
  </MDBContainer>
</template>

<script setup>
import Menubar from 'primevue/menubar'
import { MDBCol, MDBRow, MDBContainer, MDBBtn } from 'mdb-vue-ui-kit'

const items = [
  {
    label: 'File',
    items: [
      { label: 'New', icon: 'pi pi-fw pi-plus' },
      { label: 'Open', icon: 'pi pi-fw pi-folder-open' },
      { separator: true },
      { label: 'Quit', icon: 'pi pi-fw pi-times' },
    ],
  },
  {
    label: 'Edit',
    items: [
      { label: 'Cut', icon: 'pi pi-fw pi-copy' },
      { label: 'Copy', icon: 'pi pi-fw pi-clone' },
      { label: 'Paste', icon: 'pi pi-fw pi-exclamation-triangle' },
    ],
  },
  {
    label: 'Options',
    items: [
      {
        label: 'Home',
        to: '/',
      },
      {
        label: 'About',
        to: '/about',
      },
      {
        label: 'Contact',
        to: '/contact',
      },
    ],
  },
]
</script>

<style scoped></style>
