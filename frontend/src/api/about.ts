import axios from "axios";


export function getAbout(): Promise<string> {
    console.log(`getting about`)
    return axios.get(`/api/`)
        .then(response => response.data)
        .catch((error) => console.log(error))
        .finally(() => console.log('done'))
}
