import axios from "axios";


export function getAbout(): Promise<string> {
    console.log(`getting about`)
    return axios.get(`/api/`)
        .then(response => response.data)
        .finally(() => console.log('done'))
}
