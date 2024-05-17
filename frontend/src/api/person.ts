import axios from 'axios'

import type { Person, PersonNoID } from '@/api/types/person'
import type { Scores } from '@/api/types/scores'
import type { Entry } from '@/api/types/entry'


export function getPersons(): Promise<Person[]> {
    console.log('getting persons')
    return axios.get('/api/person')
        .then(response => response.data)
        .finally(() => console.log('done'))
}
  
  
export function getPerson(id: number): Promise<Person> {
    console.log(`getting person ${id}`)
    return axios.get(`/api/person/${id}`)
        .then(response => response.data)
        .finally(() => console.log('done'))
}


export function getScores(person_id: number): Promise<Scores> {
    console.log(`getting score for person ${person_id}`)
    return axios.get(`/api/person/${person_id}/scores/`)
        .then(response => response.data)
        .catch((error) => {
            
        })
        .finally(() => console.log('done'))
}


export function getEntries(person_id: number): Promise<Entry[]> {
    console.log(`getting entries for person ${person_id}`)
    return axios.get(`/api/person/${person_id}/entries/`)
        .then(response => response.data)
        .finally(() => console.log('done'))
}


export function searchPersons(search_term: string): Promise<Person[]> {
    console.log(`searching persons for ${search_term}`)
    const params: { [key: string]: string } = {}
    params['search_term'] = search_term
    return axios.get(`/api/person/`, { params: params })
        .then(response => response.data)
        .finally(() => console.log('done'))
}


export function addPerson(person: PersonNoID): Promise<Person> {
  console.log(`adding person ${person.name}`)
  return axios.post('/api/person', person)
    .then(response => response.data)
    .finally(() => console.log('done'))
}
