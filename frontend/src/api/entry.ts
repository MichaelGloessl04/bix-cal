import axios from "axios";
import type { EntryNoID } from "./types/entry";


export function addEntry(entry: EntryNoID) {
  console.log("adding entry")
  return axios.put("/api/entry", entry)
    .then(response => response.data)
    .finally(() => {console.log("done")});
}