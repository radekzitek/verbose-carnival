import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: localStorage.getItem('isAuthenticated') === 'true' || false,
  }),
  getters: {
    getIsAuthenticated: (state) => state.isAuthenticated,
  },
  actions: {
    setIsAuthenticated(value) {
      this.isAuthenticated = value
      localStorage.setItem('isAuthenticated', value)
    },
    clearAuthentication() {
      this.isAuthenticated = false
      localStorage.removeItem('isAuthenticated')
    }
  },
})
