export type EntryNoID = {
  person_id: number
  author_id: number
  hot: number
  crazy: number
  nice: number
  comment: string
}

export type Entry = EntryNoID & {
  id: number
}
