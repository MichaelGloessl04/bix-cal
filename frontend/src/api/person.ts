import axios from 'axios'

import type { Person, PersonNoID } from '@/api/types/person'

export async function getPersons(search_term: string | undefined = undefined): Promise<Person[]> {
  const params: Record<string, string> = {}
  if (search_term) {
    params['search_term'] = search_term
  }

  const response = await axios.get('/api/person', { params: params })
  return response.data
}

export async function getPerson(id: number): Promise<Person> {
  const response = await axios.get(`/api/person/${id}`)
  return response.data
}

export async function createPerson(person: PersonNoID): Promise<Person> {
  const response = await axios.post('/api/person', person)
  return response.data
}
