import { ref, getCurrentInstance } from 'vue'
import axios from 'axios'
import { useAuthStore } from '@/stores/authStore'
import { useAuth } from './useAuth'

export function useUser() {
  const error = ref('')
  const instance = getCurrentInstance()
  const $log = instance.appContext.config.globalProperties.$log
  const authStore = useAuthStore()
  const { refreshToken } = useAuth()

  const registerUser = async (userData) => {
    try {
      $log.debug('useUser: Registering user with data:', {
        username: userData.username,
        first_name: userData.first_name,
        last_name: userData.last_name,
        email: userData.email,
      })
      const response = await axios.post('http://localhost:8000/users/register/', userData)
      $log.info('useUser: User registered successfully:', response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data?.error || 'Registration failed'
      $log.error('useUser: Registration failed:', err, err.response)
      throw err
    }
  }

  const getUserProfile = async () => {
    try {
      $log.debug('useUser: Fetching user profile')
      let accessToken = authStore.getAccessToken

      if (!accessToken) {
        $log.debug('useUser: Access token not found, refreshing...')
        try {
          const newAccessToken = await refreshToken()
          if (newAccessToken) {
            accessToken = newAccessToken
            $log.debug('useUser: New access token: ' + accessToken)
          } else {
            $log.error('useUser: Failed to refresh token, authentication required')
            throw new Error('Authentication required')
          }
        } catch (refreshError) {
          $log.error('useUser: Failed to refresh token:', refreshError)
          throw new Error('Could not refresh token')
        }
      }

      $log.debug('useUser: Access token found, sending request to /users/me/')
      const headers = {
        Authorization: `Bearer ${accessToken}`,
      }
      $log.debug('useUser: Request headers:', headers) // Log the headers

      const response = await axios.get('http://localhost:8000/users/me/', {
        headers: headers,
      })
      $log.info('useUser: User profile fetched successfully:', response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to fetch user profile'
      $log.error('useUser: Failed to fetch user profile:', err, err.response)
      throw err
    }
  }

  const updateUserProfile = async (profileData) => {
    try {
      $log.debug('useUser: Updating user profile with data:', profileData)
      let accessToken = authStore.getAccessToken

      if (!accessToken) {
        $log.debug('useUser: Access token not found, refreshing...')
        try {
          const newAccessToken = await refreshToken()
          if (newAccessToken) {
            accessToken = newAccessToken
          } else {
            throw new Error('Authentication required')
          }
        } catch (refreshError) {
          $log.error('useUser: Failed to refresh token:', refreshError)
          throw new Error('Could not refresh token')
        }
      }

      $log.debug('useUser: Access token found, sending request to /users/me/update/')

      const response = await axios.put('http://localhost:8000/users/me/update/', profileData, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      })
      $log.info('useUser: User profile updated successfully:', response.data)
      return response.data
    } catch (err) {
      error.value = err.response?.data?.error || 'Failed to update user profile'
      $log.error('useUser: Failed to update user profile:', err, err.response)
      throw err
    }
  }

  return {
    error,
    registerUser,
    getUserProfile,
    updateUserProfile,
  }
}
