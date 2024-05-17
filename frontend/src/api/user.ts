import axios from "axios"

import type { User, UserNoID } from '@/api/types/user'


export function getUser(email: string): Promise<User> {
    console.log(`getting user ${email}`)
    return axios.get(`/api/user/${email}`)
        .then(response => response.data)
        .catch((error) => console.log(error))
        .finally(() => console.log('done'))
}


export function createUser(user: UserNoID): Promise<User> {
    console.log(`creating user ${user.username}`)
    return axios.post('/api/user', user)
        .then(response => response.data)
        .catch((error) => console.log(error))
        .finally(() => console.log('done'))
}
