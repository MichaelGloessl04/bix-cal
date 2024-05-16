import axios from "axios"

import type { User } from '@/api/types/user'


export function getUser(email: string): Promise<User> {
    console.log(`getting user ${email}`)
    return axios.get(`/api/user/${email}`)
        .then(response => response.data)
        .finally(() => console.log('done'))
}
