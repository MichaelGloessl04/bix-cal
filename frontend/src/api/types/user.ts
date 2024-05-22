export type UserNoID = {
  username: string
  email: string
}

export type User = UserNoID & {
  id: number
}
