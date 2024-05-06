import { defineStore } from "pinia";
import { ref, type Ref } from "vue";

import type { User } from "@/types/user";

export const useUserStore = defineStore('user', () => {
    const user: Ref<User> = ref({
        id: 0,
        username: '',
    })

    function setUser(newUser: User) {
        user.value = newUser
    }

    return { user, setUser}
})
