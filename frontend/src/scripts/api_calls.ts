import axios from 'axios'

import type { Person, PersonNoID } from '@/types/person'
import type { Scores } from '@/types/scores'
import type { User } from '@/types/user'


export function getPersons(): Promise<Person[]> {
  console.log('getting persons')
  return axios.get('/api/person')
    .then(response => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}


export function getPerson(id: number): Promise<Person> {
  console.log(`getting person ${id}`)
  return axios.get(`/api/person/${id}`)
    .then(response => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}


export function getScore(person_id: number): Promise<Scores> {
  console.log(`getting score for person ${person_id}`)
  return axios.get(`/api/person/${person_id}/score/`)
    .then(response => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}


export function addPerson(person: PersonNoID): Promise<Person> {
  console.log(`adding person ${person.name}`)
  return axios.post('/api/person', person)
    .then(response => response.data)
    .catch((error) => console.log(error))
    .finally(() => console.log('done'))
}


export function getUser(username: string, password: string): Promise<User> {
  console.log(`getting user ${username}`)
  const params: { [key: string]: string } = {}
  params["username"] = username
  params["password"] = password
  return axios.get('/api/user', { params: params })
    .then(response => response.data)
    .finally(() => console.log('done'))
}
