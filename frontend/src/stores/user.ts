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

    function clearUser() {
        user.value = {
            id: 0,
            username: '',
        }
    }

    function isLoggedIn() {
        return user.value.id !== 0
    }

    return { user, setUser, clearUser, isLoggedIn}
})
