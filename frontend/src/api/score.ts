import axios from "axios";

import type { Scores } from '@/api/types/scores'

export function getScore(person_id: number): Promise<Scores> {
    console.log(`getting score for person ${person_id}`)
    return axios.get(`/api/person/${person_id}/score/`)
        .then(response => response.data)
        .catch((error) => console.log(error))
        .finally(() => console.log('done'))
}
