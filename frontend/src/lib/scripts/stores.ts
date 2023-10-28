import { writable, type Writable } from "svelte/store";
export const userLogged = writable(false);

interface UserParams {
    id: number;
    username: string;
};

class UserStore {
    public id: Writable<Number>;
    public username: Writable<string>

    constructor () {
        this.id = writable(0);
        this.username = writable("");
    };

    init(params: UserParams) {
        this.id.set(params.id);
        this.username.set(params.username);
    }
    

}

export const userState: UserStore  = new UserStore();

