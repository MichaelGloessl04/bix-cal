import axios from 'axios'
import type { Entry, EntryNoID } from './types/entry'

export function addEntry(entry: EntryNoID) {
  console.log('adding entry')
  return axios
    .post('/api/entry', entry)
    .then((response) => response.data)
    .finally(() => {
      console.log('done')
    })
}

export function updateEntry(entry_id: number, entry: EntryNoID) {
  console.log('updating entry')
  return axios
    .put(`/api/entry/${entry_id}`, entry)
    .then((response) => response.data)
    .finally(() => {
      console.log('done')
    })
}
  
