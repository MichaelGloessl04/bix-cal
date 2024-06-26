import axios from 'axios'

import type { User, UserNoID } from '@/api/types/user'
import type { Entry } from './types/entry'

export function getUser(email: string): Promise<User> {
  console.log(`getting user ${email}`)
  return axios
    .get(`/api/user/${email}`)
    .then((response) => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}

export function getUserByID(id: number): Promise<User> {
  console.log(`getting user ${id}`)
  return axios
    .get(`/api/user/id/${id}`)
    .then((response) => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}

export function createUser(user: UserNoID): Promise<User> {
  console.log(`creating user ${user.username}`)
  return axios
    .post('/api/user', user)
    .then((response) => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}

export function getRating(user_id: number, person_id: number): Promise<Entry> {
  console.log(`getting rating for user ${user_id} and person ${person_id}`)
  return axios
    .get(`/api/user/id/${user_id}/entries/${person_id}`)
    .then((response) => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}

export function hasRated(user_id: number, person_id: number): Promise<boolean> {
  console.log(`checking if user ${user_id} has rated person ${person_id}`)
  let rated = false
  return getRating(user_id, person_id).then((entries) => {
    console.log('entries: ', entries)
    if (entries) {
      rated = true
    }
    return rated
  })
}
