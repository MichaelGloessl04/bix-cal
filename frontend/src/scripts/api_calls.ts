import axios from 'axios'

import type { Person } from '@/types/person'
import type { Scores } from '@/types/scores'


export function getPersons(): Promise<Person[]> {
  console.log('getting persons')
  return axios.get('/api/person')
    .then(response => response.data)
    .catch(() => console.log('error'))
    .finally(() => console.log('done'))
}


export function getPerson(id: number): Promise<Person> {
  console.log(`getting person ${id}`)
  return axios.get(`/api/person/${id}`)
    .then(response => response.data)
    .catch(() => console.log('error'))
    .finally(() => console.log('done'))
}


export function getScore(person_id: number): Promise<Scores> {
  console.log(`getting score for person ${person_id}`)
  return axios.get(`/api/person/${person_id}/score/`)
    .then(response => response.data)
    .catch(() => console.log('error'))
    .finally(() => console.log('done'))
}
