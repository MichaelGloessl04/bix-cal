export type PersonNoID = {
    name: string
    surname: string
}

export type Person = PersonNoID & {
    id: number
}
