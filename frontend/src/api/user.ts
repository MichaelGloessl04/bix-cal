import axios from 'axios'

import type { User, UserNoID } from '@/api/types/user'
import type { Rating } from './types/rating'

export async function getUser(id: number): Promise<User> {
  const response = await axios.get(`/api/user/${id}`)
  return response.data
}

export async function getUserByEmail(email: string): Promise<User> {
  const response = await axios.get(`/api/user/email/${email}`)
  return response.data
}

export async function createUser(user: UserNoID): Promise<User> {
  const response = await axios.post('/api/user', user)
  return response.data
}

export async function getUserPersonRating(user_id: number, person_id: number): Promise<Rating> {
  const response = await axios.get(`/api/user/rating/${user_id}/${person_id}`)
  return response.data
}
