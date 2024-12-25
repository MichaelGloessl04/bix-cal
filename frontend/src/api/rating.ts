import axios from 'axios'
import type { Rating, RatingNoID } from './types/rating'

export async function getRating(rating_id: number): Promise<Rating> {
  const response = await axios.get(`/api/rating/${rating_id}`)
  return response.data
}

export async function getPersonRatings(person_id: number): Promise<Rating[]> {
  const response = await axios.get(`/api/rating/${person_id}`)
  return response.data
}

export async function getAverageRating(person_id: number): Promise<Rating> {
  const response = await axios.get(`/api/rating/average/${person_id}`)
  return response.data
}

export async function createRating(rating: RatingNoID): Promise<Rating> {
  const response = await axios.post('/api/rating', rating)
  return response.data
}

export async function updateRating(rating_id: number, rating: Rating): Promise<Rating> {
  const response = await axios.put(`/api/rating/${rating_id}`, rating)
  return response.data
}

export async function deleteRating(rating_id: number): Promis<Rating> {
  const response = await axios.delete(`/api/rating/${rating_id}`)
}
