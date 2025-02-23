<template>
  <MDBContainer>
    <MDBRow class="fs-5 fw-bold">References:</MDBRow>
    <MDBRow v-for="(item, index) in sidebarItems" :key="index">
      <MDBCol md="2" class="d-flex align-items-center justify-content-center">
        <img :src="item.image" alt="Image" class="img-fluid" style="max-width: 32px; max-height: 32px" />
      </MDBCol>
      <MDBCol md="10">
        <a :href="item.url" target="_blank">
          <div class="fw-bold">
            {{ item.oline }}
            <br />
          </div>
        </a>
        <div class="text-secondary" style="font-size: 0.8rem">
          {{ item.uline }}
        </div>
      </MDBCol>
    </MDBRow>
  </MDBContainer>
</template>

<script setup>
import { ref } from 'vue';
import vueLogo from '../assets/vue.svg';
import vueCliLogo from '../assets/vue.svg';
import vueRouterLogo from '../assets/vue.svg';
import piniaLogo from '../assets/pinia.png';
import viteLogo from '../assets/vite.svg';
import bootstrapLogo from '../assets/bootstrap.svg';
import mdbVueLogo from '../assets/mdb-vue.png';
import { MDBContainer, MDBRow, MDBCol } from 'mdb-vue-ui-kit';

const sidebarItems = ref([
  {
    oline: 'Vue.js',
    uline: 'The Progressive JavaScript Framework',
    image: vueLogo,
    url: 'https://vuejs.org/',
  },
  {
    oline: 'Vue CLI',
    uline: 'Standard Tooling for Vue.js Development',
    image: vueCliLogo,
    url: 'https://cli.vuejs.org/',
  },
  {
    oline: 'Vue Router',
    uline: 'The official router for Vue.js',
    image: vueRouterLogo,
    url: 'https://router.vuejs.org/',
  },
  {
    oline: 'Pinia',
    uline: 'Intuitive, type safe, light and flexible Store for Vue 3',
    url: 'https://pinia.esm.dev/',
    image: piniaLogo,
  },
  {
    oline: 'Vite',
    uline: 'Next Generation Frontend Tooling',
    url: 'https://vitejs.dev/',
    image: viteLogo,
  },
  {
    oline: 'Bootstrap',
    uline: 'The most popular HTML, CSS, and JS library in the world',
    url: 'https://getbootstrap.com/',
    image: bootstrapLogo,
  },
  {
    oline: 'MDB for Vue',
    uline: 'Material Design for Bootstrap',
    url: 'https://mdbootstrap.com/docs/vue/',
    image: mdbVueLogo,
  },
]);
</script>

<style scoped lang="scss"></style>
