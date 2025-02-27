import { ref, getCurrentInstance } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/authStore'
import axios from 'axios'

export function useAuth() {
  const error = ref('')
  const router = useRouter()
  const authStore = useAuthStore()
  const instance = getCurrentInstance()
  const $log = instance.appContext.config.globalProperties.$log

  const login = async (username, password) => {
    error.value = ''
    try {
      $log.debug('useAuth: Attempting login with username:', username)
      const response = await axios.post(
        'http://localhost:8000/oauth/token/',
        {
          username: username,
          password: password,
        },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        },
      )

      if (response.status === 200) {
        $log.info('useAuth: Login successful for user:', username)
        authStore.setAccessToken(response.data.access_token)
        authStore.setRefreshToken(response.data.refresh_token)
        authStore.setIsAuthenticated(true)
        router.push('/') // Redirect to home page
      } else {
        $log.warn('useAuth: Login failed for user:', username, 'Error:', response.data.error)
        error.value = response.data.error || 'Invalid credentials'
      }
    } catch (err) {
      $log.error('useAuth: An error occurred during login:', err)
      error.value = 'An error occurred: ' + err.message
    }
  }

  const logout = async () => {
    error.value = ''
    try {
      $log.debug('useAuth: Attempting logout')
      const response = await axios.post(
        'http://localhost:8000/oauth/logout/',
        {},
        {
          headers: {
            'Content-Type': 'application/json',
          },
        },
      )

      if (response.status === 200) {
        $log.info('useAuth: Logout successful')
        authStore.clearAuthentication()
        router.push('/login')
      } else {
        $log.warn('useAuth: Logout failed:', response.status, response.statusText)
        error.value = 'Logout failed'
        // Handle logout failure (e.g., display an error message)
      }
    } catch (err) {
      $log.error('useAuth: An error occurred during logout:', err)
      error.value = 'An error occurred during logout: ' + err.message
      // Handle network errors or other exceptions
    }
  }

  const refreshToken = async () => {
    error.value = ''
    try {
      $log.debug('useAuth: Attempting token refresh')
      const refreshTokenValue = authStore.refreshToken
      if (!refreshTokenValue) {
        $log.warn('useAuth: No refresh token available')
        error.value = 'No refresh token available'
        return
      }

      const response = await axios.post(
        'http://localhost:8000/oauth/jwt/refresh/', // refresh endpoint
        { refresh_token: refreshTokenValue },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        },
      )

      if (response.status === 200) {
        $log.info('useAuth: Token refresh successful')
        authStore.setAccessToken(response.data.access_token)
        return response.data.access_token // Return the new access token
      } else {
        $log.warn('useAuth: Token refresh failed:', response.status, response.statusText)
        // If refresh fails, redirect to login
        authStore.clearAuthentication()
        router.push('/login')
        error.value = 'Token refresh failed: ' + (response.data.error || response.statusText)
      }
    } catch (err) {
      $log.error('useAuth: An error occurred during token refresh:', err)
      authStore.clearAuthentication()
      router.push('/login')
      error.value = 'An error occurred during token refresh: ' + err.message
    }
  }

  return { login, logout, error, refreshToken }
}
