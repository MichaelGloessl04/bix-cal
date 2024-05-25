export type RatingNoID = {
  person_id: number
  user_id: number
  score: number
  hot: number
  crazy: number
  nice: number
  comment: string
}

export type Rating = RatingNoID & {
  id: number
}
