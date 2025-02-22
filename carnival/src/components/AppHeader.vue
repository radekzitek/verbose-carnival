<template>
  <MDBContainer fluid>
    <MDBRow>
      <MDBCol md="3"> Carnival </MDBCol>
      <MDBCol md="9">
        <Menubar :model="items" />
      </MDBCol>
    </MDBRow>
  </MDBContainer>
</template>

<script setup>
import Menubar from 'primevue/menubar'
import { MDBCol, MDBRow, MDBContainer } from 'mdb-vue-ui-kit'

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

<style scoped>

</style>
