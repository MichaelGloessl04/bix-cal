export type UserNoID = {
  person_id: number
  username: string
  email: string
}

export type User = UserNoID & {
  id: number
}
