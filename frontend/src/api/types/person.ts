export type PersonNoID = {
  user_id: number
  name: string
  surname: string
  image_url: string
}

export type Person = PersonNoID & {
  id: number
}
