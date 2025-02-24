import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: localStorage.getItem('isAuthenticated') === 'true' || false,
    accessToken: localStorage.getItem('accessToken') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
  }),
  getters: {
    getIsAuthenticated: (state) => state.isAuthenticated,
    getAccessToken: (state) => state.accessToken,
    getRefreshToken: (state) => state.refreshToken,
  },
  actions: {
    setIsAuthenticated(value) {
      this.isAuthenticated = value
      localStorage.setItem('isAuthenticated', value)
    },
    setAccessToken(token) {
      this.accessToken = token
      localStorage.setItem('accessToken', token)
    },
    setRefreshToken(token) {
      this.refreshToken = token
      localStorage.setItem('refreshToken', token)
    },
    clearAuthentication() {
      this.isAuthenticated = false
      this.accessToken = null
      this.refreshToken = null
      localStorage.removeItem('isAuthenticated')
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
    },
  },
})
