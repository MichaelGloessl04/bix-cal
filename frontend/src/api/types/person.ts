export type PersonNoID = {
  creator_id: number
  name: string
  surname: string
}

export type Person = PersonNoID & {
  id: number
}
